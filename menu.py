from operacao import Operacao


class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Operacao()
        self.num = 0
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print("\n ---Menu---\n\n" +
              "Escolha uma das opções abaixo:" +
              "\n0. Sair" +
              "\n1.Somar" +
              "\n2.Subtrair" +
              "\n3.Dividir" +
              "\n4.Multiplicar" +
              "\n5.Potência" +
              "\n6.Raiz" +
              "\n7.Tabuada" +
              "\n8 potencia" +
              "\n9 exercicio1" +
              "\n10 exercicio2" +
              "\n11 exercicio3" +
              "\n12 exercicio4" +
              "\n13 exercicio5" +
              "\n14 exercicio6" +
              "\n15 exercicio7")








    def coletar(self):
        self.num1 = int(input('Informe o primeiro número:'))
        self.num2 = int(input('Informe o segundo número:'))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print("Obrigado!")
            if self.opcao == 1:
                self.coletar()  # chamando o input
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')

            elif self.opcao == 2:
                self.coletar()  # chamando o input
                print(f'A subtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()  # chamando o input
                print(f'A divisão dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()  # chamando o input
                print(f'A multiplicação dos números digitados é: {self.exer.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()  # chamando o input
                print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()  # chamando o input
                print(f'A raiz de {self.num1} digitado é: {self.exer.raiz(self.num1)}')

            elif self.opcao == 7:
                self.coletar()  # chamando o input
                print(f'A tabuada de {self.num1} digitado é: {self.exer.tabuada(self.num1)}')

            elif (self.opcao == 8):
                print(self.exer.potencia(base,expoente))

            elif (self.opcao == 9):
                print(self.exer.exercicio1())

            elif (self.opcao == 10):
                print(self.exer.exercicio2())

            elif(self.opcao == 11):
                print(self.exer.exercicio3())

            elif(self.opcao == 12):
                print(self.exer.exercicio4())

            elif (self.opcao == 13):
                num = int(input("Informe o primeiro número: "))
                print(self.exer.exercicio5(num))

            elif(self.opcao == 14):
                num = int(input("informe o primeiro número"))
                print(self.exer.exercicio6(num))

            elif(self.opcao == 15):
                num = int(input("informe o número"))
                print(f'A tabuada de {self.num} digitado é: {self.exer.exercicio7(self.num)}')


