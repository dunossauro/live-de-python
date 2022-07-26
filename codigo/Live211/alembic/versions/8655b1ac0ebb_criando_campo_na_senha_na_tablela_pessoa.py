"""Criando campo na senha na tablela pessoa

Revision ID: 8655b1ac0ebb
Revises: eb9562d19265
Create Date: 2022-07-18 23:06:32.450697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8655b1ac0ebb'
down_revision = 'eb9562d19265'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'pessoa',
        sa.Column('senha', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    op.drop_column(
        'pessoa', 'senha'
    )
