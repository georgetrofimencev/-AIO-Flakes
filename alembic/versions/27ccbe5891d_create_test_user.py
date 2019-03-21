"""Create Test User

Revision ID: 27ccbe5891d
Revises: 45cd7dee0ca
Create Date: 2019-03-21 15:26:18.632370

"""

# revision identifiers, used by Alembic.
revision = '27ccbe5891d'
down_revision = '45cd7dee0ca'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sources', sa.JSON(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sources')
    ### end Alembic commands ###
