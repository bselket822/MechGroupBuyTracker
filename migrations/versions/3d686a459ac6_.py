"""empty message

Revision ID: 3d686a459ac6
Revises: 3c867b5f6dd5
Create Date: 2022-03-11 23:35:54.466689

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3d686a459ac6'
down_revision = '3c867b5f6dd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'baseprice',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=8),
               existing_nullable=True)
    op.alter_column('project', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=True)
    op.alter_column('project', 'started_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.Date(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'started_at',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=True)
    op.alter_column('project', 'updated_at',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('project', 'baseprice',
               existing_type=sa.Float(precision=8),
               type_=sa.REAL(),
               existing_nullable=True)
    # ### end Alembic commands ###