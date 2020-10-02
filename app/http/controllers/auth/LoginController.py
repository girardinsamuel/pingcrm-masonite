"""A LoginController Module."""

from masonite.auth import Auth
from masonite.request import Request
from masonite.validation import Validator
from masonite.view import View
from masonite.inertia import InertiaResponse


class LoginController:
    """Login Form Controller."""

    def __init__(self):
        """LoginController Constructor."""
        pass

    def show_login_form(self, view: InertiaResponse):
        return view.render("Auth/Login")

    def store(self, request: Request, auth: Auth, validate: Validator):
        """Login the user.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
            auth {masonite.auth.auth} -- The Masonite auth class.
            validate {masonite.validator.Validator} -- The Masonite Validator class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """
        errors = request.validate(
            validate.required(["email", "password"]),
            validate.email("email"),
        )

        if errors:
            return request.back().with_errors(errors).with_input()

        if auth.login(request.input("email"), request.input("password")):
            return request.redirect("/")

        return request.back().with_errors({"email": "Email or password is incorrect"})

    def logout(self, request: Request, auth: Auth):
        """Log out the user.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
            auth {masonite.auth.auth} -- The Masonite auth class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """
        auth.logout()
        return request.redirect("/login")
