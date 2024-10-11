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
        CREATE TABLE IF NOT EXISTS balance_accounts
        (
            account_id uuid NOT NULL PRIMARY KEY,
            account_type VARCHAR(256) NOT NULL,
            account_name VARCHAR(256) NOT NULL,
            description VARCHAR(256) NOT NULL,
            available_balance BIGINT NOT NULL,
            hold_balance BIGINT NOT NULL,
            currency VARCHAR(5) NOT NULL
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS ledger
        (
            ledger_id uuid NOT NULL PRIMARY KEY,
            operation_date TIMESTAMP NOT NULL,
            account_id uuid NOT NULL,
            description TEXT NOT NULL,
            debit BIGINT NOT NULL,
            credit BIGINT NOT NULL,
            CONSTRAINT fk_ledger_account
                    FOREIGN KEY (account_id) REFERENCES balance_accounts(account_id)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS vendor
        (
            vendor_id uuid NOT NULL PRIMARY KEY,
            name VARCHAR(256) NOT NULL
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS payments
        (
            payment_id uuid NOT NULL PRIMARY KEY,
            payment_date TIMESTAMP NOT NULL,
            amount BIGINT NOT NULL,
            currency VARCHAR(5) NOT NULL,
            description VARCHAR(256) NOT NULL,
            vendor_id uuid NOT NULL,
            CONSTRAINT fk_payments_vendor
                    FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS account_operations
        (
            operation_id uuid NOT NULL PRIMARY KEY,
            payment_id uuid NOT NULL,
            operation_date TIMESTAMP NOT NULL,
            description VARCHAR(256) NOT NULL,
            amount BIGINT NOT NULL,
            operation_type VARCHAR(256) NOT NULL,
            CONSTRAINT fk_account_operations_payment
                    FOREIGN KEY (payment_id) REFERENCES payments(payment_id)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS operations_ledger
        (
            operation_id uuid NOT NULL,
            ledger_id uuid NOT NULL,
            PRIMARY KEY (operation_id, ledger_id),
            CONSTRAINT fk_operations_ledger_operation
                    FOREIGN KEY (operation_id) REFERENCES account_operations(operation_id)
                    ON DELETE CASCADE, -- Ensures that deleting an operation also removes its association in the join table
                CONSTRAINT fk_operations_ledger_ledger
                    FOREIGN KEY (ledger_id) REFERENCES ledger(ledger_id)
                    ON DELETE CASCADE -- Ensures that deleting a ledger also removes its association in the join table
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS periods
        (
            period_id uuid NOT NULL PRIMARY KEY,
            period TEXT NOT NULL
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS projects
        (
            project_id uuid NOT NULL PRIMARY KEY,
            project_key TEXT NOT NULL,
            description TEXT NOT NULL,
            period uuid NOT NULL,
            CONSTRAINT fk_projects_period
                    FOREIGN KEY (period) REFERENCES periods(period_id)
        );
    """)


def downgrade() -> None:
    op.drop_table('balance_accounts')
    op.drop_table('ledger')
    op.drop_table('vendor')
    op.drop_table('payments')
    op.drop_table('account_operations')
    op.drop_table('operations_ledger')
    op.drop_table('periods')
    op.drop_table('projects')
