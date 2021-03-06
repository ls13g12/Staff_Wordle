"""empty message

Revision ID: 50708356d276
Revises: b36be76a33cd
Create Date: 2022-02-07 20:40:27.898843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50708356d276'
down_revision = 'b36be76a33cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_word_link',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('guesses', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['word.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'word_id')
    )
    op.drop_table('user_word')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_word',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('word_id', sa.INTEGER(), nullable=False),
    sa.Column('datetime', sa.DATETIME(), nullable=True),
    sa.Column('guesses', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['word.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'word_id')
    )
    op.drop_table('user_word_link')
    # ### end Alembic commands ###
