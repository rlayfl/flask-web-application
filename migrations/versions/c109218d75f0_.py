"""empty message

Revision ID: c109218d75f0
Revises: 
Create Date: 2024-03-20 13:52:47.098692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c109218d75f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # Get the Table objects for channels and users
    channels_table = sa.Table('channels', sa.MetaData(), autoload_with=op.get_bind())
    users_table = sa.Table('users', sa.MetaData(), autoload_with=op.get_bind())

    # Add new channel
    op.bulk_insert(channels_table, [
        {'name': 'New Channel'}
    ])
    # Add new user
    op.bulk_insert(users_table, [
        {'name': 'New User'}
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('channels')
    # ### end Alembic commands ###
