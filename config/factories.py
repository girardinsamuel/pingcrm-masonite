import random
import string
from orator.orm import Factory
from masonite.helpers import password
from app.User import User

factory = Factory()


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def users_factory(faker):
    return {
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'password': password('secret'),
        'remember_token': get_random_string(10),
        'owner': False
    }


factory.register(User, users_factory)
