"""Web Routes."""
from masonite.routes import Get, Post
# from masonite.auth import Auth

ROUTES = [
    Get('/', 'DashboardController@index').name('dashboard'),

    Get('/login', 'auth.LoginController@show_login_form').name('login'), #.middleware('guest')
    Post("/login", "auth.LoginController@store").name('login.attempt'),
    Get("/logout", "auth.LoginController@logout").name("logout"),
    Get("/register", "auth.RegisterController@show").name("register"),
    Post("/register", "auth.RegisterController@store"),
    Get("/home", "auth.HomeController@show").name("home"),
    Get("/email/verify", "auth.ConfirmController@verify_show").name("verify"),
    Get("/email/verify/@id:signed", "auth.ConfirmController@confirm_email"),
    Get("/email/verify/@id:signed", "auth.ConfirmController@confirm_email"),
    Get("/password", "auth.PasswordController@forget").name("forgot.password"),
    Post("/password", "auth.PasswordController@send"),
    Get("/password/@token/reset", "auth.PasswordController@reset").name(
        "password.reset"
    ),
    Post("/password/@token/reset", "auth.PasswordController@update"),
]

# ROUTES += Auth.routes()
