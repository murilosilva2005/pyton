import math


class Operacao:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)  # utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível Dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f' \n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio1(self):
        msg = ""
        for i in range(1, 11,1):
            msg += F'\n{i}'
        return msg

    def exercicio2(self): #2
        pares = ""
        for i in range(1, 21,1):
            if i % 2 == 0:
                pares+= f'\n{i}'
        return pares

    def exercicio3(self): #3
            for i in range(1, 101,1):
                soma += i

    def exercicio4(self): #4
        multiplos = ""
        for i in range(1, 51,1):
            if i % 5 == 0:
                multiplos+=f'\n{i}'
        return multiplos

    def exercicio5(self, num):
        if num % 2 == 0:
            return "Par"
        else:
            return "ìmpar"

    def exercicio6(self, num):
        if num < 0:
            return ("O número é negativo.")
        else:

            return("O número é positivo.")

    def exercicio7(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f' \n{num1} * {i} = {num1 * i}'


     def exercicio8(self, num):
        if num < 0:
            return "O número é negativo."
        else:
        for i in range(1, num + 1):
                print(i)
            return "O número é positivo."


     def exercicio10(self, num):
        if num < 0:
            return "O número é negativo."
        else:
            if (num):
                return f"{num} é um número primo."
            else:
                return f"{num} não é um número primo."


    def exercicio11(self):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True



    def exercicio12(self):
        if self.numero == 0 or self.numero == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, self.numero + 1):
                resultado *= i
            return resultado
