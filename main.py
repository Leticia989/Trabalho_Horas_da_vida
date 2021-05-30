from src.usuario import usuario
from src.telas.idoso import converte_data_nascimento_idade, nome_usuario, Verifica_nasciento
from src.utils.notificacao import OMS


def Interacao():
    usuario_maior_idade = None
    maior_idade = 0
    pessoas = []
    count = 1
    while True:
        print(f'Pessoa {count}')
        pessoa = usuario()
        pessoa.nome = nome_usuario()
        if pessoa.nome == 'Fim' or pessoa.nome == 'fim':
            break
        pessoa.data_nascimento = Verifica_nasciento()
        dicionario_usuario = {
            'nome': pessoa.nome,
            'idade': converte_data_nascimento_idade(pessoa.data_nascimento)
        }
        pessoas.append(dicionario_usuario)
        if dicionario_usuario['idade'] > maior_idade:
            usuario_maior_idade = dicionario_usuario
            maior_idade = dicionario_usuario['idade']
        count += 1
        print(OMS(dicionario_usuario))
        print('='*35)
    print(f'Pessoas cadastradas: {pessoas}')
    print(f'Pessoa mais velha: {usuario_maior_idade}')


Interacao()