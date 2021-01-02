from masoniteorm.migrations import Migration


class CreateOrganizationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('organizations') as table:
            table.increments('id')
            table.integer('account_id')
            table.index('account_id')
            table.string('name', 100)
            table.string('email', 50).nullable()
            table.string('phone', 50).nullable()
            table.string('address', 150).nullable()
            table.string('city', 50).nullable()
            table.string('region', 50).nullable()
            table.string('country', 2).nullable()
            table.string('postal_code', 25).nullable()
            table.timestamps()
            table.datetime('deleted_at').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('organizations')
