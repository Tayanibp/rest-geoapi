"""Create database

Revision ID: 37f94f03aafc
Revises: 
Create Date: 2023-03-09 23:37:56.762857

"""
import geoalchemy2
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37f94f03aafc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('edificacao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4674, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )


def downgrade() -> None:
    op.drop_table('edificacao', schema='public')
