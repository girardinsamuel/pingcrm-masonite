from masonite.provider import ServiceProvider
from masonite.auth import Auth


class MyAppProvider(ServiceProvider):
    """Custom app provider to configure app"""

    wsgi = False

    def boot(self, auth: Auth):
        # update default view to use with Inertia
        # inertia.set_root_view("spa_view")
        # add shared data
        # auth = self.app.make('Auth')

        def get_auth():
            if auth.user():
                return {
                    'user': {
                        'id': auth.user().id,
                        'first_name': auth.user().first_name,
                        'last_name': auth.user().last_name,
                        'email': auth.user().email,
                        'role': auth.user().role,
                        'account': {
                            'id': auth.user().account.id,
                            'name': auth.user().account.name
                        }
                    }
                }
            else:
                return {'user': None}

        self.app.make('Inertia').share({
            'auth': get_auth
        })
