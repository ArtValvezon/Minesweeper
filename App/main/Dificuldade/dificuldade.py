from abc import ABC, abstractmethod

class Dificuldade(ABC):
    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas

    def getBombas(self)-> int:
        return self.bombas
    
    def getLinha(self)-> int:
        return self.linhas
    
    def getColuna(self)-> int:
        return self.colunas

    @abstractmethod
    def getDificuldade(self)-> str:
        raise NotImplementedError("Subclasses should implement this method")