"""A OrganizationsController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse


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
        return view.render('Organizations/Index', {
            'filters': self.request.all(internal_variables=False),
            'organizations': {
                'data': organizations.serialize(),
                'links': []
            }
            # 'organizations': organizations.transform(lambda org: {
            #     'id': org.id,
            #     'name': org.name,
            #     'phone': org.phone,
            #     'city': org.city,
            #     'deleted_at': org.deleted_at
            # }).serialize()
        })

    def create(self, view: InertiaResponse):
        return view.render('Organizations/Create')

    def edit(self, view: InertiaResponse):
        pass