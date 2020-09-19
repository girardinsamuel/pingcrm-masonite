"""Organization Model."""
from orator.orm import has_many

from config.database import Model


class Organization(Model):
    """Organization Model."""
    
    @has_many
    def contacts(self):
        from app.Contact import Contact
        return Contact