import time

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #crio uma lista com as letras

def tamanho(t): #função que determina o tamanho da arvore de acordo com o valor de 't'
    if 1 <= t <= 26: #verifica se o valor passado está dentro do limite minímo e máximo para fazer a árvore

        for count in range(t): #vou criar cada galho da árvore até o limite através de um loop e contador
            if count == 0: #quando o contador é 0 (quando ele começa no caso
                galho = letras[count] #defino a letra do galho que estou de acordo com o contador
                alinhamento = [' '] * (t - count - 1) #faço alinhamento dando espaços vazios olhando: o tamnho da arvore - numero do galho -1(para deixar simétrico)
                arvore = alinhamento + [galho] + alinhamento #defino o topo da minha árvore
                print(''.join(arvore)) #printo 'a'
            elif count == 1: #quando o contador passa para 1 (próximo loop)
                galho = letras[count] #defino uma nova letra para este galho, no caso: 'b'
                asterisco = ['*'] #coloco '*'
                alinhamento = [' '] * (t - count - 1) #faço novamente o mesmo alinhamento
                arvore = alinhamento + [galho] + asterisco + [galho] + alinhamento #defino o galho depois do topo, dessa vez possuí asterisco
                print(''.join(arvore)) #printo 'b*b'
            else: #para os demais tamanhos de galhos
                asterisco = ['*'] * (count * 2 - 1 ) #defino o número de asteriscos, sendo que o -1 é para deixar simétrico
                galho = letras[count] #defino uma letra para o galho de acordo com o contador
                alinhamento = [' '] * (t - count - 1) #novamente faço o alinhamento do galho
                arvore = alinhamento + [galho] + asterisco + [galho] + alinhamento #defino o galho seguinte
                print(''.join(arvore)) # printo

    else:
        print("Erro!") #caso o valor seja maior que 26, pois as letras de a-z vão até 26.

print('Olá sou um programa em python que irá gerar uma árvore de natal com letras do alfabeto nas suas extremidades!')
time.sleep(3)
t = int(input("Informe o tamanho que você deseja para a sua árvore: "))
time.sleep(1)
print('gerando árvore...')
time.sleep(3)
tamanho(t)