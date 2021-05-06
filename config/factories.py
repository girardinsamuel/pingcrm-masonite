import random
import string
from masoniteorm import Factory
from masonite.helpers import password
from app.User import User
from app.Organization import Organization
from app.Contact import Contact


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def user_factory(self, faker):
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "password": password("secret"),
        "remember_token": get_random_string(10),
        "owner": False,
        "photo_path": "",
    }


def organization_factory(self, faker):
    return {
        "name": faker.name(),
        "email": faker.email(),
        "phone": faker.phone(),
        "address": faker.address(),
        "city": faker.city(),
        "region": faker.region(),
        "country": "US",
        "postal_code": faker.post_code(),
    }


def contact_factory(self, faker):
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "phone": faker.phone(),
        "address": faker.address(),
        "city": faker.city(),
        "region": faker.region(),
        "country": "US",
        "postal_code": faker.post_code(),
    }


Factory.register(User, user_factory)
Factory.register(Organization, organization_factory)
Factory.register(Contact, contact_factory)
