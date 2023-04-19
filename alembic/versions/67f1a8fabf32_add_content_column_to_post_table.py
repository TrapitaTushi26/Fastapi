"""add content column to post table

Revision ID: 67f1a8fabf32
Revises: acaa1941441f
Create Date: 2023-04-09 13:34:05.969162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f1a8fabf32'
down_revision = 'acaa1941441f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass

    

def downgrade():
    op.drop_column('posts','content')
    
    pass
