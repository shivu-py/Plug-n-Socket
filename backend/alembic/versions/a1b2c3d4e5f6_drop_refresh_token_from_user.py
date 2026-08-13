"""drop refresh_token from user

Revision ID: a1b2c3d4e5f6
Revises: 0e2997e6e091
Create Date: 2026-08-12 23:40:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


revision: str = "a1b2c3d4e5f6"
down_revision: Union[str, Sequence[str], None] = "0e2997e6e091"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("user", "refresh_token")


def downgrade() -> None:
    op.add_column(
        "user",
        sa.Column("refresh_token", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    )
