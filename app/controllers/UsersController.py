"""A UsersController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.inertia import Inertia
# from masonite.validation import Validator

from app.User import User


class UsersController(Controller):
    """UsersController Controller Class."""

    def __init__(self, request: Request):
        """UsersController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: Inertia):
        users = (
            User.where("account_id", self.request.user().account.id)
            .order_by_name()
            .filter(self.request.only("search", "role", "trashed"))
            .get()
        )
        return view.render(
            "Users/Index",
            {
                "filters": self.request.all(internal_variables=False),
                "users": users.serialize(),
            },
        )

    def create(self, view: Inertia):
        return view.render("Users/Create")

    def edit(self, view: Inertia):
        user = User.with_trashed().find(self.request.param("user"))
        return view.render(
            "Users/Edit",
            {
                "user": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "owner": user.owner,
                    "photo": user.photo,
                    "deleted_at": user.deleted_at,
                }
            },
        )

    def store(self, view: Inertia):
    # def store(self, view: Inertia, validate: Validator):
        # errors = self.request.validate(
        #     validate.required(["email", "first_name", "last_name", "owner"]),
        #     validate.truthy("owner"),
        #     validate.length(["first_name", "last_name", "email"], max=50),
        #     validate.email("email"),
        #     validate.when(validate.isnt(validate.none("photo"))).then(
        #         validate.image("photo"),
        #     ),
        #     # 3 ISSUES:
        #     # - do we need to override driver to support uploading pdfs ?
        #     # - if not valid, request.input() put the file in the request, and the request is too big
        #     # validate.image("photo"),
        #     validate.when(validate.isnt(validate.none("password"))).then(
        #         validate.strong("password", length=8, special=1),
        #     ),
        # )
        errors = None

        if errors:
            return (
                self.request.redirect_to("users.create")
                .with_errors(errors)
                .with_input()
            )

        # save file if any
        photo_path = None
        if self.request.input("photo") != "":
            photo_path = self.request.app.make("storage").disk("local").store(
                self.request.input("photo"), location="disk.users"
            )

        User.create(
            **self.request.only(
                "first_name", "last_name", "email", "owner", "password"
            ),
            photo_path=photo_path,
            account_id=self.request.user().account.id,
        )

        return self.request.redirect_to("users").with_success("User created.")

    def update(self, view: Inertia):
    # def update(self, view: Inertia, validate: Validator):
        user = User.find(self.request.param("user"))
        if user.is_demo_user:
            return self.request.redirect_to(
                "users.edit", {"user": user.id}
            ).with_errors("Updating the demo user is not allowed.")

        # errors = self.request.validate(
        #     validate.required(["first_name", "last_name", "email", "owner"]),
        #     validate.length(["first_name", "last_name", "email"], max=50),
        #     # TODO: add unique validator for email (waiting for PR to be merged)
        #     validate.email("email"),
        #     # TODO: add nullable validator to avoid doing this trick...
        #     validate.when(validate.isnt(validate.none("password"))).then(
        #         validate.strong("password", length=8, special=1)
        #     ),
        #     validate.when(validate.isnt(validate.none("photo"))).then(
        #         validate.image("photo"),
        #     ),
        # )
        errors = None
        if errors:
            return (
                self.request.redirect_to("users.edit", {"user": user.id})
                .with_errors(errors)
                .with_input()
            )

        photo_path = None
        if self.request.input("photo") != "":
            photo_path = self.request.app.make("storage").disk("local").store(
                self.request.input("photo"), location="disk.users"
            )
            user.photo_path = photo_path

        user.update(
            {
                **self.request.only(
                    "first_name", "last_name", "email", "owner", "password"
                ),
                "photo_path": photo_path,
            },
        )
        return self.request.redirect_to("users.edit", {"user": user.id}).with_success(
            "User updated."
        )

    def destroy(self, view: Inertia):
        user = User.find(self.request.param("user"))
        if user.is_demo_user:
            return self.request.redirect_to("users").with_errors(
                "Deleting the demo user is not allowed."
            )

        user.delete()
        self.request.session.flash("success", "User deleted.")
        return self.request.redirect_to("users")
