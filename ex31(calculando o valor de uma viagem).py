v= float(input('Digite a distância da viagem: '))
if v<=200:
    vr=v*0.50
    print('O valor da viagem é de R${} '.format(vr))
else:
    vr=v*0.45
    print('O valor da viagem é de R${}'.format(vr))
print('Uma boa viagem!')
