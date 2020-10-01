"""Organization Model."""
from masoniteorm.relationships import has_many
from masoniteorm.models import Model


class Organization(Model):
    """Organization Model."""

    @has_many
    def contacts(self):
        from app.Contact import Contact

        return Contact