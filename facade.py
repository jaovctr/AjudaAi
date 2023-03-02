from model import *
import notifica

def listagem_tags():
    return tags


def busca_tag_id(id):
    return [t['nome'] for t in tags if t['id'] == id][0]


def busca_demanda_id(id):
    for indice, demanda in enumerate(demandas):
        if demanda['codDemanda'] == id:
            return indice, demanda


def busca_usuario_id(id):
    return [u for u in usuarios if u['codUsuario'] == id][0]
    

def listagem_topicos_forum():
    aux = topicos_forum.copy()
    for t in aux:
        t['usuario'] = busca_usuario_id(t['codUsuario'])

    return aux
    
    
def listagem_demandas(id_usuario=0):
    if id_usuario:
        return [d for d in demandas if d['codUsuario'] == id_usuario]
    else:
        return demandas


def apaga_demanda(id):
    global demandas
    pos = busca_demanda_id(id)[0]
    demandas = demandas[:pos] + demandas[pos+1:]


def notifica_usuarios(nome_tags: list, tipo: str):
    usuarios_envio = set()

    for t in nome_tags:
        for u in usuarios:
            if t in u['tags']:
                usuarios_envio.add(u['email'])

    if tipo == 'nova demanda':
        assunto = 'Nova demanda cadastrada! ;)'
        corpo = 'Ei, ajuda aí! Uma nova demanda foi cadastrada'\
                + ' com uma de suas tags de interesse!'
    else:
        assunto = 'Nova dúvida cadastrada no fórum! ;)'
        corpo = 'Ei, ajuda aí! Um novo tópico acaba de ser criado'\
                + ' no fórum com um tema de seu interesse!'

    notifica.enviar_emails(assunto, usuarios_envio, corpo)


def salvar_topico_forum(titulo, descricao, usuario_padrao):
    global topicos_forum

    






def salvar_demanda(titulo, tipo, descricao, tags, codDemanda=0, codUsuario=0):
    global demandas
    lista = [busca_tag_id(int(id)) for id in tags]
    tags = '; '.join(lista)

    if codDemanda:
        pos = busca_demanda_id(id)[0]
        demandas[pos]['descricao'] = descricao
        demandas[pos]['titulo'] = titulo
        demandas[pos]['tipo'] = tipo
        demandas[pos]['tags'] = tags
    else:
        notifica_usuarios(tags.split('; '), 'nova demanda')
        demandas.append({
            'codDemanda': prox_id_demanda(),
            'titulo': titulo,
            'tags': tags,
            'tipo': tipo,
            'descricao': descricao,
            'status': 'Em aberto',
            'codUsuario': codUsuario
        })

    return True


# def editar_demanda(codDemanda, titulo, tipo, descricao, tags):
#     global demandas

#     demanda = busca_demanda_id(id)
#     salvar_demanda(titulo, tipo, descricao, tags, codDemanda)
