import tkinter as tk

ligado = 'red'
desligado = '#130101'
fundo = 'black'

class Display7Segmentos:
    mapa_segmentos = {
        '0': 'ABCDEF',
        '1': 'BC',
        '2': 'ABGED',
        '3': 'ABGCD',
        '4': 'FGBC',
        '5': 'AFGCD',
        '6': 'AFGCDE',
        '7': 'ABC',
        '8': 'ABCDEFG',
        '9': 'AFGBC',
    }

    def __init__(self, root, x: int=0, y: int=0, cor_ativa: str=ligado):
        """ Cria um display de 7 segmentos

        Args:
            root (_type_): root da interface tk
            x (int, optional): posição horizontal. Defaults to 0.
            y (int, optional): posição vertical. Defaults to 0.
            cor_ativa (str, optional): cor desejada. Defaults to '#130101'.
        """

        self.cor_ativa = cor_ativa
        self.canvas = tk.Canvas(root, width=29, height=58, bg='black', bd=0, highlightthickness=0)
        self.canvas.place(x=x, y=y)

        self.segmentos = {
            'A': self.canvas.create_polygon(4, 2, 25, 2, 18, 7, 9, 7, fill=desligado),
            'B': self.canvas.create_polygon(27, 4, 27, 27, 22, 22, 22, 9, fill=desligado),
            'C': self.canvas.create_polygon(27, 30, 27, 53, 22, 48, 22, 35, fill=desligado),
            'D': self.canvas.create_polygon(4, 55, 25, 55, 18, 50, 9, 50, fill=desligado),
            'E': self.canvas.create_polygon(2, 30, 2, 53, 7, 48, 7, 35, fill=desligado),
            'F': self.canvas.create_polygon(2, 4, 2, 27, 7, 22, 7, 9, fill=desligado),
            'G': self.canvas.create_polygon(6, 27, 23, 27, 18, 32, 9, 32, fill=desligado),
        }


    def mostrar_numero(self, numero: int):
        """ Revela o numero passado no display

        Args:
            numero (int): Numero a ser exibido
        """

        numero = str(numero)
        segmentos_ativos = self.mapa_segmentos.get(numero, '')
        for nome, segmento in self.segmentos.items():
            cor = self.cor_ativa if nome in segmentos_ativos else desligado
            self.canvas.itemconfig(segmento, fill=cor)

    def limpar(self):
        """ Desliga todos o segmentos do display
        """
        for segmento in self.segmentos.values():
            self.canvas.itemconfig(segmento, fill=desligado)