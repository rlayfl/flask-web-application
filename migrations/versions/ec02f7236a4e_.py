"""empty message

Revision ID: ec02f7236a4e
Revises: 
Create Date: 2024-03-20 16:23:11.055273

"""
from alembic import op
from datetime import datetime

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec02f7236a4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('module_enrolments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userAccountID', sa.Integer(), nullable=True),
    sa.Column('ModuleID', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('startDate', sa.DateTime(), nullable=True),
    sa.Column('endDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    
     # Get tables as objects to be worked with

    module_enrolments_table = sa.Table('module_enrolments', sa.MetaData(), autoload_with=op.get_bind())
    modules_table = sa.Table('modules', sa.MetaData(), autoload_with=op.get_bind())
    user_accounts_table = sa.Table('user_accounts', sa.MetaData(), autoload_with=op.get_bind())

    # Insert values into the database upon database upgrade

    op.bulk_insert(user_accounts_table, [
        {'name': 'Francisco Rendo'}
    ])

    op.bulk_insert(modules_table, [
        {'name': 'Website Development',
        'code': 'IY4103',
        'startDate': datetime.now(),
        'endDate': datetime.now()}
    ])

    op.bulk_insert(module_enrolments_table, [
        {'userAccountID': 1,
        'moduleID': 1}
    ])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_accounts')
    op.drop_table('modules')
    op.drop_table('module_enrolments')
    # ### end Alembic commands ###
