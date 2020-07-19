class Enviador:

    def enviar(self, remetente, destinatario, assunto, conteudo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email: {remetente} é inválido!')
        return remetente


class EmailInvalido(Exception):
    pass
