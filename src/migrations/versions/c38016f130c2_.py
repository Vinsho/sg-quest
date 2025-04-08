"""empty message

Revision ID: c38016f130c2
Revises: 35e806c2c3ea
Create Date: 2025-04-07 23:19:58.169450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c38016f130c2'
down_revision = '35e806c2c3ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypto_currency', schema=None) as batch_op:
        batch_op.add_column(sa.Column('coin_gecko_currency_id', sa.Text(), nullable=False))
        batch_op.drop_constraint('crypto_currency_coing_gecko_currency_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'coing_gecko_currency', ['coin_gecko_currency_id'], ['id'])
        batch_op.drop_column('coing_gecko_currency_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypto_currency', schema=None) as batch_op:
        batch_op.add_column(sa.Column('coing_gecko_currency_id', sa.TEXT(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('crypto_currency_coing_gecko_currency_id_fkey', 'coing_gecko_currency', ['coing_gecko_currency_id'], ['id'])
        batch_op.drop_column('coin_gecko_currency_id')

    # ### end Alembic commands ###
