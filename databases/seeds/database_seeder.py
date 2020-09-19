"""Base Database Seeder Module."""

from orator.seeds import Seeder
from .user_table_seeder import UserTableSeeder
from masonite.helpers import password
from app.Account import Account
from app.User import User
from config.factories import factory


class DatabaseSeeder(Seeder):

    def run(self):
        """Run the database seeds."""
        # self.call(UserTableSeeder)
        account = Account.create(name="Acme Corporation")

        user = User.create(
            account_id=account.id,
            first_name="John",
            last_name="Doe",
            password=password('secret'),
            email="johndoe@example.com",
            owner=True
        )

        factory(User, 5).create(account_id=account.id)
