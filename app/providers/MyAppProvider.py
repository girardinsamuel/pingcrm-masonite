from masonite.provider import ServiceProvider
from masonite.auth import Auth


class MyAppProvider(ServiceProvider):
    """Custom app provider to configure app"""

    wsgi = False

    def boot(self, auth: Auth):
        # add shared data
        def get_auth():
            user = auth.user()
            if user:
                return {
                    'user': {
                        'id': user.id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'role': user.role,
                        'account': {
                            'id': user.account.id,
                            'name': user.account.name
                        }
                    }
                }
            else:
                return {'user': None}

        self.app.make('Inertia').share({
            'auth': get_auth
        })
