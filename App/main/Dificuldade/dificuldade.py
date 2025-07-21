from abc import ABC, abstractmethod

class Dificuldade(ABC):
    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas

    def getBombas(self):
        return self.bombas
    
    def getLinha(self):
        return self.linhas
    
    def getColuna(self):
        return self.colunas

    @abstractmethod
    def getDificuldade(self):
        raise NotImplementedError("Subclasses should implement this method")