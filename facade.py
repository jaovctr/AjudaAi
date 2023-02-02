from model import *

def listagem_demandas(id_usuario=0):
    if id_usuario:
        return [d for d in demandas if d['codUsuario'] == id_usuario]
    else:
        return demandas


def busca_demanda_id(id) -> dict:
    return [d for d in demandas if d['codDemanda'] == id][0]


def apaga_demanda(id):
    global demandas
    
    for i in range(len(demandas)):
        if demandas[i]['codDemanda'] == id:
            demandas = demandas[:i] + demandas[i+1:]
            break
