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

#exerc.3
from random import sample, randint
vetor1 = []
vetor2 = []
vetor3 = []
for cont in range(10):
    v1 = sample(range(1, 100), 1)
    vetor1.append(v1)
    vetor3.append(v1)
    v2 = sample(range(1, 100), 1)
    vetor2.append(v2)
    vetor3.append(v2)
print(vetor1)
print(vetor2)
print(vetor3)

#exerc.4
texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our
community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''
list1=[]
texto = texto.replace(',', ' ')
texto = texto.replace('.', ' ')
texto = texto.replace(':', ' ')
texto = texto.lower()
txt = texto.split()
for palavras in txt:
    if palavras[0] in 'python' or palavras[-1] in 'python':
        list1.append(palavras)
print(list1)


#exerc.5
texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our
community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''
list1=[]
list2=[]
texto = texto.replace(',', ' ')
texto = texto.replace('.', ' ')
texto = texto.replace(':', ' ')
texto = texto.lower()
txt = texto.split()
for palavras in txt:
    if palavras[0] in 'python' or palavras[-1] in 'python':
        list2.append(palavras)
for p in list2:
    if len(p) > 4:
        list1.append(p)
print(list2)
print(list1)
print(f''' há {len(list1)} palavras que começam ou terminam com uma
das letras de 'python' e que possuem 4 ou mais caracteres''')


