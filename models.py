from msilib.schema import Class


class Solicita():
    def __init__(self, fk_categoria_solicitacao, descricao_solicitacao, data_abertura, id=None):
        self.id = id
        self.fk_categoria_solicitacao = fk_categoria_solicitacao
        self.descricao_solicitacao=descricao_solicitacao
        self.data_abertura=data_abertura


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha=senha


# class Categoria:
#     def __init__(self, categoria_solicitacao, id_categoria_solicitacao):
#         self.id_categoria_solicitacao = id_categoria_solicitacao 
#         self.categoria_solicitacao=categoria_solicitacao