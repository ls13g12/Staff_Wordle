"""empty message

Revision ID: fb5b00e14320
Revises: 2134b5263d11
Create Date: 2022-02-14 10:43:58.666716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb5b00e14320'
down_revision = '2134b5263d11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('initials', sa.String(length=3), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_initials'), 'user', ['initials'], unique=True)
    op.create_index(op.f('ix_user_nickname'), 'user', ['nickname'], unique=False)
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_word_name'), 'word', ['name'], unique=True)
    op.create_table('user_word_link',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('guesses', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['word.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'word_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_word_link')
    op.drop_index(op.f('ix_word_name'), table_name='word')
    op.drop_table('word')
    op.drop_index(op.f('ix_user_nickname'), table_name='user')
    op.drop_index(op.f('ix_user_initials'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
