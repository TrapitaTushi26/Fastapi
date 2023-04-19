"""create posts table

Revision ID: acaa1941441f
Revises: 
Create Date: 2023-04-09 13:03:17.192076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acaa1941441f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id',sa.Integer(), 
                                       nullable=False, primary_key=True),
    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
