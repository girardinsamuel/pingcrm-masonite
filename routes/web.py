"""Web Routes."""
from masonite.routes import Route

ROUTES = [
    # Auth
    # TODO: implement guest middleware in Masonite
    Route.get('/login', 'auth.LoginController@show_login_form').name('login'), #.middleware('guest')
    Route.post("/login", "auth.LoginController@store").name('login.attempt'),
    Route.post("/logout", "auth.LoginController@logout").name("logout"),

    # Dashboard
    Route.get('/', 'DashboardController@index').name('dashboard'),

    # # Users
    # Route.get('/users/@user/edit', 'UsersController@edit').name('users.edit'),
    # Route.get('/users/create', 'UsersController@create').name('users.create'),
    # Route.post('/users', 'UsersController@store').name('users.store'),
    # Route.post('/users/@user/', "UsersController@update").name('users.update'),
    # Route.get('/users', "UsersController@index").name('users'),
    # Route.delete('/users/@user', "UsersController@destroy").name('users.destroy'),

    # # Organizations
    # Route.get('/organizations', "OrganizationsController@index").name('organizations'),
    # Route.get('/organizations/create', "OrganizationsController@create").name('organizations.create'),
    # Route.get('/organizations/@organization/edit', "OrganizationsController@edit").name('organizations.edit'),
    # Route.put('/organizations/@organization', "OrganizationsController@update").name('organizations.update'),
    # Route.delete('/organizations/@organization', "OrganizationsController@destroy").name('organizations.destroy'),
    # Route.post('/organizations/', "OrganizationsController@store").name('organizations.store'),

    # # Contacts
    # Route.get('/contacts', "ContactsController@index").name('contacts'),
    # Route.get('/contacts/create', "ContactsController@create").name('contacts.create'),
    # Route.get('/contacts/@contact/edit', "ContactsController@edit").name('contacts.edit'),
    # Route.post('/contacts/', "ContactsController@store").name('contacts.store'),
    # Route.delete('/contacts/@contact', "ContactsController@destroy").name('contacts.destroy'),

    # Reports
    Route.get('/reports', "ReportsController@index").name('reports'),

    # Errors
    Route.get('/500', "ErrorController@show").name('500')
]
