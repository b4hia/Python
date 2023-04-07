print('Exercicio1')
l1 = float(input('Insira o tamanho do lado1: '))
l2 = float(input('Insira o tamanho do lado2: '))
l3 = float(input('Insira o tamanho do lado3: '))
if (l1 + l2 < l3) or (l1 + l3 < l2) or (l3 + l2 < l1):
    print('Não é triangulo')
else:
        print('É triagulo')
        if (l1==l2) & (l2==l3):
            print('É um triangulo equilatero')
        if (l1==l2) or (l1==l3) or (l2==l3):
            print('É um triangulo isoceles')
        else:
            print('É um triangulo escaleno')

print('Exercicio2')
ano = int(input('Insira o ano: '))
if (ano % 4==0) & (ano % 100!=0) or (ano % 400==0):
        print('Ano bissexto')
else:
        print('Não é ano bissexto')
