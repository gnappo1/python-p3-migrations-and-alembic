"""Added student model

Revision ID: fb17b3098e2d
Revises: 1c474aea9b4a
Create Date: 2023-02-02 11:17:52.172976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb17b3098e2d'
down_revision = '1c474aea9b4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=55), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('enrolled_date', sa.DateTime(), nullable=True),
    sa.CheckConstraint('grade BETWEEN 1 AND 12', name='grade_between_1_and_12'),
    sa.PrimaryKeyConstraint('id', name='id_pk'),
    sa.UniqueConstraint('email', name='unique_email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###
