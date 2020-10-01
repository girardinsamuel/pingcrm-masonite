"""A UsersController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse
from masonite.validation import Validator
from masonite import Upload

from app.User import User
from app.Account import Account


class UsersController(Controller):
    """UsersController Controller Class."""

    def __init__(self, request: Request):
        """UsersController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def index(self, view: InertiaResponse):
        # users = Account.users_of_account(self.request.user().account.id)
        import pdb
        pdb.set_trace()
        users = self.request.user().account.users().order_by_name().filter(
            self.request.only('search', 'role', 'trashed')
        ).get()
        return view.render('Users/Index', {
            'filters': self.request.all(internal_variables=False),
            'users': users.transform(lambda user: {
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
        def lazy_prop():
            return "6"
        user = User.find(self.request.param("user"))
        return view.render('Users/Edit', {
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'owner': user.owner,
                'photo': '#', # TODO: user.photoUrl(['w' => 60, 'h' => 60, 'fit' => 'crop']),
                'deleted_at': user.deleted_at,
            },
            'other_one': lazy_prop
        })

    def store(self, view: InertiaResponse, validate: Validator, upload: Upload):
        errors = self.request.validate(
            validate.required(['email', 'first_name', 'last_name', 'owner']),
            validate.truthy('owner'),
            validate.length(['first_name', 'last_name', 'email'], max=50),
            validate.email('email'),
            # validate.when(
            #     validate.exists('photo')
            # ).then(
            #     validate.image('photo')
            # ), TODO: fix the error, file validators do not work with FieldStorage for now ...
            validate.when(
                validate.exists('password')
            ).then(
                validate.strong('password', length=8, special=1)
            )
        )

        if errors:
            # return self.request.back().with_errors(errors).with_input()
            # return view.render('Users/Create').with_errors(errors).with_input()
            return self.request.redirect('users/create').with_errors(errors).with_input()

        photo_path = None
        if self.request.input('photo'):
            # save file
            photo_path = upload.driver('disk').store(self.request.input('file_upload'), location='disk.profiles')

        self.request.user().account.users().create(
            first_name=self.request.input('first_name'),
            last_name=self.request.input('last_name'),
            email=self.request.input('email'),
            owner=self.request.input('owner'),
            password=self.request.input('password'),
            photo_path=photo_path
        )

        self.request.session.flash('success', 'User created.')
        return self.request.redirect('/users')

    def update(self, view: InertiaResponse, validate: Validator, upload: Upload):
        user = User.find(self.request.param("user"))
        if user.is_demo_user:
            self.request.session.flash('error', 'Updating the demo user is not allowed.')
            return self.request.redirect(f"/users/{user.id}/edit") #.with_errors("Updating the demo user is not allowed.")

        errors = self.request.validate(
            validate.required(['first_name', 'last_name', 'email', 'owner']),
            validate.length(['first_name', 'last_name', 'email'], max=50),
            validate.email('email'),
            validate.when(
                validate.exists('password')
            ).then(
                validate.strong('password', length=8, special=1)
            )
            # TODO: add unique
        )

        if errors:
            return self.request.redirect(f"users/{user.id}").with_errors(errors).with_input()

        # update user
        user.first_name = self.request.input('first_name')
        user.last_name = self.request.input('last_name')
        user.email = self.request.input('email')
        user.owner = self.request.input('owner')

        if self.request.input('password'):
            pass

        photo_path = None
        if self.request.input('photo'):
            photo_path = upload.driver('disk').store(self.request.input('file_upload'),
                                                     location='disk.profiles')
            user.photo_path = photo_path

        user.save()

        self.request.session.flash('success', 'User updated.')
        return self.request.back()

    def destroy(self, view: InertiaResponse):
        user = User.find(self.request.param('user'))

        if user.is_demo_user:
            self.request.session.flash('error', 'Deleting the demo user is not allowed.')
            self.request.redirect(f"/users/{user.id}")

        user.delete()

        self.request.session.flash('success', 'User deleted.')
        return self.request.redirect_to('users')
        # OR return self.request.back()
