"""
CONFTEST

É nomeado por convenção no pytest.
Serve para disponibilizar as fixtures para os escopos desejados.
"""
import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='module')
# FIXTURE EVITA REPETIÇÃO DE CÓDIGO
# SCOPE DEFINE A FORMA QUE A FIXTURE SERÁ UTILIZADA
def conexao():
    # SETUP
    conexao_obj = Conexao()
    yield conexao_obj
    # TEAR DOWN
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # SETUP
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # TEAR DOWN
    sessao_obj.rollback()
    sessao_obj.fechar()
