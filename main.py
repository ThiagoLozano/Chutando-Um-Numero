from random import randint


class ChuteUmNumero:
    def __init__(self):
        self.pc = randint(0, 10)
        self.contador = 0

    def chutar(self):
        print("Estou pensando em um número entre 0 e 10!")
        jg = float(input("\nQual número você acha que é: "))
        self.contador += 1
        while self.pc != jg:
            print("Errou!")
            if self.pc > jg:
                print("Dica: Pensei em um número maior")
                jg = float(input("\nQual número você acha que é: "))
                self.contador += 1
            elif self.pc < jg:
                print("Dica: Pensei em um número menor")
                jg = float(input("\nQual número você acha que é: "))
                self.contador += 1
        else:
            if self.contador == 1:
                print("Uau, acertou de primeira!")
            print("\nAcertou!")
            print("Número total de Tentativas: {}".format(self.contador))


j = ChuteUmNumero()
j.chutar()
