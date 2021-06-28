from masonite.providers import Provider
from ..listeners.SendResetPasswordListener import SendResetPasswordListener

class EventProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.make('event').listen('auth.password_reset', [
                SendResetPasswordListener
            ]
        )

    def boot(self):
        pass