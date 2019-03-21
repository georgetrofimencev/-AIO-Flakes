"""Create Test User

Revision ID: 4e6ec61d9cb
Revises: 
Create Date: 2019-03-20 22:51:34.391277

"""

# revision identifiers, used by Alembic.
revision = '4e6ec61d9cb'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('telegram_account', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_nickname'), 'users', ['nickname'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_nickname'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###