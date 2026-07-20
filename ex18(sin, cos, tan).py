import math
a=float(input('Digite o valor do angulo: '))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('O valor do seno de {}° é {:.2f}'.format(a,s))
print('O valor do cosseno de {}° é {:.2f}'.format(a,c))
print('E o valor tangente de {}° é {:.2f}'.format(a,t))
