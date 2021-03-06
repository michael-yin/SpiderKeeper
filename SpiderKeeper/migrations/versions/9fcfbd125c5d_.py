"""empty message

Revision ID: 9fcfbd125c5d
Revises: 
Create Date: 2018-06-05 10:50:46.446820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fcfbd125c5d'
down_revision = None
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
    op.drop_table('DetailItem')
    op.drop_table('QAItem')
    op.drop_table('ReviewItem')
    op.drop_table('MiniItem')
    # ### end Alembic commands ###


def downgrade_data():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('MiniItem',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"MiniItem_id_seq"\'::regclass)'), nullable=False),
    sa.Column('itemid', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('sku', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('price', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('originalprice', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('country', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='MiniItem_pkey'),
    sa.UniqueConstraint('itemid', name='MiniItem_itemid_key')
    )
    op.create_table('ReviewItem',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"ReviewItem_id_seq"\'::regclass)'), nullable=False),
    sa.Column('itemid', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('review_title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('review_date', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('reviewer', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('review_text', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('upvode', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='ReviewItem_pkey'),
    sa.UniqueConstraint('itemid', name='ReviewItem_itemid_key')
    )
    op.create_table('QAItem',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"QAItem_id_seq"\'::regclass)'), nullable=False),
    sa.Column('itemid', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('question', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('question_date', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('question_author', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_author', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_date', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='QAItem_pkey'),
    sa.UniqueConstraint('itemid', name='QAItem_itemid_key')
    )
    op.create_table('DetailItem',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"DetailItem_id_seq"\'::regclass)'), nullable=False),
    sa.Column('itemid', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('quote', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('sku', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('rating_count', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('warranty', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seller_name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('question_count', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('positive_rating', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('json_data', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seller_data', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='DetailItem_pkey'),
    sa.UniqueConstraint('itemid', name='DetailItem_itemid_key')
    )
    # ### end Alembic commands ###

