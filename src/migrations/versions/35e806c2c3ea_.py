"""empty message

Revision ID: 35e806c2c3ea
Revises: b33b6a1c859f
Create Date: 2025-04-07 18:55:53.511564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35e806c2c3ea'
down_revision = 'b33b6a1c859f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypto_currency', schema=None) as batch_op:
        batch_op.add_column(sa.Column('coing_gecko_currency_id', sa.Text(), nullable=False))
        batch_op.create_foreign_key(None, 'coing_gecko_currency', ['coing_gecko_currency_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypto_currency', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('coing_gecko_currency_id')

    # ### end Alembic commands ###
