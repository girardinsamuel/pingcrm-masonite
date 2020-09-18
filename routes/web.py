"""Web Routes."""
from masonite.routes import Get
from masonite.auth import Auth

ROUTES = [
    Get('/', 'DashboardController@show').name('dashboard'),
]

ROUTES += Auth.routes()
