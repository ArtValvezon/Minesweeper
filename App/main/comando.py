from Interface.singleton import Singleton
from controle import Controle
from Dificuldade import Facil, Medio, Dificil
from tabuleiro import Tabuleiro
from Interface.observer import Observer

class Comando(Singleton, Observer):
    def __init__(self):
        Observer.__init__(self)
        Singleton.__init__(self)
        self.dificuldade = Facil() 
        self.criarJogo()

    def criarJogo(self):
        self.linhas = self.dificuldade.getLinha()
        self.colunas = self.dificuldade.getColuna()
        self.bombas = self.dificuldade.getBombas()
        self.controle = Controle(casas=self.linhas * self.colunas, bombas=self.bombas)
        self.controle.adicionarObserver(self)
        self.tabuleiro = Tabuleiro(self.controle, self.linhas, self.colunas, self.bombas)
        self.tabuleiro.adicionarObserver(self)
        self.estado = "jogando"

    def getControle(self):
        return self.controle
    
    def getTabuleiro(self):
        return self.tabuleiro
    
    def getEstado(self):
        return self.estado

    def setDificuldade(self, dificuldade):
        if dificuldade == "facil":
            self.dificuldade = Facil()
        elif dificuldade == "medio":
            self.dificuldade = Medio()
        elif dificuldade == "dificil":
            self.dificuldade = Dificil()
        else:
            raise ValueError("Dificuldade inválida")

        self.criarJogo()

    def reset(self):
        self.tabuleiro.setTabuleiro()
        self.controle.reset()
        self.estado = "jogando"

    def terminarJogo(self, estado):
        self.tabuleiro.abrirTabuleiro()
        self.estado = estado

    def update(self, estado):
        if estado == "reset":
            self.reset()
        else:
            self.terminarJogo(estado)

