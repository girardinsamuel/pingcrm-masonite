"""Organization Model."""
from masoniteorm.relationships import has_many
from masoniteorm.models import Model
from masoniteorm.scopes import scope


class Organization(Model):
    """Organization Model."""

    @has_many("id", "organization_id")
    def contacts(self):
        from app.Contact import Contact

        return Contact

    @scope
    def order_by_name(self, query):
        return query.order_by("name")
