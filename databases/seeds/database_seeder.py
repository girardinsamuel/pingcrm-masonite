"""Base Database Seeder Module."""

from masoniteorm.seeds import Seeder
from masonite.helpers import password

from app.User import User
from app.Account import Account
from config.factories import Factory
from .user_table_seeder import UserTableSeeder


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
            owner=True,
            photo_path=""
        )

        Factory(User, 5).create({"account_id": account.id})
