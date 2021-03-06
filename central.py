from flask import Flask, render_template, request, redirect, session, flash, url_for


class Solicita:
    def __init__(self, tipo, descricao, data):
        self.tipo=tipo
        self.descricao=descricao
        self.data=data


solicitacao1 = Solicita('Solução em Hardware', 'meu monitor não liga', '19/03/2022')
solicitacao2 = Solicita('Solução em software', 'o app do Java não ta rodando', '21/03/2022')
listando = [solicitacao1, solicitacao2]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha=senha

usuario1 = Usuario('Thiago Leite', 'TL', 'fatec')
usuario2 = Usuario('Mateus Augusto', 'MA', 'fatec1')
usuario3 = Usuario('Pedro Corrá', 'PC', 'fatec2')

usuarios = {usuario1.nickname: usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3
}




app = Flask(__name__)
app.secret_key = 'whatscode'


@app.route('/')
def index():

    lista = ['Solução em Hardware', 'Solução em Software','esclarecimentos/informações']
    return render_template('lista.html', titulo='Service Desk', serviços=lista)

@app.route('/solicitacoes')
def solicitando():

    return render_template('solicitacoes.html', titulo='Minhas solicitações', demanda=listando)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Solicitação de serviço')

@app.route('/criar', methods=['POST',])
def criar():
    tipo = request.form['Tipo de serviço']
    descricao = request.form['descrição do problema']
    data = request.form['Data']
    solicitacao = Solicita(tipo, descricao, data)
    listando.append(solicitacao)

    return redirect(url_for('solicitando'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autentica():

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        
        else:
            flash('Senha incorreta. Tente novamente!')
            return redirect(url_for('login'))
    
    flash('Usuário incorreto ou não cadastrado. Por gentileza, se cadastre.!')
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('index'))

app.run(debug=True)