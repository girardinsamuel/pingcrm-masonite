"""User Model."""
from orator.orm import belongs_to, accessor

from config.database import Model
from app.Account import Account


class User(Model):
    """User Model."""

    __fillable__ = ['first_name', 'last_name', 'email', 'password', 'photo_path', 'owner', 'account_id']
    __append__ = ["role", "is_demo_user"]
    __auth__ = 'email'

    @belongs_to
    def account(self):
        return Account
    
    @accessor
    def role(self):
        owner = self.get_raw_attribute('owner')
        return 'owner' if owner else 'user'
    
    @accessor
    def is_demo_user(self):
        return self.email == 'johndoe@example.com'