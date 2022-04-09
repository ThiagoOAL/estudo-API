from models import Solicita, Usuario

SQL_DELETA_JOGO = 'delete from jogo where id = %s'
SQL_JOGO_POR_ID = 'SELECT id, nome, categoria, console from jogo where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_SOLICITACAO = 'UPDATE solicitacao SET tipo=%s, descricao=%s, data_solicitacao=%s where id = %s'
SQL_BUSCA_SOLICITACAO = 'SELECT id_solicitacao, categoria_solicitacao, descricao_solicitacao, data_abertura FROM solicitacoes INNER JOIN categoria_solicitacoes ON solicitacoes.fk_categoria_solicitacao = categoria_solicitacoes.id_categoria_solicitacao'
# SQL_CRIA_SOLICITACAO = 'INSERT into solicitacao (tipo, descricao, data_solicitacao) values (%s, %s, %s)'
SQL_CRIA_SOLICITACAO = 'INSERT into solicitacoes (fk_categoria_solicitacao, descricao_solicitacao, data_abertura) values (%s, %s, %s)'

SQL_TESTE = 'SELECT id, tipo, descricao, data_solicitacao FROM  solicitacao'
#SQL_BUSCA_CATEGORIA = 'SELECT id_categoria_solicitacao, categoria_solicitacao from categoria_solicitacoes'

class SolicitaDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, solicitacao):
        cursor = self.__db.connection.cursor()

        if (solicitacao.id):
            cursor.execute(SQL_ATUALIZA_SOLICITACAO, (solicitacao.tipo, solicitacao.descricao, solicitacao.data_solicitacao, solicitacao.id))
        else:
            cursor.execute(SQL_CRIA_SOLICITACAO, (solicitacao.fk_categoria_solicitacao, solicitacao.descricao_solicitacao, solicitacao.data_abertura))
            solicitacao.id = cursor.lastrowid
        self.__db.connection.commit()
        return solicitacao

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SOLICITACAO)
        # solicitacoes = (cursor.fetchall())
        # print(solicitacoes[0])
        solicitacoes = traduz_solicitacoes(cursor.fetchall())
        return solicitacoes



    # def lista_categ(self):
    #     cursor = self.__db.connection.cursor()
    #     cursor.execute(SQL_BUSCA_CATEGORIA)
    #     solicitacoes = traduz_solicitacoes_categ(cursor.fetchall())
    #     return solicitacoes

#     def busca_por_id(self, id):
#         cursor = self.__db.connection.cursor()
#         cursor.execute(SQL_JOGO_POR_ID, (id,))
#         tupla = cursor.fetchone()
#         return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

#     def deletar(self, id):
#         self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id, ))
#         self.__db.connection.commit()


# class UsuarioDao:
#     def __init__(self, db):
#         self.__db = db

#     def buscar_por_id(self, id):
#         cursor = self.__db.connection.cursor()
#         cursor.execute(SQL_USUARIO_POR_ID, (id,))
#         dados = cursor.fetchone()
#         usuario = traduz_usuario(dados) if dados else None
#         return usuario


def traduz_solicitacoes(solicitacoes):
    def cria_solicitacao_com_tupla(tupla):
        return Solicita(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_solicitacao_com_tupla, solicitacoes))

# def traduz_solicitacoes_categ(solicitacoes):
#     def cria_solicitacao_com_tupla(tupla):
#         return Categoria(tupla[1],id_categoria_solicitacao=tupla[0])
#     return list(map(cria_solicitacao_com_tupla, solicitacoes))

# def traduz_usuario(tupla):
#     return Usuario(tupla[0], tupla[1], tupla[2])
