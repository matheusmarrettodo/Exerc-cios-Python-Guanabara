km=float(input('Quantos Km foram percorridos?'))
d=int(input('E quantos dias foi alugado?'))
pkm=km*0.15
pd=d*60
tt=pkm+pd
print('Dados os valores, será cobrado R${} por km rodado, mais R${} por dias alugados.'.format(pkm,pd))
print('Totalizando R${} .'.format(tt))
print('Obrigado por nos escolher, e pode contar com a gente sempre!')
