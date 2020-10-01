import random
import string
from masoniteorm import Factory
from masonite.helpers import password
from app.User import User
from app.Organization import Organization


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def user_factory(faker):
    return {
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'password': password('secret'),
        'remember_token': get_random_string(10),
        'owner': False,
        'photo_path': ''
    }

def organization_factory(faker):
    return {
        'name': faker.company(),
        'email': faker.email(),
        'phone': "0656453423",
        'address': faker.address(),
        'city': faker.city(),
        'region': faker.state(),
        'country': 'US',
        'postal_code': faker.postcode()
    }

Factory.register(User, user_factory)
Factory.register(Organization, organization_factory)
