"""empty message

Revision ID: 3d999ba5655d
Revises: 7affc592074b
Create Date: 2022-10-08 12:42:03.610242

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3d999ba5655d"
down_revision = "7affc592074b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("items", sa.Column("description", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("items", "description")
    # ### end Alembic commands ###
