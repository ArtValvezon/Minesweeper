from Dificuldade.dificuldade import Dificuldade

class Medio(Dificuldade):
    def __init__(self):
        super().__init__(linhas=16, colunas=16, bombas=40)

    def getDificuldade(self):
        return "Medio"