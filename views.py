import facade
from flask import *
from aplicacao import aplicacao

visualizar_lista = 0

def login_usuario(url_seguinte):
    return redirect(url_for('login', proxima_pagina=url_for(url_seguinte)))


@aplicacao.route('/')
def index():
    return render_template('index.html')


@aplicacao.route('/nova_demanda')
def nova_demanda():
#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
#         return login_usuario('nova_demanda')
    return render_template('nova_demanda.html', tags=facade.listagem_tags())


@aplicacao.route('/criar', methods=['GET', 'POST'])
def criar_demanda():
    tags = list()
    titulo = request.form['titulo']
    tipo = request.form['tipo-demanda']
    descricao = request.form['descricao-demanda']

    for i in range(4):
        tag_id = request.form[f'select_tag{i}']
        
        if tag_id:
            tags.append(tag_id)

    if facade.salvar_demanda(titulo, tipo, descricao, tags):
        flash('Demanda criada com sucesso! Acesse a página Minhas Demandas para visualizar suas demandas.',
        category='success')
    else:
        flash('Ocorreu um erro ao cadastrar sua demanda! Tente novamente em outro momento e, '
            + 'se o erro persistir, entre em contato conosco.',
        category='danger')

    return redirect(url_for('index'))


@aplicacao.route('/lista_demandas')
def lista_demandas():
    global visualizar_lista
    visualizar_lista = 1
    return render_template('lista_demandas.html', demandas=facade.listagem_demandas())


@aplicacao.route('/minhas_demandas')
def minhas_demandas():
    global visualizar_lista
    visualizar_lista = 0

#     if 'usuario_logado' not in session or session['usuario_logado'] is None:
#         return login_usuario('nova_demanda')
    return render_template('minhas_demandas.html', demandas=facade.listagem_demandas(1))


@aplicacao.route('/retorna_lista')
def retorna_lista():
    global visualizar_lista
    if visualizar_lista: # lista geral
        return redirect(url_for('lista_demandas'))
    else:
        return redirect(url_for('minhas_demandas'))


@aplicacao.route('/visualizar_demanda/<int:cod>')
def visualizar_demanda(cod):
    demanda = facade.busca_demanda_id(cod)[1]
    return render_template('visualizar_demanda2.html', demanda=demanda)


@aplicacao.route('/apagar_demanda/<int:cod>/<int:pagina>')
def apagar_demanda(cod, pagina):
    demanda = facade.apaga_demanda(cod)
    
    if pagina == 1: # lista geral
        return redirect(url_for('lista_demandas'))
    else:
        return redirect(url_for('minhas_demandas'))


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