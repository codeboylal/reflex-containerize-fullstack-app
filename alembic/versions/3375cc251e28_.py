"""empty message

Revision ID: 3375cc251e28
Revises: 277cad49d2b0
Create Date: 2024-10-20 21:36:07.342913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '3375cc251e28'
down_revision: Union[str, None] = '277cad49d2b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('remarks', sqlmodel.sql.sqltypes.AutoString(), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_column('remarks')

    # ### end Alembic commands ###
