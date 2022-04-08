from PilhaEncadeada import Pilha
from Jogador import Jogador
from Baralho import Baralho
import random




print("---------- Batalha ---------- \n")

#Loop principal
while (True):
    
    contadorDeJogadas = 0
    baralho = Baralho()
    montanteDeEmpate = list()

    #Instanciando os dois jogadores
    print("Digite o nome do jogador 1")
    nomeDoJogador1 = input()
    jogador1 = Jogador(nomeDoJogador1)
    print()

    print("Digite o nome do jogador 2")
    nomeDoJogador2 = input()
    jogador2 = Jogador(nomeDoJogador2)
    print()

    
    #Distribuindo as cartas
    tamanho_do_baralho = baralho.__len__() 
    numero_de_rodadas = (tamanho_do_baralho - 1) / 2 #
    n = 0
    #*******transformar em método "contarRodadas"
    while(n <= numero_de_rodadas):
        n += 1
        jogador1.cartasDoJogador.empilha(baralho.retirarCarta())
        jogador2.cartasDoJogador.empilha(baralho.retirarCarta())

    print(jogador1)
    print(jogador2)
    #Loop para numerar a jogada da vez.
    while(contadorDeJogadas <= 25):
        print()
        print(f"------------------- Jogada #{contadorDeJogadas + 1}: --------------------\n")

        print(f"Carta do jogador(a) {jogador1.nome}: ") #Informa a carta do jogador.
        cartaNaMaoDoJogador1 = jogador1.cartasDoJogador.desempilha() #Retira a carta da coleção do jogador e atribui a mao.
        print(cartaNaMaoDoJogador1)
        print()

        print(f"Carta do jogador(a) {jogador2.nome}: ")
        cartaNaMaoDoJogador2 = jogador2.cartasDoJogador.desempilha()
        print(cartaNaMaoDoJogador2)
        print()

        numeroCartaNaMaoDoJogador1 = cartaNaMaoDoJogador1.numero #Recebe o numero da carta.
        numeroCartaNaMaoDoJogador2 = cartaNaMaoDoJogador2.numero

        

        # Controle da pontuação por rodada e armazenamento nos montantes reservas.
        if (numeroCartaNaMaoDoJogador1 > numeroCartaNaMaoDoJogador2 ):
            jogador1.pontos += 1
            jogador1.montanteReserva.append(cartaNaMaoDoJogador2) #Carta recebida em caso de vitoria vai para outro montante


            print(f"PONTO PARA O JOGADOR {jogador1.nome}")
            print(f"Cartas adquirida: ")
            print(f"{cartaNaMaoDoJogador2}")
            print()
            #No caso de emprate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            if(montanteDeEmpate != []):
                for carta in montanteDeEmpate:
                    print(carta.__str__(), sep="\n")
            
            jogador1.montanteReserva.append(montanteDeEmpate)
            montanteDeEmpate.clear()
            

        elif (numeroCartaNaMaoDoJogador1 < numeroCartaNaMaoDoJogador2 ):
            jogador2.pontos += 1
            jogador2.montanteReserva.append(cartaNaMaoDoJogador1)

            print(f"PONTO PARA O JOGADOR {jogador2.nome}")
            print(f"Cartas adquirida: ")
            print(f"{cartaNaMaoDoJogador1}")
            print()


            if(montanteDeEmpate != []):
                for carta in montanteDeEmpate:
                    print(carta.__str__(), sep="\n")
            
            jogador2.montanteReserva.append(montanteDeEmpate)
            montanteDeEmpate.clear()



        # Caso haja empate, armazenaremos a carta para atribuição futura.
        elif(numeroCartaNaMaoDoJogador1 == numeroCartaNaMaoDoJogador2):
            montanteDeEmpate.append(cartaNaMaoDoJogador1)
            montanteDeEmpate.append(cartaNaMaoDoJogador2)

            for x in range(len(montanteDeEmpate)):
                print(montanteDeEmpate[x] , sep="\n")

        print(f"--------- PLACAR DA RODADA ---------")
        print(f"{jogador1.pontos} x {jogador2.pontos}")

        if(jogador1.cartasDoJogador.estaVazia()):
            for carta in jogador1.montanteReserva: 
                random.shuffle(jogador1.montanteReserva)
                jogador1.cartasDoJogador.empilha(carta)
                

        if(jogador2.cartasDoJogador.estaVazia()):
            for carta in jogador1.montanteReserva:
                random.shuffle(jogador2.montanteReserva)     
                jogador2.cartasDoJogador.empilha(carta)
        contadorDeJogadas += 1

    #Verifica se o usuário gostaria de jogar novamente.
    print()
    print("Deseja jogar novamente? (s/n)")
    jogarNovamente = input()
    

    if (jogarNovamente.upper() == 'N'):
        break










