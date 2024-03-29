"""empty message

Revision ID: 0c473a5a3874
Revises: 1acf5018d179
Create Date: 2019-09-16 20:22:39.512414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c473a5a3874'
down_revision = '1acf5018d179'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usernames', sa.String(length=64), nullable=True),
    sa.Column('content', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_content'), 'content', ['content'], unique=False)
    op.create_index(op.f('ix_content_usernames'), 'content', ['usernames'], unique=False)
    op.drop_index('ix_contents_content', table_name='contents')
    op.drop_index('ix_contents_username', table_name='contents')
    op.drop_table('contents')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contents',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('content', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='contents_pkey')
    )
    op.create_index('ix_contents_username', 'contents', ['username'], unique=False)
    op.create_index('ix_contents_content', 'contents', ['content'], unique=False)
    op.drop_index(op.f('ix_content_usernames'), table_name='content')
    op.drop_index(op.f('ix_content_content'), table_name='content')
    op.drop_table('content')
    # ### end Alembic commands ###
