# PROJETO PYTHON: Chutando Um Número

> Um programa que gera um um valor que pede para o usuário advinhar ele.

  O programa deve gerar um valor aleatório, deve pedir para o usuário adivinhar o valor que
o programa gerou, o usuário deve inserir o valor que acha ser o certo. Caso o usuário não acerte
de primeira o programa deve dizer quanto falta para acertar, retornando se o valor gerado é mais
alto ou mais baixo, quando o usuário acertar, o programa deve contabilizar o total de tentativas.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
class ChuteUmNumero:
    def __init__(self):
        self.pc = randint(0, 10)
        self.contador = 0
```
![Classe](https://github.com/ThiagoLozano/Chutando-Um-Numero/blob/master/Screenshot/Classe.PNG)

### Função que pede para o usuário chutar um valor
```
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
```
![Chutando um Valor](https://github.com/ThiagoLozano/Chutando-Um-Numero/blob/master/Screenshot/Funcao.PNG)

# Bibliotecas e Configurações

### Biblioteca Python Utilizada

```
from random import randint
```
![Biblioteca](https://github.com/ThiagoLozano/Chutando-Um-Numero/blob/master/Screenshot/Biblioteca.PNG)
