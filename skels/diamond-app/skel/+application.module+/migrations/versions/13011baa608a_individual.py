"""empty message

Revision ID: 13011baa608a
Revises: 20f04b9598da
Create Date: 2015-02-05 18:15:17.866888

"""

# revision identifiers, used by Alembic.
revision = '13011baa608a'
down_revision = '20f04b9598da'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('individual',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('friend_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['friend_id'], ['individual.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('individual')
    ### end Alembic commands ###