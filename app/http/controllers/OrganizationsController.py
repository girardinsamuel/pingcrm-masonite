"""A OrganizationsController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.validation import Validator
from masonite.inertia import InertiaResponse

from app.Organization import Organization


class OrganizationsController(Controller):
    """OrganizationsController Controller Class."""

    def __init__(self, request: Request):
        """OrganizationsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):

        organizations = self.request.user().account.organizations
        # TODO add pagination
        return view.render(
            "Organizations/Index",
            {
                "filters": self.request.all(internal_variables=False),
                "organizations": {"data": organizations.serialize(), "links": []},
            },
        )

    def create(self, view: InertiaResponse):
        return view.render("Organizations/Create")

    def edit(self, view: InertiaResponse):
        # org = Organization.find(self.request.param("organization"))
        # organization = org.with_("contacts").get().serialize()
        organization = (
            Organization.where("id", self.request.param("organization"))
            .with_("contacts")
            .get()
            .first()
            .serialize()
        )
        return view.render("Organizations/Edit", {"organization": organization})

    def store(self, view: InertiaResponse, validate: Validator):
        # TODO: add nullable rule
        # TODO: add postal_code rule
        errors = self.request.validate(
            validate.required(["name"]),
            validate.length(["email", "phone", "city", "region"], max=50),
            validate.length(["name"], min=2, max=100),
            # validate.length('address', max=150),
            # validate.length('country', max=2),
            # validate.length('postal_code', max=25),
            # validate.email('email'),
            # 'name': 'required|length:2,100',
            # 'email': 'length:3,50|email',
            # 'phone': 'length:3,50',
            # 'address': 'length:3,150',
            # 'city': 'length:3,50',
            # 'region': 'length:3,50',
            # 'country': 'length:0,2',
            # 'postal_code': 'length:2,25'
        )
        if errors:
            # return self.request.back().with_errors(errors).with_input()
            return (
                self.request.redirect_to("organizations.create")
                .with_errors(errors)
                .with_input()
            )

        Organization.create(
            **self.request.only(
                "name",
                "email",
                "phone",
                "address",
                "city",
                "region",
                "postal_code",
                "country",
            ),
            account_id=self.request.user().account.id,
        )
        return self.request.redirect_to("organizations").with_success(
            "Organization created."
        )

    def update(self, view: InertiaResponse, validate: Validator):
        org = Organization.find(self.request.param("organization"))

        # TODO: add nullable rule
        # TODO: add postal_code rule
        errors = self.request.validate(
            validate.required(["name"]),
            validate.length(["email", "phone", "city", "region"], max=50),
            validate.length(["name"], min=2),
        )

        if errors:
            return (
                self.request.redirect_to("organizations.edit", {"organization": org.id})
                .with_errors(errors)
                .with_input()
            )

        org.update(
            self.request.only(
                "name",
                "email",
                "phone",
                "address",
                "city",
                "region",
                "postal_code",
                "country",
            )
        )
        return self.request.redirect_to("organizations").with_success(
            "Organization updated."
        )

    def destroy(self, view: InertiaResponse):
        org = Organization.find(self.request.param("organization"))
        org.delete()
        return self.request.redirect_to("organizations").with_success(
            "Organization deleted."
        )
