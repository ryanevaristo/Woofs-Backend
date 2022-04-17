"""add app

Revision ID: 808ab481f595
Revises: 
Create Date: 2022-04-16 22:20:03.333002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '808ab481f595'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Localidade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('longitude', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('latitude', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('limiteDistanciaMatch', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Localidade_id'), 'Localidade', ['id'], unique=False)
    op.create_table('Usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=55), nullable=False),
    sa.Column('senha', sa.String(length=50), nullable=False),
    sa.Column('idade', sa.String(length=2), nullable=False),
    sa.Column('id_localidade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_localidade'], ['Localidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Usuario_id'), 'Usuario', ['id'], unique=False)
    op.create_table('Animal',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('sexo', sa.String(length=1), nullable=False),
    sa.Column('raca', sa.String(length=30), nullable=False),
    sa.Column('idade', sa.String(length=2), nullable=False),
    sa.Column('vacinacao', sa.String(length=200), nullable=True),
    sa.Column('validacao_vacina', sa.Boolean(), nullable=True),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usuario'], ['Usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Animal_id'), 'Animal', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Animal_id'), table_name='Animal')
    op.drop_table('Animal')
    op.drop_index(op.f('ix_Usuario_id'), table_name='Usuario')
    op.drop_table('Usuario')
    op.drop_index(op.f('ix_Localidade_id'), table_name='Localidade')
    op.drop_table('Localidade')
    # ### end Alembic commands ###