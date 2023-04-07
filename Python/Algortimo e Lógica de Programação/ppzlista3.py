#Lista3
#Exercicio 1
n1 = int(input('Digite uma nota de 0 a 10: '))
while n1 > 0 and n1 < 10:
    print('A nota está ok')
    break
else:
    print('Digite um valor valido')

#Exercicio 2
nome = (input('Digite um nome: '))
senha = (input('Digite uma senha: '))
while nome == senha:
    print('Erro! Digite uma senha diferente do nome. ')
    break

#Exercicio3
ca = 0
cb = 0
pa = 80000 + ca
pb = 200000 + cb
x = 1
while pa <= pb:
    ca = (pa*0.03*x)+ ca
    cb = (pb*0.015*x)+ cb
    pa = 80000 + ca
    pb = 200000 + cb
    x = x+1
    if pa >= pb:
        print(f'São nescessários {x} anos para A superar B')
        break
    
    
    
