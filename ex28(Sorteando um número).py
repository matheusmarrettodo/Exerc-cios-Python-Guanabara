import random
n=[1,2,3,4,5]
ns=random.choice(n)
ne=int(input('Escolha um número de 0 a 5: '))
if ns==ne:
    print('PARABÉNS! VOCÊ ACERTOU O NÚMERO!')
else:
    print('Poxa, Não foi dessa vez.')
