"""Account Model."""
from masoniteorm.relationships import has_many
from masoniteorm.models import Model
from masoniteorm.scopes import scope


class Account(Model):
    """Account Model."""

    __fillable__ = ["name"]

    @has_many('id', 'account_id')
    def users(self):
        from app.User import User

        return User

    @has_many('id', 'account_id')
    def organizations(self):
        from app.Organization import Organization

        return Organization

    @has_many
    def contacts(self):
        from app.Contact import Contact

        return Contact

    @scope
    def users_of_account(self, query, account_id):
        return query.where("id", account_id)
