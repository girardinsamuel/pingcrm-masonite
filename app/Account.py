"""Account Model."""
from orator.orm import has_many

from config.database import Model


class Account(Model):
    """Account Model."""
    __fillable__ = ["name"]
    
    @has_many
    def users(self):
        from app.User import User
        return User
    
    @has_many
    def organizations(self):
        from app.Organization import Organization
        return Organization
    
    @has_many
    def contacts(self):
        from app.Contact import Contact
        return Contact