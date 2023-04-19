"""add foreign key to the posts table

Revision ID: 16963bce4729
Revises: 2fe9f55b847f
Create Date: 2023-04-09 16:00:30.960197

"""
# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision = '16963bce4729'
# down_revision = '2fe9f55b847f'
# branch_labels = None
# depends_on = None

# def upgrade():
#     op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
#     op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
#                           'owner_id'], remote_cols=['id'], ondelete="CASCADE")
#     pass

# def downgrade():
#     op.drop_constraint('post_users_fk', table_name="posts")
#     op.drop_column('posts', 'owner_id')
#     pass

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16963bce4729'
down_revision = '2fe9f55b847f'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
