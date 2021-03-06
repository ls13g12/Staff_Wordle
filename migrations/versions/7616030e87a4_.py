"""empty message

Revision ID: 7616030e87a4
Revises: fb5b00e14320
Create Date: 2022-02-17 15:17:45.964873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7616030e87a4'
down_revision = 'fb5b00e14320'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('word_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('word', sa.Column('word_log_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'word', 'word_log', ['word_log_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'word', type_='foreignkey')
    op.drop_column('word', 'word_log_id')
    op.drop_table('word_log')
    # ### end Alembic commands ###
