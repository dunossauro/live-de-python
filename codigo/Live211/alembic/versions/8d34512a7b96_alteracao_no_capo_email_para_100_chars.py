"""alteracao no capo email para 100 chars

Revision ID: 8d34512a7b96
Revises: b723047f6d98
Create Date: 2022-07-18 23:28:18.249992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d34512a7b96'
down_revision = 'b723047f6d98'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.alter_column(
            'email',
            existing_type=sa.VARCHAR(length=50),
            type_=sa.String(length=100),
            existing_nullable=False
        )


def downgrade() -> None:
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.alter_column(
            'email',
            existing_type=sa.String(length=100),
            type_=sa.VARCHAR(length=50),
            existing_nullable=False
        )
