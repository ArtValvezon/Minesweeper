import random
from celula import Celula
from Interface.subject import Subject
from controle import Controle
from BombaExplodiuException import BombaExplodiuException

# random.seed(42) 

class Tabuleiro(Subject):
    def __init__(self, controle: Controle, linhas = 9, colunas = 9, bombas = 10):     #facil 9 x 9 10 bombas
        Subject.__init__(self, name="Tabuleiro")
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.tabuleiro = None
        self.controle = controle
        self.setTabuleiro()
        
    def getDimensoes(self)-> tuple[int, int]:
        """ Retorna dimensões do tabuleiro

        Returns:
            tuple[int, int]: (x, y)
        """
        return self.linhas, self.colunas
    
    def imprimirMatriz(self):
        matriz = self.tabuleiro
        for linha in matriz:
            print(" ".join(str(valor.getValor()) for valor in linha))

    def getRandom_Matrix(self)-> list[list[bool]]:
        """ Cria uma matriz com a quantidade de bombas espalhadas pelo tabuleiro

        Returns:
            list[list[bool]: matriz onde bomba = True
        """

        matriz = [[False for _ in range(self.colunas)] for _ in range(self.linhas)]
        posicoes = random.sample([(i, j) for i in range(self.linhas) for j in range(self.colunas)], self.bombas)

        for i, j in posicoes:
            matriz[i][j] = True

        return matriz

    def setTabuleiro(self)-> None:
        """ Cria matriz com as celulas com os valores de obmbas ao redor
        """

        if self.tabuleiro:
            del self.tabuleiro

        matriz =  self.getRandom_Matrix()

        tabuleiro = [[9 for _ in range(self.colunas)] for _ in range(self.linhas)]

        for i in range(self.linhas):
            for j in range(self.colunas):
                if not matriz[i][j]:
                    tabuleiro[i][j]  = self.contarVizinhos(matriz, i, j)
                tabuleiro[i][j] = Celula(self.controle, tabuleiro[i][j])
                tabuleiro[i][j].adicionarTabuleito(self)

        for i in range(self.linhas):
            for j in range(self.colunas):
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue  

                        ni, nj = i + di, j + dj

                        if 0 <= ni < self.linhas and 0 <= nj < self.colunas:
                            tabuleiro[i][j].adicionarObserver(tabuleiro[ni][nj])

        self.tabuleiro = tabuleiro

    def abrirCelula(self, i: int, j: int)-> None:
        """ Abre celula correspondete

        Args:
            i (int): coordenada x
            j (int): coordenada y
        """

        if 0 <= i < self.linhas and 0 <= j < self.colunas:
            try:
                self.tabuleiro[i][j].abrir()
            except BombaExplodiuException:
                self.notificarObserver()

    def getValor(self, i: int, j: int)-> int:
        """ Retorna o valor da celula 

        Args:
            i (int): coordenada x
            j (int): coordenada y
        """
        return self.tabuleiro[i][j].getValor()

    
    def flagCelula(self, i: int, j: int)-> None:
        """ Set flag na celula correspondente

        Args:
            i (int): coordenada x
            j (int): coordenada y
        """

        if 0 <= i < self.linhas and 0 <= j < self.colunas:
            self.tabuleiro[i][j].setFlag()
    
    def contarVizinhos(self, matriz: list[list[bool]], i: int, j: int)-> int:
        """ Conta quantas celulas de bomba existe ao redor da celula

        Args:
            matriz (list[list[bool]]): matiz booleana
            i (int): coordenada x
            j (int): coordenada y

        Returns:
            int: quantidade de bombas
        """

        linhas = len(matriz)
        colunas = len(matriz[0])
        contador = 0

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  

                ni, nj = i + di, j + dj

                if 0 <= ni < linhas and 0 <= nj < colunas:
                    if matriz[ni][nj]:
                        contador += 1
        return contador
    
    def abrirTabuleiro(self)-> None:
        """ Abre todas as celulas do tabuleiro
        """

        for i in range(self.linhas):
            for j in range(self.colunas):
                self.tabuleiro[i][j].abrir(False)

    def setCelulas(self)-> None:
        """ Marca as celulas como bombas
        """

        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.tabuleiro[i][j] == 9:
                    self.celulas[i][j].bomba = True

    def notificarObserver(self)-> None:
        """ Notifica o comando de que o jogo acabou
        """

        for observer in self.observer:
            observer.update("perdeu")

if __name__ == "__main__":
    Tabuleiro1 = Tabuleiro()
    while True:
        Tabuleiro1.imprimirMatriz()
        entrada = input("Digite dois números separados por espaço: ")
        num1, num2 = map(int, entrada.split())
        result = Tabuleiro1.flagCelula(num1, num2)

    Tabuleiro1.abrirTabuleiro()
    Tabuleiro1.imprimir_matriz()
    print("Fim do jogo!")