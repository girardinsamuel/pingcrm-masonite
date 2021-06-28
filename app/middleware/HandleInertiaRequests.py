from masonite.inertia import InertiaMiddleware


class HandleInertiaRequests(InertiaMiddleware):

    root_view = "app"

    def share(self, request):
        # add shared data
        def get_auth():
            # TODO: submit PR to set _user=None on request class in M4
            user = request.user() if hasattr(request, "_user") else None
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

        return {
            'auth': get_auth
        }