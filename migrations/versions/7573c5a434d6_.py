"""empty message

Revision ID: 7573c5a434d6
Revises: 
Create Date: 2023-01-03 14:10:22.648857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7573c5a434d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postal_code', sa.String(length=5), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('register_at', sa.DateTime(), nullable=True),
    sa.Column('videos_checked_out_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rental',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.Column('total_inventory', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video')
    op.drop_table('rental')
    op.drop_table('customer')
    # ### end Alembic commands ###
