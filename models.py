class Solicita:
    def __init__(self, tipo, descricao, data_solicitacao, id=None):
        self.id = id
        self.tipo=tipo
        self.descricao=descricao
        self.data_solicitacao=data_solicitacao


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha=senha
