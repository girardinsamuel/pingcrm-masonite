from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """Run the migrations."""
        with self.schema.create('users') as table:
            table.increments('id')
            table.integer('account_id')
            table.string('first_name', 25)
            table.string('last_name', 25)
            table.string('email', 50).unique()
            table.string('password').nullable()
            table.boolean('owner').default(False)
            table.string('photo_path', 100).nullable()
            table.string('remember_token').nullable()
            table.timestamp('verified_at').nullable()
            table.timestamps()
            table.timestamp('deleted_at').nullable()
            table.index("account_id")

    def down(self):
        """Revert the migrations."""
        self.schema.drop('users')
