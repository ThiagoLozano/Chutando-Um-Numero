from random import randint


class ChuteUmNumero:
    def __init__(self):
        # Escolhe um número para o computador.
        self.pc = randint(0, 10)
        self.contador = 0

    def Chutar(self):
        print("Estou pensando em um número entre 0 e 10!")
        # Pergunta para o usuário.
        jg = float(input("\nQual número você acha que é: "))
        self.contador += 1
        # Cria um laço de repetição até o jogador acertar.
        while self.pc != jg:
            print("Errou!")
            if self.pc > jg:
                # Caso o número digitado seja menor.
                print("Dica: Pensei em um número maior")
                jg = float(input("\nQual número você acha que é: "))
                self.contador += 1
            elif self.pc < jg:
                # Caso o número digitado seja maior.
                print("Dica: Pensei em um número menor")
                jg = float(input("\nQual número você acha que é: "))
                self.contador += 1
        else:
            if self.contador == 1:
                print("Uau, acertou de primeira!")
            print("\nAcertou!")
            # Retorna a quantidade de tentativas.
            print("Número total de Tentativas: {}".format(self.contador))


j = ChuteUmNumero()
j.Chutar()
