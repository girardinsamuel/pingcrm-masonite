"""Contact Model."""
from masoniteorm.relationships import belongs_to
from masoniteorm.models import Model
from masoniteorm.scopes import scope, SoftDeletesMixin


class Contact(Model, SoftDeletesMixin):
    """Contact Model."""

    __appends__ = ["name"]

    def __str__(self):
        return self.name

    @belongs_to("organization_id", "id")
    def organization(self):
        from app.Organization import Organization

        return Organization

    @property
    def name(self):
        return self.last_name + " " + self.first_name

    @scope
    def order_by_name(self, query):
        return query.order_by("last_name").order_by("first_name")

    @scope
    def filter(self, query, filters):
        if filters.get("search", None):
            search_token = f"%{filters['search']}%"
            query.where("first_name", "like", search_token).or_where(
                "last_name", "like", search_token
            ).or_where("email", "like", search_token)

        if filters.get("trashed", None):
            if filters["trashed"] == "with":
                query.with_trashed()
            else:
                query.only_trashed()

        return query