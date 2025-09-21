"""drop is_deleted column from users

Revision ID: 2046def341c7
Revises: 68c7a660c924
Create Date: 2025-09-09 10:14:21.990235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2046def341c7'
down_revision: Union[str, Sequence[str], None] = '68c7a660c924'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Supprime la colonne 'is_deleted' dans la table 'users'
    op.drop_column('users', 'is_deleted')


def downgrade() -> None:
    # Ajoute la colonne 'is_deleted' avec type Boolean, valeur par défaut False
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), nullable=True, server_default=sa.text('false')))

