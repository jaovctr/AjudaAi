from flask import *
from aplicacao import aplicacao

def login_usuario(url_seguinte):
    return redirect(url_for('login', proxima_pagina=url_for(url_seguinte)))


@aplicacao.route('/')
def index():
    return render_template('index.html')


@aplicacao.route('/nova_demanda')
def nova_demanda():
#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
#         return login_usuario('nova_demanda')
    return render_template('nova_demanda.html')


@aplicacao.route('/criar', methods=['POST'])
def criar():
    # cria a nova e retorna a lista de demandas
    return redirect(url_for('lista_demandas'))


@aplicacao.route('/login')
def login():
    proxima = request.args.get('proxima_pagina')
    return render_template('login.html', proxima=proxima)


@aplicacao.route('/autenticar', methods=['POST'])
def autenticar():
    # busca o usuario no banco
    
#     usuario = usuario_dao.buscar_por_id(request.form['usuario'])

    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(f'Bem vindo, {usuario.nome}!', category='success')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Senha incorreta, tente novamente!', category='danger')
            return redirect(url_for('login'))
    else:
        flash('Usuário não cadastrado!', category='danger')
        return redirect(url_for('login'))


@aplicacao.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Até mais! ;)', category='info')
    return redirect(url_for('index'))


@aplicacao.route('/entrar')
def entrar():
    flash('Em breve será necessário efetuar o login. Por enquanto, fique a vontade!', category='info')
    return redirect(url_for('index'))


@aplicacao.route('/sobre')
def sobre():
    flash('Em breve!', category='info')
    return redirect(url_for('index'))


@aplicacao.route('/contato')
def contato():
    flash('Em breve!', category='info')
    return redirect(url_for('index'))