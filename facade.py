from model import *

def listagem_demandas(id_usuario=0):
    if id_usuario:
        return [d for d in demandas if d['codUsuario'] == id_usuario]
    else:
        return demandas


def busca_demanda_id(id):
    for indice, demanda in enumerate(demandas):
        if demanda['codDemanda'] == id:
            return indice, demanda


def apaga_demanda(id):
    global demandas
    pos = busca_demanda_id(id)[0]
    demandas = demandas[:pos] + demandas[pos+1:]


def salvar_demanda(titulo, tipo, descricao, tags, codDemanda=0, codUsuario=0):
    global demandas

    if codDemanda:
        pos = busca_demanda_id(id)[0]
        demandas[pos]['descricao'] = descricao
        demandas[pos]['titulo'] = titulo
        demandas[pos]['tipo'] = tipo
        demandas[pos]['tags'] = tags
    else:
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
