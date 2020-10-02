"""Web Routes."""
from masonite.routes import Get, Post, Delete, Put
# from masonite.auth import Auth

ROUTES = [
    Get('/', 'DashboardController@index').name('dashboard').middleware('auth'),

    Get('/login', 'auth.LoginController@show_login_form').name('login'), #.middleware('guest')
    Post("/login", "auth.LoginController@store").name('login.attempt'),

    Post("/logout", "auth.LoginController@logout").name("logout"),

    # Users
    Get('/users/@user/edit', 'UsersController@edit').name('users.edit').middleware('auth'),
    Get('/users/create', 'UsersController@create').name('users.create').middleware('auth'),
    Post('/users', 'UsersController@store').name('users.store').middleware('auth'),
    Post('/users/@user', "UsersController@update").name('users.update').middleware('auth'),
    Get('/users', "UsersController@index").name('users').middleware('auth'),
    Delete('/users/@user', "UsersController@destroy").name('users.destroy').middleware('auth'),

    # Organizations
    Get('/organizations', "OrganizationsController@index").name('organizations').middleware('auth'),
    Get('/organizations/create', "OrganizationsController@create").name('organizations.create').middleware('auth'),
    Get('/organizations/@organization/edit', "OrganizationsController@edit").name('organizations.edit').middleware('auth'),
    Put('/organizations/@organization', "OrganizationsController@update").name('organizations.update').middleware('auth'),
    Delete('/organizations/@organization', "OrganizationsController@destroy").name('organizations.destroy').middleware('auth'),
    Post('/organizations/', "OrganizationsController@store").name('organizations.store').middleware('auth'),

    # Errors
    Get('/500', "ErrorController@show").name('500')
]

# ROUTES += Auth.routes()
