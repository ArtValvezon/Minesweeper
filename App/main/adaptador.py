from Interface.singleton import Singleton
from tabuleiro import Tabuleiro
from controle import Controle

class Adaptador(Singleton):
    def __init__(self, controle: Controle, tabuleiro: Tabuleiro):
        super().__init__()
        self.tabuleiro = tabuleiro
        self.controle = controle

    def setComando(self, comando)-> None:
        self.comando = comando

    def getDimensoes(self)-> tuple[int, int]:
        return self.tabuleiro.getDimensoes()

    def getValor(self, i, j)-> int:
        return self.tabuleiro.getValor(i, j)

    def abrirCelula(self, i: int, j: int)-> None:
        self.tabuleiro.abrirCelula(i, j)

    def flagCelula(self, i: int, j: int)-> None:
        self.tabuleiro.flagCelula(i, j)

    def getBombas(self) -> int:
        return self.controle.getBombas()

    def getCasas(self)-> int:
        return self.controle.getCasas()

    def setDificuldade(self, dificuldade: str)-> None:
        self.comando.setDificuldade(dificuldade)

    def reset(self)-> None:
        self.comando.reset()

    def getEstado(self)-> str:
        return self.comando.getEstado()

    