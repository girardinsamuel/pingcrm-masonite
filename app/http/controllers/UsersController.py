"""A UsersController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse
from masonite.validation import Validator
from masonite import Upload

from app.User import User


class UsersController(Controller):
    """UsersController Controller Class."""

    def __init__(self, request: Request):
        """UsersController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):
        users = User.where("account_id", self.request.user().account.id).order_by_name().filter(
            self.request.only('search', 'role', 'trashed')
        ).get()
        return view.render('Users/Index', {
            'filters': self.request.all(internal_variables=False),
            'users': users.serialize()
        })

    def create(self, view: InertiaResponse):
        return view.render('Users/Create')

    def edit(self, view: InertiaResponse):
        user = User.find(self.request.param("user"))
        return view.render('Users/Edit', {
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'owner': user.owner,
                'photo': user.photo_path,
                'deleted_at': user.deleted_at,
            }
        })

    def store(self, view: InertiaResponse, validate: Validator, upload: Upload):
        errors = self.request.validate(
            validate.required(['email', 'first_name', 'last_name', 'owner']),
            validate.truthy('owner'),
            validate.length(['first_name', 'last_name', 'email'], max=50),
            validate.email('email'),
            # validate.when(
            #     validate.exists('photo')
            # ).then(
            #     validate.image('photo')
            # ), TODO: fix the error, file validators do not work with FieldStorage for now ...
            validate.when(
                validate.isnt(validate.none('password'))
            ).then(
                validate.strong('password', length=8, special=1)
            )
        )

        if errors:
            return self.request.redirect_to('users.create').with_errors(errors).with_input()

        photo_path = None
        if self.request.input('photo'):
            # save file
            photo_path = upload.driver('disk').store(self.request.input('file_upload'), location='disk.profiles')

        User.create(
            first_name=self.request.input('first_name'),
            last_name=self.request.input('last_name'),
            email=self.request.input('email'),
            owner=self.request.input('owner'),
            password=self.request.input('password'),
            photo_path=photo_path,
            account_id=self.request.user().account.id
        )

        self.request.session.flash('success', 'User created.')
        return self.request.redirect_to('users')

    def update(self, view: InertiaResponse, validate: Validator, upload: Upload):
        user = User.find(self.request.param("user"))
        if user.is_demo_user:
            return self.request.redirect_to("users.edit", {"user": user.id}).with_errors("Updating the demo user is not allowed.")

        errors = self.request.validate(
            validate.required(['first_name', 'last_name', 'email', 'owner']),
            validate.length(['first_name', 'last_name', 'email'], max=50),
            # TODO: add unique validator for email
            validate.email('email'),
            # TODO: add nullable validator to avoid doing this trick...
            validate.when(
                validate.isnt(validate.none('password'))
            ).then(
                validate.strong('password', length=8, special=1)
            )
        )
        if errors:
            return self.request.redirect_to("users.edit", {"user": user.id}).with_errors(errors).with_input()

        # update user
        user.first_name = self.request.input('first_name')
        user.last_name = self.request.input('last_name')
        user.email = self.request.input('email')
        user.owner = self.request.input('owner')

        photo_path = None
        if self.request.input('photo'):
            photo_path = upload.driver('disk').store(self.request.input('file_upload'),
                                                     location='disk.profiles')
            user.photo_path = photo_path

        user.save()

        self.request.session.flash('success', 'User updated.')
        # @issue: this does not work => 404
        # return self.request.back()
        return self.request.redirect_to("users.edit", {"user": user.id})  # gone for now : .with_success("User updated.")


    def destroy(self, view: InertiaResponse):
        user = User.find(self.request.param("user"))
        if user.is_demo_user:
            self.request.redirect_to("users").with_errors("Deleting the demo user is not allowed.")

        user.delete()
        self.request.session.flash('success', 'User deleted.')
        return self.request.redirect_to('users')
