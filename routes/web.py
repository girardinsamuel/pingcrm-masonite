"""Web Routes."""
from masonite.routes import Get, Post, Delete
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

    # Get("/register", "auth.RegisterController@show").name("register"),
    # Post("/register", "auth.RegisterController@store"),

    # Get("/home", "auth.HomeController@show").name("home"),
    # Get("/email/verify", "auth.ConfirmController@verify_show").name("verify"),
    # Get("/email/verify/@id:signed", "auth.ConfirmController@confirm_email"),
    # Get("/email/verify/@id:signed", "auth.ConfirmController@confirm_email"),
    # Get("/password", "auth.PasswordController@forget").name("forgot.password"),
    # Post("/password", "auth.PasswordController@send"),
    # Get("/password/@token/reset", "auth.PasswordController@reset").name(
    #     "password.reset"
    # ),
    # Post("/password/@token/reset", "auth.PasswordController@update"),
]

# ROUTES += Auth.routes()
