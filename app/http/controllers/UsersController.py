"""A UsersController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse

from app.User import User


class UsersController(Controller):
    """UsersController Controller Class."""

    def __init__(self, request: Request):
        """UsersController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):

        return view.render('Users/Index', {
            'filters': [],
            'users': self.request.user().account.users.transform(lambda user: {
                'id': user.id,
                'email': user.email,
                'name': user.last_name + ' ' + user.first_name,
                'owner': user.owner,
                'photo': '#',
                'deleted_at': user.deleted_at
            }).serialize()
        })

    def create(self, view: InertiaResponse):
        return view.render('Users/Create')

    def edit(self, view: InertiaResponse):
        user = User.find(self.request.param("user"))
        return view.render('Users/Edit', {
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'owner': user.owner,
                'photo': '#', # user.photoUrl(['w' => 60, 'h' => 60, 'fit' => 'crop']),
                'deleted_at': user.deleted_at,
            },
        })
    
    def update(self, view: InertiaResponse):
        user = User.find(self.request.param("user"))
        if user.is_demo_user:
            self.request.session.flash('error', 'Updating the demo user is not allowed.')
            return self.request.redirect(f"/users/{user.id}/edit") #.with_errors("Updating the demo user is not allowed.")

        # check demo
        # errors = request.validate(
        #     validate.required(["name", "email", "password"]),
        #     validate.email("email"),
        #     validate.strong(
        #         "password",
        #         length=8,
        #         special=1,
        #         uppercase=1,
        #         # breach=True checks if the password has been breached before.
        #         # Requires 'pip install pwnedapi'
        #         breach=False,
        #     ),
        # )

        self.request.session.flash('success', 'User updated.')
        return self.request.back()

    #     if (App::environment('demo') && $user->isDemoUser()) {
    #         return Redirect::back()->with('error', 'Updating the demo user is not allowed.');
    #     }

    #     Request::validate([
    #         'first_name' => ['required', 'max:50'],
    #         'last_name' => ['required', 'max:50'],
    #         'email' => ['required', 'max:50', 'email', Rule::unique('users')->ignore($user->id)],
    #         'password' => ['nullable'],
    #         'owner' => ['required', 'boolean'],
    #         'photo' => ['nullable', 'image'],
    #     ]);

    #     $user->update(Request::only('first_name', 'last_name', 'email', 'owner'));

    #     if (Request::file('photo')) {
    #         $user->update(['photo_path' => Request::file('photo')->store('users')]);
    #     }

    #     if (Request::get('password')) {
    #         $user->update(['password' => Request::get('password')]);
    #     }

        
    #     return Redirect::back()->with('success', 'User updated.');
    # }
