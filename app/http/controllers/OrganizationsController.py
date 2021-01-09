"""A OrganizationsController Module."""

from masonite.request import Request
from masonite.view import View
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
                "organizations": {"data": organizations.serialize(), "links": []}
                # 'organizations': organizations.transform(lambda org: {
                #     'id': org.id,
                #     'name': org.name,
                #     'phone': org.phone,
                #     'city': org.city,
                #     'deleted_at': org.deleted_at
                # }).serialize()
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
            # return view.render('Organizations/Create').with_errors(errors).with_input()
            return (
                self.request.redirect_to("organizations.create")
                .with_errors(errors)
                .with_input()
            )

        Organization.create(
            name=self.request.input("name"),
            email=self.request.input("email"),
            phone=self.request.input("phone"),
            address=self.request.input("address"),
            city=self.request.input("city"),
            region=self.request.input("region"),
            postal_code=self.request.input("postal_code"),
            country=self.request.input("country"),
            account_id=self.request.user().account.id,
        )

        self.request.session.flash("success", "Organization created.")
        return self.request.redirect_to("organizations")

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

        # TODO: how to update more quickly/cleanly ?
        org.name = self.request.input("name")
        org.email = self.request.input("email")
        org.phone = self.request.input("phone")
        org.address = self.request.input("address")
        org.city = self.request.input("city")
        org.region = self.request.input("region")
        org.postal_code = self.request.input("postal_code")
        org.country = self.request.input("country")
        org.save()

        self.request.session.flash("success", "Organization updated.")
        return self.request.redirect_to("organizations")

    def destroy(self, view: InertiaResponse):
        org = Organization.find(self.request.param("organization"))
        org.delete()
        self.request.session.flash("success", "Organization deleted.")
        return self.request.redirect_to("organizations")
