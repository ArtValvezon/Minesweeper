from Interface.singleton import Singleton
from controle import Controle
from Dificuldade import Facil, Medio, Dificil
from tabuleiro import Tabuleiro
from Interface.observer import Observer

class Comando(Singleton, Observer):

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.dificuldade = Facil() 
        return cls._instancia
    
    def __init__(self):
        Observer.__init__(self)
        Singleton.__init__(self)
        self.criarJogo()

    def criarJogo(self)-> None:
        """ inicializa o tabuleiro e controle de celulas com a dificuldade definida
        """

        self.linhas = self.dificuldade.getLinha()
        self.colunas = self.dificuldade.getColuna()
        self.bombas = self.dificuldade.getBombas()
        self.controle = Controle(casas=self.linhas * self.colunas, bombas=self.bombas)
        self.controle.adicionarObserver(self)
        self.tabuleiro = Tabuleiro(self.controle, self.linhas, self.colunas, self.bombas)
        self.tabuleiro.adicionarObserver(self)
        self.estado = "jogando"

    def getControle(self)-> Controle:
        return self.controle
    
    def getTabuleiro(self)-> Tabuleiro:
        return self.tabuleiro
    
    def getEstado(self)-> str:
        return self.estado

    def setDificuldade(self, dificuldade)-> None:
        if dificuldade == "facil":
            self.dificuldade = Facil()
        elif dificuldade == "medio":
            self.dificuldade = Medio()
        elif dificuldade == "dificil":
            self.dificuldade = Dificil()
        else:
            raise ValueError("Dificuldade inválida")

        self.criarJogo()

    def reset(self)-> None:
        """ Reseta o tabuleiro e controle com a mesma dificldade
        """

        self.tabuleiro.setTabuleiro()
        self.controle.reset()
        self.estado = "jogando"

    def terminarJogo(self, estado: str)-> None:
        """ Termina o jogo e abre o tabuleiro

        Args:
            estado (str): estado do jogo
        """

        self.tabuleiro.abrirTabuleiro()
        self.estado = estado

    def update(self, estado: str)-> None:
        """ Recebe a notificação dos Subject que a classe observa

        Args:
            estado (str): estado do jogo
        """

        if estado == "reset":
            self.reset()
        else:
            self.terminarJogo(estado)

