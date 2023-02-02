"""Renaming birthday to birthday_datetime in students

Revision ID: 80d9b707312e
Revises: fb17b3098e2d
Create Date: 2023-02-02 12:48:53.732916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80d9b707312e'
down_revision = 'fb17b3098e2d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'birthday', new_column_name = 'birthday_datetime')


def downgrade() -> None:
    op.alter_column('students', 'birthday_datetime', new_column_name =  'birthday')
