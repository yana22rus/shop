"""empty message

Revision ID: 7c197b6ae050
Revises: 
Create Date: 2023-02-27 02:17:21.051827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c197b6ae050'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('subtitle', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('guarantee', sa.String(length=500), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('brand', sa.String(length=255), nullable=False),
    sa.Column('color', sa.String(length=255), nullable=False),
    sa.Column('number_stock', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goods')
    op.drop_table('category')
    # ### end Alembic commands ###