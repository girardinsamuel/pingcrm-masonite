"""User Table Seeder.

You can run this seeder in order to generate users.

    - Each time it is ran it will generate 50 random users.
    - All users have the password of 'secret'.
    - You can run the seeder by running: craft seed:run.
"""

from masoniteorm.seeds import Seeder
from app.User import User
from config.factories import Factory


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        Factory(User, 5).create()
