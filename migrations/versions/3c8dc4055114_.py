"""empty message

Revision ID: 3c8dc4055114
Revises: 45fe3474236c
Create Date: 2018-12-24 01:22:16.337998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c8dc4055114'
down_revision = '45fe3474236c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###
