"""Contact Model."""
from orator.orm import belongs_to

from config.database import Model


class Contact(Model):
    """Contact Model."""
    
    @belongs_to
    def organization(self):
        from app.Organization import Organization
        return Organization