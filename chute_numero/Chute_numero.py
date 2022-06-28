from random import randint


class ChuteNumero():
    def __init__(self) -> None:
        self.valor_aleatorio = 0
        self.valor_maximo = 100
        self.valor_minimo = 1
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarAleatorio()
        self.PedirValor()
        try:
            while self.tentar_novamente == True:
                if self.valor_chute > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.PedirValor()
                elif self.valor_chute < self.valor_aleatorio:
                    print('chute valor mais alto')
                    self.PedirValor()
                elif self.valor_chute == self.valor_aleatorio:
                    print('Parabéns você acertou!')
                    self.tentar_novamente = False
        except:
            print('Digitar somente números inteiros!!')

    def PedirValor(self):
        try:
            self.valor_chute = int(input('Chute um número \n>> '))
        except:
            print('Digitar somente números inteiros!!')

    def GerarAleatorio(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)


jogar = ChuteNumero()
jogar.Iniciar()
