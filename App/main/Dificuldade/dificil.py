from Dificuldade.dificuldade import Dificuldade

class Dificil(Dificuldade):
    def __init__(self):
        super().__init__(linhas=16, colunas=30, bombas=99)

    def getDificuldade(self):
        return "Dificil"