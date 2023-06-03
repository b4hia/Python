class player():
    def __init__(self, classe):
        self.life = 0
        self.player_level = 1
        self.player_xp = 0
        self.classe = classe
        self.dano_min = 0
        self.dano_max = 0
        self.habilidade = ""
        self.player_life = 0
        self.player_itens = []
        print("Escolha sua classe")
        if self.classe == "Clérigo":
            self.life = 80
            self.dano_min = 10
            self.dano_max = 22
            self.habilidade = "Luz divina"
        elif self.classe == "Guerreiro":
            self.life = 100
            self.dano_min = 15
            self.dano_max = 20
            self.habilidade = "Ataque pesado"
        elif self.classe == "Mago":
            self.life = 60
            self.dano_min = 8
            self.dano_max = 18
            self.habilidade = "Bola de fogo"
        else:
            print('escolha uma classe válida')
        self.player_life = self.life

    def ataque (self):
        return random.randint (self.dano_min, self.dano_max)
    
    def usar_habilidade(self):
        if self.classe == "Ladino":
            self.jogador_vida += self.ataque() // 2
            print('Você usou sua habilidade especial e ganhou', self.ataque()//2, 'pontos de vida.')
        elif self.classe == "Guerreiro":
            dano_habilidade = self.ataque() * 2
            print("Você usou sua habilidade especial e causou", dano_habilidade, 'pontos de dano')
        elif self.classe == "Mago":
            dano_habilidade = self.ataque() + 20
            print("Você usou sua habilidade especial e causou", dano_habilidade, 'pontos de dano.')
        return self.ataque()
    
    def batalha(self, inimigo_life):
        player_dano_bonus = 0
        inimigo_sono = 0
        while self.player_life > 0 and inimigo_life > 0:
            print('Sua vida:', self.player_life)
            print('Vida do Inimigo:', inimigo_life)
            print('Escolha sua ação:')
            print('1. Atacar')

            if self.player_life > 0:
                print('2. Curar')
                print('3. Usar Item')
            escolha = input('>>')
            
            if escolha == '1':
                player_dano = self.ataque() + player_dano_bonus
                inimigo_dano = random.randint(self.player_level*5, self.player_level*15)
                inimigo_life -= player_dano
                self.player_life -= inimigo_dano
                print('Você causou', player_dano, 'de dano ao inimigo.')
                print('O inimigo causou', inimigo_dano, 'de dano a você.')
                player_dano_bonus = 0
            
            elif escolha == '2' and self.player_life > 0:
                cura = random.randint(10,20)
                self.player_life += cura
                print('Você se curou em:', cura, 'pontos.')
            
            elif escolha == '3' and self.player_life > 0:
                if len(self.player_itens) == 0:
                    print('Seu inventário está vazio')
                else:
                    print('Itens no inventário:')
                    for i, item in enumerate(self.player_itens):
                        print(i + 1, '-', item)
                    item_escolhido = int(input("Escolha o número do item que deseja usar: "))
                    if item_escolhido <= 0 or item_escolhido > len(self.player_itens):
                        print('Escolha inválida.')
                    else:
                        item_usado = self.player_itens.pop(item_escolhido - 1)
                        print('Você usou', item_usado)

                        if item_usado == "Poção de força":
                            player_dano_bonus += 10
                            print("Seu próximo ataque terá +10 pontos de dano")
                        elif item_usado == "Poção de super cura":
                            self.player_life = self.life
                            print('Sua vida foi completamente restaurada.')
                        elif item_usado == "Poção de veneno":
                            inimigo_life -= 50
                            print("O inimigo sofreu 50 pontos de dano.")
                        elif item_usado == "Poção de sono":
                            inimigo_sono = 2
                            print("O inimigo está dormindo e não te atacará nas próximas duas rodadas.")
            else:
                print('Opção Inválida. Tente Novamente.')

            if inimigo_sono > 0:
                print('O inimigo está dormindo e não te atacará')
                inimigo_sono -= 1
            else:
                inimigo_dano = random.randint(self.player_level*5, self.player_level*15)
                self.player_life -= inimigo_dano
                print('O inimigo causou', inimigo_dano, "de dano a você.")
    
        if self.player_life <= 0:
            print('Você foi derrotado.')
            return self.player_life, self.player_level, self.player_xp
        else:
            print('Você derrotou o inimigo.')
            xp_ganho = random.randint(10,50)
            self.player_xp += xp_ganho
            print('Você ganhou', xp_ganho, 'pontos de experiência.')
        if self.player_xp >= 100:
            self.player_level += 1
            self.player_xp = 0
            print('Parabéns, você subiu para o nível', self.player_level, 'e está mais forte!')
        
        escolha_loot = input('Deseja lootear o inimigo? (s/n): ')
        if escolha_loot.lower() == 's':
            item_loot = random.choice(["Poção de força", "Poção de super cura", "Poção de veneno", "Poção de sono"])
            self.player_itens.append(item_loot)
            print('Você looteou uma', item_loot)
        return self.player_life, self.player_level, self.player_xp

def jogo():
    print("Bem-vindo ao jogo de RPG!")
    classe_escolhida = input('Escolha uma classe (Arqueiro, Guerreiro ou Mago): ')
    jogador = player(classe_escolhida)
    print('Você escolheu a classe', player.classe)
    print('Vida inicial:', player.life)    
    print('Habilidade Especial:', player.habilidade)

    while True:
        print('==NovaSala==')
        print('Você entrou em uma sala vazia.')
        print('Escolha sua ação:')
        print('1. Avançar para a próxima sala')
        print('2. Sair do jogo')

        escolha = input(">> ")

        if escolha == "1":
            inimigo_life = random.randint(60,80) + (player.player_level * 15)
            player.player_life, player.player_level, player.playe_xp = player.batalha(inimigo_life)
            if player.player_life <= 0:
                print('Você foi derrotado. Fim de Jogo.')
                break
        elif escolha == "2":
            break
        else:
            print('Opção inválida. Tente Novamente.')
    print('Obrigado por jogar!')
jogo()