"""Add a new column datetime

Revision ID: c21ff3d20511
Revises: 7eb43d939f27
Create Date: 2024-02-01 09:00:08.566272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c21ff3d20511'
down_revision = '7eb43d939f27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('join_date', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint("uq_username", ["username"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('join_date')

    # ### end Alembic commands ###