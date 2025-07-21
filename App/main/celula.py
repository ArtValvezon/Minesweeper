from Interface.observer import Observer
from Interface.subject import Subject


class Celula(Subject, Observer):
    def __init__(self, controle, valor=0):
        self.aberto = False
        self.flag = False
        self.explodiu = False
        self.valor = valor
        self.observer = []
        self.controle = controle

    def update(self):
        self.abrir()

    def adicionarTabuleito(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def notificarTabuleiro(self):
        if self.tabuleiro:
            self.tabuleiro.notificarObserver()

    def abrir(self, jogo= True):
        if jogo:
            if not self.flag:
                if self.aberto:
                    self.abrirAdjacentes()
                    return False
                self.aberto = True
                self.controle.abreCasa()
                if self.valor == 9:
                    self.explodiu = True
                    self.notificarTabuleiro()
                    return True
                if self.valor == 0:
                    self.notificarObserver()
        else:
            self.aberto = True
        return False
    
    def setFlag(self):
        if not self.aberto:
            if self.flag:
                if self.controle.removeFlag():
                    self.flag = not self.flag
                    return True
            else:
                if self.controle.adicionaFlag():
                    self.flag = not self.flag
                    return True
        return False
    
    def getValor(self):
        if self.explodiu:
            return "E"
        if self.aberto:
            return self.valor if self.valor != 9 else "B"
        elif self.flag:
            return "F"
        else:
            return "X"
        
    def abrirAdjacentes(self):
        if self.valor == 0:
            return
        i = 0
        for observer in self.observer:
            if observer.getValor() == "F":
                i += 1
        if i == self.valor:
             for observer in self.observer:
                if not observer.aberto:
                    observer.abrir()
                        

    
