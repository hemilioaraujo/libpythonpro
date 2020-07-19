from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Hemilio', email='hemilioaraujo@gmail.com'),
            Usuario(nome='Ximbinha', email='hemilioaraujo@gmail.com')
        ],
        [
            Usuario(nome='Hemilio', email='hemilioaraujo@gmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'hemilioaraujo@gmail.com',
        'enviando spam',
        'este email é o teste de envio de spam!'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Hemilio', email='hemilioaraujo@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ximbinha@gmail.com',
        'enviando spam',
        'este email é o teste de envio de spam!'
    )
    enviador.enviar.assert_called_once_with(
        'ximbinha@gmail.com',
        'hemilioaraujo@gmail.com',
        'enviando spam',
        'este email é o teste de envio de spam!'
    )
