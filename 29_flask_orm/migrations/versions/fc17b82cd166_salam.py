"""salam

Revision ID: fc17b82cd166
Revises: f9a7d6bfd27c
Create Date: 2024-08-19 20:34:33.146135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc17b82cd166'
down_revision = 'f9a7d6bfd27c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.add_column(sa.Column('new_field', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.drop_column('new_field')

    # ### end Alembic commands ###
