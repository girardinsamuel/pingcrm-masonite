"""Contact Model."""
from masoniteorm.relationships import belongs_to
from masoniteorm.models import Model


class Contact(Model):
    """Contact Model."""

    @belongs_to
    def organization(self):
        from app.Organization import Organization

        return Organization