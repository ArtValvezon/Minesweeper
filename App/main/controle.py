from Interface.subject import Subject

class Controle(Subject):
    def __init__(self, casas = 81, bombas = 10):
        Subject.__init__(self, name="Controle")
        self.totalCasas = casas
        self.casas = casas
        self.bombas = bombas
        self.flag = 0
        

    def reset(self):
        self.casas = self.totalCasas
        self.flag = 0

    def adicionaFlag(self):
        if self.flag < self.bombas:
            self.flag += 1
            return True
        return False
    
    def removeFlag(self):
        if self.flag > 0:
            self.flag -= 1
            return True
        return False
    
    def abreCasa(self):
        self.casas -= 1
        if self.casas == self.bombas:
            self.notificarObserver()
            return True
    
    def notificarObserver(self):
        for observer in self.observer:
            observer.update("ganhou")

    def getCasas(self):
        return self.casas
    
    def getBombas(self):
        return self.bombas - self.flag