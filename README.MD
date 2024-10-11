# DATABASE

We use [alembic](https://alembic.sqlalchemy.org/) as a tool for migrate database.


## Create migration
To create migration please use:

```
$ alembic revision -m "create first migration"
```

## Run migrations in test

```
$ alembic upgrade head
```
or use the script:

```
$  python scripts/migrations.py upgrade test
```
