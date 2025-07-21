import tkinter as tk

ligado = 'red'
desligado = 'gray20'
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

    def __init__(self, root, cor_ativa=ligado):
        self.cor_ativa = cor_ativa
        self.canvas = tk.Canvas(root, width=28, height=56, bg='black')
        self.canvas.pack()

        desligado = "#4D0404"  # Cor cinza escuro para os segmentos desligados

        # Cada segmento é desenhado como um trapezoide
        self.segmentos = {
            'A': self.canvas.create_polygon(5, 3, 26, 3, 19, 8, 10, 8, fill=desligado),
            'B': self.canvas.create_polygon(28, 5, 28, 28, 23, 23, 23, 10, fill=desligado),
            'C': self.canvas.create_polygon(28, 31, 28, 54, 23, 49, 23, 36, fill=desligado),
            'D': self.canvas.create_polygon(5, 56, 26, 56, 19, 51, 10, 51, fill=desligado),
            'E': self.canvas.create_polygon(3, 31, 3, 54, 8, 49, 8, 36, fill=desligado),
            'F': self.canvas.create_polygon(3, 5, 3, 28, 8, 23, 8, 10, fill=desligado),
            'G': self.canvas.create_polygon(7, 28, 24, 28, 19, 33, 10, 33, fill=desligado),
        }

    def mostrar_numero(self, numero):
        numero = str(numero)
        segmentos_ativos = self.mapa_segmentos.get(numero, '')
        for nome, segmento in self.segmentos.items():
            cor = self.cor_ativa if nome in segmentos_ativos else desligado
            self.canvas.itemconfig(segmento, fill=cor)


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Display 7 Segmentos - Trapezoide")

    display = Display7Segmentos(root, cor_ativa='lime')

    entrada = tk.Entry(root)
    entrada.pack()

    def atualizar_display():
        numero = entrada.get()
        if numero.isdigit() and 0 <= int(numero) <= 9:
            display.mostrar_numero(numero)
        else:
            print("Digite um número de 0 a 9.")

    btn = tk.Button(root, text="Mostrar", command=atualizar_display)
    btn.pack()

    root.mainloop()
