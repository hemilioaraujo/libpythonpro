from unittest.mock import Mock
import pytest
from libpythonpro import github_api


@pytest.fixture()
def avatar_url():
    """
    Este teste utiliza o Mock para "Simular o acesso a API",
    é criado uma instância de Mock com os métodos e retornos desejados
    para o módulo github_api.
    :return: url
    """
    # CRIANDO UM MOCK
    resp_mock = Mock()
    # ATRIBUINDO O MÉTODO JSON AO MOCK E DEFININDO O QUE ELE RETORNA
    url = "https://avatars0.githubusercontent.com/u/28680369?v=4"
    resp_mock.json.return_value = {
        "login": "hemilioaraujo",
        "id": 28680369,
        "avatar_url": url,
    }
    get_original = github_api.requests.get
    # ALTERANDO O MÉTODO GITHUB_API.REQUESTS.GET PARA RETORNAR OS DADOS DO MOCK
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    # RETORNANDO O MÉTODO GET PARA O ORIGINAL
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('hemilioaraujo')
    assert url == avatar_url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('hemilioaraujo')
    assert url == "https://avatars0.githubusercontent.com/u/28680369?v=4"
