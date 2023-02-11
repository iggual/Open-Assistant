"""added worker db entry

Revision ID: 569cd595bb10
Revises: 3a4cd8777eb2
Create Date: 2023-02-11 01:47:34.880485

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "569cd595bb10"
down_revision = "3a4cd8777eb2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "worker",
        sa.Column("id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("api_key", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_worker_api_key"), "worker", ["api_key"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_worker_api_key"), table_name="worker")
    op.drop_table("worker")
    # ### end Alembic commands ###