v=float(input('Velocidade do carro: '))
if v>80:
    vs=(v-80)*7
    print('Você foi multado!')
    print('O valor da multa é de R$7,00 por cada KM/H excedido.')
    print('Então a multa é de: R$ {}'.format(vs))
else:
    print('Parabéns, você conduz de forma segura!')
