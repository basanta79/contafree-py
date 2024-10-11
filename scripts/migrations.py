import os
import sys
from alembic import command
from alembic.config import Config

def parameters():
    if len(sys.argv) <= 1:
        print_help()
        return

    action = sys.argv[1]
    ACTIONS[action]()


def print_help():
    print("usage: python3 migrations.py [action] [prod|test]")
    print("""
    actions:
        help: prints this menu
        upgrade: upgrade database
    """)


def upgrade():
    if len(sys.argv) <= 2 :
        print_help()
        return

    env = sys.argv[2]
    config_dir = os.path.abspath(os.path.join(os.curdir,'mgibert_conta_py', 'alembic.ini'))
    alembic_cfg = Config(config_dir)

    script_location = os.path.join(os.curdir,'mgibert_conta_py', 'alembic')
    alembic_cfg.set_main_option("script_location", script_location)

    database_url = DATABASE_URL[env]
    print(database_url)
    alembic_cfg.set_main_option("sqlalchemy.url", database_url)

    command.upgrade(alembic_cfg, "head")

def downgrade():
    if len(sys.argv) <= 2 :
        print_help()
        return

    env = sys.argv[2]
    config_dir = os.path.abspath(os.path.join(os.curdir, 'mgibert_conta_py', 'alembic.ini'))
    alembic_cfg = Config(config_dir)

    script_location = os.path.join(os.curdir, 'mgibert_conta_py', 'alembic')
    alembic_cfg.set_main_option("script_location", script_location)

    database_url = DATABASE_URL[env]
    print(database_url)
    alembic_cfg.set_main_option("sqlalchemy.url", database_url)

    command.downgrade(alembic_cfg, "-1")


if __name__ == "__main__":
    ACTIONS = {
        'help': print_help,
        'upgrade': upgrade,
        'downgrade': downgrade
    }
    DATABASE_URL = {
        'prod': 'postgresql://pablo:example@localhost:5433/treasury',
        'test': 'postgresql://pablo:example@localhost:5433/treasury_test'
    }
    parameters()
