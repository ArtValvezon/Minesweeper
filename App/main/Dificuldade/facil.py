from Dificuldade.dificuldade import Dificuldade

class Facil(Dificuldade):
    def __init__(self):
        super().__init__(linhas=9, colunas=9, bombas=10)

    def getDificuldade(self):
        return "Facil"