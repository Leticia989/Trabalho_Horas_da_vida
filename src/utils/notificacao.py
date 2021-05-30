def OMS(usuario):

    crianca = 'Voce é uma cirança, não deveria ter acesso sem um responsável '
    jovem = 'Voce é um Jovem  '
    adolecente_jovem = 'Voce é um adolecente jovem'
    meia_idade = 'Voce está na faixa da meia idade'
    idoso = 'voce é um Idoso'
    anciao = 'vocé é  um Ancião'
    velhice_extrema = 'Sua taixa é de Velhice extrema'

    if 10 <= usuario['idade'] > 19:
        mensagem = adolecente_jovem
    elif 20 <= usuario['idade'] > 24:
        mensagem = jovem
    elif 40 <= usuario['idade'] > 59:
        mensagem = meia_idade
    elif 60 <= usuario['idade'] < 74:
        mensagem = idoso
    elif 75 <= usuario['idade'] < 90:
        mensagem = anciao
    elif usuario['idade'] > 90:
        mensagem = velhice_extrema
    else:
        mensagem = crianca

    return mensagem
