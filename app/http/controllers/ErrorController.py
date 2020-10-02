"""A ErrorController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class ErrorController(Controller):
    """ErrorController Controller Class."""

    def __init__(self, request: Request):
        """ErrorController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        raise Exception("Error 500")
