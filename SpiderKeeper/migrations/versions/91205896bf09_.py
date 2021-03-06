"""empty message

Revision ID: 91205896bf09
Revises: 6f7fab31143b
Create Date: 2018-06-06 09:43:09.467415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91205896bf09'
down_revision = '6f7fab31143b'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_data():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('detailitem', sa.Column('unique_id', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'detailitem', ['unique_id'])
    op.add_column('miniitem', sa.Column('unique_id', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'miniitem', ['unique_id'])
    op.add_column('qaitem', sa.Column('unique_id', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'qaitem', ['unique_id'])
    op.add_column('reviewitem', sa.Column('unique_id', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'reviewitem', ['unique_id'])
    # ### end Alembic commands ###


def downgrade_data():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviewitem', type_='unique')
    op.drop_column('reviewitem', 'unique_id')
    op.drop_constraint(None, 'qaitem', type_='unique')
    op.drop_column('qaitem', 'unique_id')
    op.drop_constraint(None, 'miniitem', type_='unique')
    op.drop_column('miniitem', 'unique_id')
    op.drop_constraint(None, 'detailitem', type_='unique')
    op.drop_column('detailitem', 'unique_id')
    # ### end Alembic commands ###

