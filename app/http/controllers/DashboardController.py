"""A DashboardController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse


class DashboardController(Controller):
    """DashboardController Controller Class."""

    def __init__(self, request: Request):
        """DashboardController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):
        return view.render('Dashboard/Index')
