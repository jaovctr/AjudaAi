demandas = [
    {
        'codDemanda': 1,
        'titulo': 'Monitoria sobre Bioquímica',
        'tags': 'BIOLOGIA - Bioquímica; BIOLOGIA - Biologia I',
        'tipo': 'Aberto a membros',
        'descricao': 'Gostaria de alguém para me auxiliar sobre estrutura e função metabólica de componentes celulares.',
        'status': 'Em aberto',
        'codUsuario': 3
    },
    {
        'codDemanda': 2,
        'titulo': 'Revisão do Abstract',
        'tags': 'INGLÊS: A1; INGLÊS: Gramática; INGLÊS: Revisão abstract',
        'tipo': 'Individual',
        'descricao': 'Possuo conhecimento básico de inglês e procuro monitoria para revisar comigo o abstract do meu artigo.',
        'status': 'Em aberto',
        'codUsuario': 1
    },
    {
        'codDemanda': 3,
        'titulo': 'Monitoria de programação',
        'tags': 'COMPUTAÇÃO: Algoritmo; COMPUTAÇÃO: Programação Estruturada; COMPUTAÇÃO: Linguagem C',
        'tipo': 'Aberto a membros',
        'descricao': 'Sou estudante de bioinformática e preciso aprender scripts em python, mas possuo dificuldade em lógica de programação.',
        'status': 'Finalizado',
        'codUsuario': 1
    },
    {
        'codDemanda': 4,
        'titulo': 'Monitoria sobre Cálculo',
        'tags': 'CÁLCULO: Derivadas; CÁLCULO: Integrais',
        'tipo': 'Individual',
        'descricao': 'Gostaria de alguém para me auxiliar na parte derivadas e integrais. Estou com muita dificuldade.',
        'status': 'Em aberto',
        'codUsuario': 5
    },
]

tags = [
        {'nome': 'COMPUTAÇÃO - Programação Estruturada', 'id': 1},
        {'nome': 'COMPUTAÇÃO - Banco de Dados', 'id': 2},
        {'nome': 'ESTATÍSTICA - Análise Combinatória', 'id': 3},
        {'nome': 'FÍSICA - Leis de Newton', 'id': 4},
        {'nome': 'LETRAS INGLÊS - Confecção de Abstract', 'id': 5},
        {'nome': 'LETRAS INGLÊS - Tempos Verbais', 'id': 6}
    ]


def prox_id_demanda():
    return demandas[-1]['codDemanda'] + 1


def busca_demanda_id(id):
    for indice, demanda in enumerate(demandas):
        if demanda['codDemanda'] == id:
            return indice, demanda


def busca_tag_id(id):
    return [t['nome'] for t in tags if t['id'] == id][0]