"""empty message

Revision ID: de4327a42cb7
Revises: 5c67c6b060df
Create Date: 2023-05-01 20:14:18.302623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de4327a42cb7'
down_revision = '5c67c6b060df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interface',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('connection', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('config', sa.JSON(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('infra_type', sa.String(length=50), nullable=True),
    sa.Column('port_channel_id', sa.Integer(), nullable=True),
    sa.Column('max_frame_size', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['port_channel_id'], ['interface.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interface')
    # ### end Alembic commands ###
