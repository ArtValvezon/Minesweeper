from Interface.observer import Observer
from Interface.subject import Subject


class Celula(Subject, Observer):
    def __init__(self, controle, valor: int=0):
        """ Cria objeto celula

        Args:
            controle (Controle): controle responsavel por armazanar as caracteristicas das celulas
            valor (int, optional): Valor de bombas da celula, 9 = bomba. Defaults to 0.
        """

        self.aberto = False
        self.flag = False
        self.explodiu = False
        self.valor = valor
        self.observer = []
        self.controle = controle

    def update(self)-> None:
        """ Celula adjacente abre essa
        """

        self.abrir()

    def adicionarTabuleito(self, tabuleiro)-> None:
        """ Adiciona um tabuleiro como observer 

        Args:
            tabuleiro (Tabuleiro): tabuleiro que a celula esta acossiada
        """
        
        self.tabuleiro = tabuleiro

    def notificarTabuleiro(self)-> None:
        """ Notifica o tabuleiro que uma celula foi explodida
        """

        if self.tabuleiro:
            self.tabuleiro.notificarObserver()

    def abrir(self, jogo= True)-> None:
        """ Abre celula 

        Args:
            jogo (bool, optional): Caso o jogo tenha terminado jogo = False. Defaults to True.
        """

        if jogo:
            if not self.flag:
                if self.aberto:
                    self.abrirAdjacentes()
                    return 
                self.aberto = True
                self.controle.abreCasa()
                if self.valor == 9:
                    self.explodiu = True
                    self.notificarTabuleiro()
                    return 
                if self.valor == 0:
                    self.notificarObserver()
        else:
            self.aberto = True
        return 
    
    def setFlag(self)-> None:
        """ Adiciona ou remove bandeira da celula
        """

        if not self.aberto:
            if self.flag:
                if self.controle.removeFlag():
                    self.flag = not self.flag
                    return 
            else:
                if self.controle.adicionaFlag():
                    self.flag = not self.flag
                    return 
        return 
    
    def getValor(self)-> any:
        """ Retorna o estado da celula

        Returns:
            Any: Estado da celula, F - flag, E - explodiu, B - bomba, int - valor
        """

        if self.explodiu:
            return "E"
        if self.aberto:
            return self.valor if self.valor != 9 else "B"
        elif self.flag:
            return "F"
        else:
            return "X"
        
    def abrirAdjacentes(self)-> None:
        """ Conta as flag para abrir as cellas adjacentes
        """
        
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
                        

    
