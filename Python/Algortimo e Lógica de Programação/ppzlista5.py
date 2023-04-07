#exerc.1
from random import sample, randint
num = sample(range(1, 100), 10)
ma = []
me = []
print(num)
for nume in num:
    if ma > num:
        ma = num
    print(ma)
    if me > num:
        me = num
    print(me)
print(' ')
    
#exerc.2
from random import sample, randint
lista = sample(range(1, 100), 10)
par = []
impar = []
for numeros in lista:
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)
print(f'numeros: {lista}')
print(f'numeros pares: {par}')
print(f'numeros impares: {impar}')
    
    
