import time

class Loops():

    def loopIF(self):
        k = int(input('Digite um número que esteja entre 0 e 20: '))

        if k > 10:
            print(f'{k} é maior do que 10')
        elif k == 10:
            print(f'{k} é igual a 10')
        else:
            print(f'{k} é menor do que 10')

    def LoopFOR(self):
        frase = input('Digite uma frase/palavra: ')

        for i in frase:
            print(i)

    def LoopWhile(self):
        i = 0
        max = int(input(('Você deseja contar quantos segundos?')))

        while i < max:
            print(i)
            time.sleep(1.0)
            i = i+1
