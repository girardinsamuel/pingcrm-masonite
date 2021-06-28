"""A DashboardController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.inertia import Inertia


class DashboardController(Controller):
    """DashboardController Controller Class."""

    def __init__(self, request: Request):
        """DashboardController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: Inertia):
        return view.render('Dashboard/Index')
