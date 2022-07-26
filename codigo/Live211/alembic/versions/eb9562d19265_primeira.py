"""primeira

Revision ID: eb9562d19265
Revises: 
Create Date: 2022-07-18 22:36:28.019202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb9562d19265'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('pessoa')
