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
        # contacts = self.request.user().account.contacts().order_by_name().filter(
        #     self.request.only('search', 'role', 'trashed')
        # ).get()
        contacts = self.request.user().account.contacts.get()
        return view.render('Contacts/Index', {
            'filters': self.request.all(internal_variables=False),
            'users': contacts.serialize()
        })
