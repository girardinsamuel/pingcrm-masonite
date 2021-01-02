"""User Model."""
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import scope, SoftDeletesMixin
from masoniteorm.models import Model


class User(Model, SoftDeletesMixin):
    """User Model."""

    __fillable__ = [
        "first_name",
        "last_name",
        "email",
        "password",
        "photo_path",
        "owner",
        "account_id",
    ]
    __appends__ = ["role", "name"]
    __auth__ = "email"

    def __str__(self):
        return self.name

    @belongs_to('account_id', 'id')
    def account(self):
        from app.Account import Account
        return Account

    @property
    def role(self):
        return "owner" if self.owner else "user"

    @property
    def name(self):
        return self.last_name + ' ' + self.first_name

    @property
    def is_demo_user(self):
        return self.email == "johndoe@example.com"

    @scope
    def order_by_name(self, query):
        return query.order_by("last_name").order_by("first_name")

    @scope
    def where_role(self, query, role):
        if role == "owner":
            return query.where("owner", True)
        else:
            return query.where("owner", False)

    @scope
    def filter(self, query, filters):
        if filters.get("search", None):
            search_token = f"%{filters['search']}%"
            query.where("first_name", "like", search_token).or_where(
                "last_name", "like", search_token
            ).or_where("email", "like", search_token)

        if filters.get("role", None):
            query.where_role(filters["role"])

        if filters.get("trashed", None):
            if filters["trashed"] == "with":
                query.with_trashed()
            else:
                # only trashed, ie User with a not null deleted date
                query.where("deleted_at", None)

        return query
