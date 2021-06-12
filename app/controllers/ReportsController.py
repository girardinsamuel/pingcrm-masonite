"""A ReportsController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.inertia import Inertia


class ReportsController(Controller):
    """ReportsController Controller Class."""

    def __init__(self, request: Request):
        """ReportsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: Inertia):
        return view.render("Reports/Index")
