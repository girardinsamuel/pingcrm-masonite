from masonite.middleware import Middleware


class CorsMiddleware(Middleware):

    def before(self, request, response):
        response.header('Access-Control-Allow-Origin', '*')
        response.header('Access-Control-Allow-Methods', 'GET,PUT')
        response.header('Access-Control-Allow-Headers', 'Content-Type, Accept, X-Requested-With,Access-Control-Allow-Origin,X-API-KEY')
        response.header('Access-Control-Max-Age', '3600')
        response.header('Access-Control-Allow-Credentials', 'true')
        if request.get_request_method().lower() == "options":
            response.view("preflight", status=200)
        return request

    def after(self, request, response):

        return request


