#Wellcome to Dungeons and Py, by Gabriel de Oliveira.
from time import sleep
from random import sample, randint
print ('''
    Você é um aluno da Fatec prof Jessen Vidal, porém algo não está certo...
    A Fatec está mais vazia do que nunca, nenhum aluno está nos corredores, um momento!
    Você avista o Benê, secretário da faculdade, ele parece estar te chamando, talvez ele queira dizer algo...
    ''')
sleep(1)
#Definindo atributos iniciais
class player():
    def __init__(self, name):
        lifeplayer = 0
        lifeplayer = lifeplayer + 20
        levelplayer = '1'
        damageplayer = '2'
        defenseplayer = '5'
        iventory = []

#INIMIGOS
class faxineira():
    def __init__(self, name)
        self.nome = nome
        self.maxlife = 
life = 0
life = life + 12
damage = '4'
atkfaxin = sample(range(1,20), 1)
defense = 5
str(defense)
ivent = []


#Funções
def combate_faxineira():
    rodada = 0
    global life
    global atkfaxin
    while life > 0:
        rodada += 1
        if rodada % 2 != 0:
            atk = sample(range(1,20), 1)
            str(atk).strip('[]')
            print(f'seu resultado foi {atk}')
            if str(atk) >= str(defense):
                print(f'você desfere um soco na cara da faxineira!')
                print(f'você causa {damageplayer} pontos de dano')
                atq = int(list(atk[0]))
                life = life - atq
                sleep(1)
            else:
                print(f'você erra o seu ataque')
        else:
            atkfaxin
            print('a faxineira vai atacar você')
            print(f'seu resultado foi {atkfaxin}')
            print(f'sua defesa é: {defenseplayer}')
            if atkfaxin >= defenseplayer:
                print('a faxineira te dá uma vassourada')
                print(f'você recebe {damage} pontos de dano')
                lifeplayer = lifeplayer - damage
                sleep(1)
            else:
                print('a faxineira erra da uma tenta te acertar, porém você esquiva')
                
                    
        
        

print('==========================================================================================================================')
print(f'O que você vai fazer?')
print('''
    [1] ir até o Benê
    [2] continuar andando
    ''')
firstchoice = input('sua escolha: ')
if firstchoice == '1':
    #Você vai até o Benê
    print('==========================================================================================================================')
    print('...')
    print()
    sleep(1)
    print('Você se aproxima de Benê')
    print()
    sleep(1)
    print('Benê: "Ei oque você está fazendo? Deveria estar escondido(a) junto dos outros!"')
    print()
    sleep(1)
    print('Benê: "Que cara é essa? não se faça de louco(a) por acaso não sabe do que estou falando?"')
    sleep(1)
    print()
    print('''Benê: "Bom vou explicar de maneira rápida! O Arakaki enlouqueceu! Ele decidiu coordenar toda a faculdade, para isso
    ele implantou no café dos funcionários microchips de controle mental, mas por algum motivo não fui afetado..."''')
    print()
    sleep(1)
    print('''Benê: "Aparentemente os microchips estão sendo alimentados pelo servidor, eu mesmo iria até lá porém é muito arriscado
    alguns alunos tentaram e foram capturados..."''')
    print()
    sleep(1)
    print('''Benê: "Mas olhe para você! você parece forte e habilidoso(a), tenho certeza que você conseguiria libertar a Fatec do controle
    do Arakaki!! Posso sentir isso"''')
    print()
    sleep(1)
    print('''Benê: "Ouça com atenção, se fizer isso pela Fatec, irei garantir que receba uma recompensa, algo incrível e extraordinário!"''')
    sleep(1)
    print()
    print('''Benê: "Então, você topa?"''')
    sleep(1)
    print('==========================================================================================================================')
    print(f'O que você vai fazer?')
    print('''
        [1] aceitar a missão
        [2] perguntar sobre a recompensa
        ''')
situação1 = input('sua escolha: ')
if situação1 == '1':
    #Você aceita a missão do Benê
    print('==========================================================================================================================')
    print('...')
    sleep(1)
    print()
    print('Um sorriso surge no rosto de Benê')
    print()
    sleep(1)
    print('''Benê: "Ótimo, antes de você seguir preciso te alertar sobre algumas coisas... primeiramente, NÃO use o elevador!
    O Arakaki saberia que você o usou e te encontraria no mesmo instânte"''')
    print()
    sleep(1)
    print('''Benê: "Segundamente saiba que em cada andar há um pendrive com uma chave.pem, você vai precisar de todos os 4 pendrives
    caso queira acessar o servidor, portanto, encontreo-os e só então vá para o servidor"''')
    sleep(1)
    print()
    print('''"Benê: "Um último aviso... os pendrives devem estar sendo protegidos pelos funcionários, tome cuidado, eles farão de tudo
    para garantir que você não saia vivo do andar deles!"''')
    print()
    sleep(1)
    print('Benê pega alguma coisa do balcão')
    print()
    print('''Benê: "pegue isto e use em caso de emergência, o Caique estava procurando por ela... se usar contra algum oponente, concerteza
    o Caique virá em sua direção e ajudará na luta"''')
    print()
    print('===== Uma bola de vôlei foi adicionada ao seu inventário!! =====')
    iventory.append('bola de vôlei')
    print()
    print('Ao entregar a bola de vôlei Benê se despede e desaparece atrás do balcão da secretária...')
    print()
    sleep(1)
    print('==========================================================================================================================')
    print(f'O que você vai fazer?')
    print('''
        [1] subir as escadas para o primeiro andar
        [2] usar o elevador
        ''')
    próximoandar1situ1 = input('sua escolha: ')
    if próximoandar1situ1 == '1':
    #Você usa as escadas para o próximo andar
        print('==========================================================================================================================')
        print('...')
        sleep(1)
        print()
        print('ao subir as escadas você se depara com uma das faxineiras')
        print()
        sleep(1)
        print('ela está segurando uma vassoura e te encara com um olhar feroz, ela definitivamente vai te atacar!')
        sleep(1)
        print('==========================================================================================================================')
        print(f'O que você vai fazer?')
        print('''
        [1] lutar com a faxineira
        [2] passar correndo por ela
        ''')
        faxineira = input('sua escolha: ')
        if faxineira == '1':
        #Você decidiu lutar com a faxineira
            print('==========================================================================================================================')
            print('...')
            sleep(1)
            print()
            print('o combate começou')
            sleep(1)
            print('==========================================================================================================================')
            print(f'O que você vai fazer?')
            print('''
                [1] atacar
                [2] usar item
                [3] pular a vez
                ''')
            combate = input('sua escolha: ')
            if combate == '1':
                combate_faxineira()
                
    
    elif próximoandar1situ1 == '2':
    #Você usa o elevador para o próximo andar
        print('==========================================================================================================================')
        print('...')
    
    
    elif situação1 == '2':
        #Você pergunta sobre sua recompensa
        print('==========================================================================================================================')
        print('...')
        sleep(2)
        print()
        print('''Benê: "Bom a recompensa pode ser muitas coisas, um troféu, ser aprovado automaticamente em todas as matérias durante um semestre,
        tickets de alimentação para serem usados no trailer..."''')
        print()
        print('Benê fica pensando por um tempo')
        print('...')
        sleep(2)
        print('Benê: "Olha... não se preocupe, você será recompensado! de um jeito ou de outro"')
        print()
        print('Benê: "Agora vamos ao que interessa: sua missão!"')
        print()
        sleep(1)
        print('''Benê: "Antes de você seguir preciso te alertar sobre algumas coisas... primeiramente, NÃO use o elevador!
        O Arakaki saberia que você o usou e te encontraria no mesmo instânte"''')
        print()
        sleep(4)
        print('''Benê: "Segundamente saiba que em cada andar há um pendrive com uma chave.pem, você vai precisar de todos os 4 pendrives
        caso queira acessar o servidor, portanto, encontreo-os e só então vá para o servidor"''')
        sleep(8)
        print()
        print('''Benê: "Um último aviso... os pendrives devem estar sendo protegidos pelos funcionários, tome cuidado, eles farão de tudo
        para garantir que você não saia vivo do andar deles!"''')
        print()
        sleep(5)
        print('Benê pega alguma coisa do balcão')
        print()
        sleep(2)
        print('''Benê: "pegue isto e use em caso de emergência, o Caique estava procurando por ela... se usar contra algum oponente, concerteza
        o Caique virá em sua direção e ajudará na luta"''')
        print()
        print('===== Uma bola de vôlei foi adicionada ao seu inventário!! =====')
        iventory.append('bola de vôlei')
        print()
        sleep(3)
        print('Ao entregar a bola de vôlei Benê se despede e desaparece atrás do balcão da secretária...')
        print()
        sleep(2)
        print('==========================================================================================================================')
        print(f'O que você vai fazer?')
        print('''
            [1] subir as escadas para o primeiro andar
            [2] usar o elevador
            ''')
        próximoandar1situ1 = input('sua escolha: ')
        if próximoandar1situ1 == '1':
        #Você usa as escadas para o próximo andar
            print('==========================================================================================================================')
            print('...')
            print()


        elif próximoandar1situ1 == '2':
        #Você usa o elevador para o próximo andar
            print('==========================================================================================================================')
            print('...')


elif firstchoice == '2':
    #Você ignora o Benê e continua andando
    print('==========================================================================================================================')
    print('...')
    print()
    sleep(2)
    print('Você decide ignorar o Benê e continua andando')
    print()
    print('Um momento...Você vê uma figura conhecida descendo as escadas!É o Mec well...ele parece estar ferido')
    sleep(4)
    print()
    print('Mec Well se aproxima de você')
    print()
    sleep(2)
    print('Mec Well:"ei cara tá fazendo o que?')
    print()
    sleep(2)
    print('''Mec Well:"Você parece não saber de nada, então vou mandar o papo reto: O Arakaki enlouqueceu! Ele decidiu coordenar
    toda a faculdade, não sei como mas ele implantou microchips de controle mental nos funcionários..."''')
    sleep(7)
    print()
    print('''Mec Well:"Não sei ao certo se alguém conseguiu escapar mas a maioria dos nossos professores sucumbiram... Já o restante dos
         alunos decidiu se esconder ou tentar parar essa loucura!''')
    print()
    print('Mec Well:"eu sou um dos que tentou parar o Arakaki"')
    sleep(5)
    print('''Mec Well:"Talvez você tenha mais sorte do que eu, até porque você parece especial, posso sentir isso!"''')
    print()
    print('''Mec Well:"Até onde sei o Arakaki está usando o servidor para manter os chips funcionando, se você conseguir derrubar o servidor
    todos seriam libertados e claro, você receberia uma grande recompensa por libertar a Fatec do controle do Arakaki!!"''')
    sleep(7)
    print()
    print('''Mec Well:"Eai tá dentro?"''')
    print('''
        [1] aceitar a missão
        [2] perguntar sobre o Benê
        [3] ajudar nos ferimentos Mec Well
        ''')
situação2 = input('sua escolha: ')
if situação2 == '1':
    print('==========================================================================================================================')
    print('...')
elif situação2 == '2':
    print('==========================================================================================================================')
    print('...')
if situação2 == '3':
    print('==========================================================================================================================')
    print('...')
    
    
    
    
