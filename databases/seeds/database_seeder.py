"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder
from config.factories import Factory
import random

from app.Account import Account
from app.Organization import Organization
from app.Contact import Contact


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # self.call(UserTableSeeder)
        account = Account.first()

        # organizations = Factory(Organization, 100).create({"account_id": account.id})
        organizations = Organization.all()
        contacts = Factory(Contact, 100).create({"account_id": account.id})
        for c in contacts:
            c.update({"organization_id": organizations[random.randint(0, 99)].id})
