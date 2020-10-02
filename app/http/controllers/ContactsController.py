"""A ContactsController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse
from masonite.validation import Validator

from app.Contact import Contact


class ContactsController(Controller):
    """ContactsController Controller Class."""

    def __init__(self, request: Request):
        """ContactsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):
        # TODO: does not work yet
        # contacts = self.request.user().account.contacts().order_by_name().filter(
        #     self.request.only('search', 'role', 'trashed')
        # ).get()
        # TODO: add pagination
        contacts = self.request.user().account.contacts
        return view.render('Contacts/Index', {
            'filters': self.request.all(internal_variables=False),
            'contacts': {
                "data": contacts.serialize(),
                "links": []
            }
        })

    def create(self, view: InertiaResponse):
        return view.render('Contacts/Create')

    def edit(self, view: InertiaResponse):
        contact = Contact.find(self.request.param('contact'))
        # TODO: not working yet
        # contact = contact.with_('organizations').get().serialize()
        return view.render("Contacts/Edit", {
            "contact": contact.serialize(),
            "organizations": []
        })

    def store(self, view: InertiaResponse):
        # TODO: implement
        self.request.session.flash('success', 'Contact created.')
        return view.redirect_to('contacts')

    def destroy(self, view: InertiaResponse):
        # TODO: can't do that yet
        # contact = Contact.find(self.request.param('contact'))
        # contact.delete()
        Contact.where("id", self.request.param('contact')).delete()
        self.request.session.flash('success', 'Contact deleted.')
        return self.request.redirect_to('contacts')
