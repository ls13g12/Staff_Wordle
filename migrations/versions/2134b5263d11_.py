"""empty message

Revision ID: 2134b5263d11
Revises: 8e059f1c1596
Create Date: 2022-02-09 22:08:15.566487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2134b5263d11'
down_revision = '8e059f1c1596'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_word_link', sa.Column('date', sa.DateTime(), nullable=True))
    op.drop_column('user_word_link', 'datetime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_word_link', sa.Column('datetime', sa.DATETIME(), nullable=True))
    op.drop_column('user_word_link', 'date')
    # ### end Alembic commands ###
