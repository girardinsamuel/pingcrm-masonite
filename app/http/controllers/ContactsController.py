"""A ContactsController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse
from masonite.validation import Validator

from app.Contact import Contact
from app.Organization import Organization


class ContactsController(Controller):
    """ContactsController Controller Class."""

    def __init__(self, request: Request):
        """ContactsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):
        # contacts = self.request.user().account.contacts().order_by_name().filter(
        #     self.request.only('search', 'role', 'trashed')
        # ).get()
        contacts = (
            Contact.where("account_id", self.request.user().account.id)
            .order_by_name()
            .filter(self.request.only("search", "trashed"))
            .get()
        )
        # TODO: add pagination
        # contacts = self.request.user().account.contacts
        # TODO: how to include organization data (e.g. name) for each contact instead of the id
        return view.render(
            "Contacts/Index",
            {
                "filters": self.request.all(internal_variables=False),
                "contacts": {"data": contacts.serialize(), "links": []},
            },
        )

    def create(self, view: InertiaResponse):
        # TODO: order by name, return only id and name !
        # 'organizations' => Auth::user()->account
        #         ->organizations()
        #         ->orderBy('name')
        #         ->get()
        #         ->map
        #         ->only('id', 'name'),
        return view.render(
            "Contacts/Create",
            {"organizations": self.request.user().account.organizations.serialize()},
            # {
            #     "organizations": Organization.where(
            #         "account_id", self.request.user().account.id
            #     )
            #     # .order_by_name() raise error about a first_name column...
            #     .get().serialize()
            # },
        )

    def edit(self, view: InertiaResponse):
        contact = Contact.find(self.request.param("contact"))
        # TODO: not working yet
        # contact = contact.with_('organizations').get().serialize()
        return view.render(
            "Contacts/Edit", {"contact": contact.serialize(), "organizations": []}
        )

    def store(self, view: InertiaResponse, validate: Validator):
        # TODO: add nullable
        # TODO: check organization id exists and is an organization linked to the user account
        errors = self.request.validate(
            validate.required(["first_name", "last_name"]),
            validate.length(
                ["first_name", "last_name", "email", "phone", "city", "region"], max=50
            ),
            validate.email("email"),
            validate.length(["address"], max=150),
            validate.length(["country"], max=2),
            validate.length(["postal_code"], max=25),
        )
        if errors:
            return (
                self.request.redirect_to("contacts.create")
                .with_errors(errors)
                .with_input()
            )

        Contact.create(
            first_name=self.request.input("first_name"),
            last_name=self.request.input("last_name"),
            email=self.request.input("email"),
            phone=self.request.input("phone"),
            address=self.request.input("address"),
            city=self.request.input("city"),
            postal_code=self.request.input("postal_code"),
            region=self.request.input("region"),
            country=self.request.input("country"),
            account_id=self.request.user().account.id,
            organization_id=self.request.input("organization_id"),
        )

        self.request.session.flash("success", "Contact created.")
        return self.request.redirect_to("contacts")

    def destroy(self, view: InertiaResponse):
        Contact.where("id", self.request.param("contact")).delete()
        self.request.session.flash("success", "Contact deleted.")
        return self.request.redirect_to("contacts")
