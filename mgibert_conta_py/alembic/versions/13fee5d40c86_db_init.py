"""db_init

Revision ID: 13fee5d40c86
Revises: 
Create Date: 2024-09-28 07:52:32.099970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13fee5d40c86'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.execute("""
    CREATE TABLE IF NOT EXISTS test(account_id uuid NOT NULL PRIMARY KEY,account_type VARCHAR(256) NOT NULL,account_name VARCHAR(256) NOT NULL,description VARCHAR(256) NOT NULL,available_balance BIGINT NOT NULL,hold_balance BIGINT NOT NULL,currency VARCHAR(5) NOT NULL);
    """)


def downgrade() -> None:
    op.drop_table('test')
