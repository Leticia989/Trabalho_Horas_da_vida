import datetime

def nome_usuario():
    try:
        nome = input('Digite seu nome ')
    except Exception:
        raise Exception
    else:
        return nome


def Verifica_nasciento():
    try:
        dia = eval(input('Digite o dia de seu nascimento '))
        mes = eval(input('Digite o mês do seu nascimento '))
        ano = eval(input('Digite o ano do seu nascimento '))
        data_nascimento = datetime.date(ano, mes, dia)
    except Exception:
        raise Exception
    else:
        return data_nascimento


def converte_data_nascimento_idade(data_nascimento):
    data_atual = datetime.date.today()
    idade = (data_atual - data_nascimento) / 365.25
    return idade.days