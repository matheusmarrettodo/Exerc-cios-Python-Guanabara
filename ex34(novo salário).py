s=float(input('Digite o seu salário:R$'))
if s>1250:
    sa=(s*0.10)+s
    print('o valor de novo salário é de: R${}'.format(sa))
else:
    sa=(s*0.15)+s
    print('o valor de novo salário é de: R${}'.format(sa))
