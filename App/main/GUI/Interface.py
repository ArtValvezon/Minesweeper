from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from adaptador import Adaptador
from Interface.subject import Subject
from GUI.display import Display
from TrocarDificuldadeException import TrocarDificuldadeException
from FimdeJogoException import FimdeJogoException
from datetime import datetime




altura_sombra = 4
altura_bordas = 32
altura_celula = 32
cinza_claro = '#C0C0C0'
cinza_medio = '#BDBDBD'
cinza_escuro = '#808080'

class Interface():
    def __init__(self, adaptador: Adaptador):
        self.flag = False
        self.root = Tk()
        self.root.title("Campo Minado")
        self.root.iconbitmap("Imagens/bomb_icon.ico")

        self.adaptador = adaptador
        self.linhas, self.colunas = adaptador.getDimensoes()
        

        self.largura_root = self.colunas * altura_celula + altura_bordas * 2
        self.altura_root = self.linhas * altura_celula + altura_bordas * 5 
        self.root.geometry(f"{self.largura_root}x{self.altura_root}")
        self.root.configure(bg=cinza_medio)
        self.root.resizable(False, False)
        self.imagens = {
            0: PhotoImage(file="Imagens/number_0.png"),
            1: PhotoImage(file="Imagens/number_1.png"),
            2: PhotoImage(file="Imagens/number_2.png"),
            3: PhotoImage(file="Imagens/number_3.png"),
            4: PhotoImage(file="Imagens/number_4.png"),
            5: PhotoImage(file="Imagens/number_5.png"),
            6: PhotoImage(file="Imagens/number_6.png"),
            7: PhotoImage(file="Imagens/number_7.png"),
            8: PhotoImage(file="Imagens/number_8.png"),
            'B': PhotoImage(file="Imagens/bomb.png"),
            'F': PhotoImage(file="Imagens/flag.png"),
            'E': PhotoImage(file="Imagens/bomb_exploded.png"),
            'X': PhotoImage(file="Imagens/empty_cell.png"),
            "jogando": PhotoImage(file="Imagens/smiley-face.png"),
            "perdeu": PhotoImage(file="Imagens/dead-face.png"),
            "ganhou": PhotoImage(file="Imagens/cool-face.png")
        }
        self.criarFrames()
        self.criarBotoes()
        self.criarMenu()
        self.criarPlacar()

    def run(self)-> bool:
        """ Inicia o main loop da root

        Returns:
            bool: caso tenha sido reiniciado retorna True
        """

        self.root.mainloop()
        if self.flag:
            raise TrocarDificuldadeException
        raise FimdeJogoException
    
    def stop(self)-> None:
        """ Cancela a GUI e marca flag como True
        """

        
        self.root.destroy()
        self.flag = True

    def getCell_Image(self, i: int, j: int)-> Image:
        """ Retorna a imagem correspondente ao conteudo da celula

        Args:
            i (int): coordenada x
            j (int): coordenada y

        Raises:
            ValueError: caso uma celula retorne um valor incorreto

        Returns:
            Image: tkinter image
        """

        value = self.adaptador.getValor(i, j)
        if value in self.imagens:
            return self.imagens[value]
        else:
            raise ValueError(f"Valor inválido para a célula: {value}")

    def criarFrames(self)-> None:
        """ Cria as bordas da aplcação com todos os efeitos de luz e sombra
        """

        def get_sombra_horizontal(largura)-> Frame:
            return Frame(self.root,
                        width= largura,
                        height=altura_sombra,
                        bg=cinza_escuro)

        def get_sombra_vertical(altura)-> Frame:
            return Frame(self.root,
                        width=altura_sombra,
                        height=altura,
                        bg=cinza_escuro)

        def get_luz_horizontal(largura)-> Frame:
            return Frame(self.root,
                        width= largura,
                        height=altura_sombra,
                        bg='white')

        def get_luz_vertical(altura)-> Frame:
            return Frame(self.root,
                        width=altura_sombra,
                        height=altura,
                        bg='white')

        def get_horizontal_frame()-> Frame:
            return Frame(self.root,
                        width= self.largura_root - (altura_bordas * 2),
                        height=altura_bordas,
                        bg=cinza_claro)

        def get_vertical_frame()-> Frame:
            return Frame(self.root,
                        width=altura_bordas,
                        height=self.altura_root,
                        bg=cinza_claro)

        get_horizontal_frame().place(x=altura_bordas, y=0)
        get_horizontal_frame().place(x=altura_bordas, y=altura_bordas * 3)
        get_horizontal_frame().place(x=altura_bordas, y=self.altura_root - altura_bordas)

        get_vertical_frame().place(x=0, y=0)
        get_vertical_frame().place(x=self.largura_root - altura_bordas, y=0)

        get_luz_horizontal(self.largura_root).place(x=0, y=0)
        get_sombra_horizontal(self.largura_root - altura_bordas * 2 + altura_sombra * 2).place(x=altura_bordas - altura_sombra, y= altura_bordas - altura_sombra)

        get_luz_horizontal(self.largura_root - altura_bordas * 2 + altura_sombra * 2).place(x=altura_bordas - altura_sombra, y=altura_bordas*3)
        get_sombra_horizontal(self.largura_root - altura_bordas * 2 + altura_sombra * 2).place(x=altura_bordas - altura_sombra, y= altura_bordas * 4 - altura_sombra)

        get_luz_horizontal(self.largura_root - altura_bordas * 2 + altura_sombra * 2).place(x=altura_bordas - altura_sombra, y=self.altura_root - altura_bordas)
        get_sombra_horizontal(self.largura_root).place(x=0, y= self.altura_root - altura_sombra)

        get_luz_vertical(self.altura_root).place(x=0, y=0)
        get_sombra_vertical(self.altura_root).place(x=self.largura_root - altura_sombra, y=0)

        get_sombra_vertical(altura_bordas * 2 + altura_sombra * 2).place(x=altura_bordas - altura_sombra, y=altura_bordas - altura_sombra)
        get_luz_vertical(altura_bordas * 2 + altura_sombra * 2).place(x=self.largura_root - altura_bordas, y=altura_bordas - altura_sombra)

        get_sombra_vertical(self.altura_root - 5 * altura_bordas + 2 * altura_sombra).place(x=altura_bordas - altura_sombra, y=altura_bordas * 4 - altura_sombra)
        get_luz_vertical(self.altura_root - 5 * altura_bordas + 2 * altura_sombra).place(x=self.largura_root - altura_bordas, y=altura_bordas * 4 - altura_sombra)

    def cliqueEsquerdo(self, event, i: int, j: int)-> None:
        """ Clique com o botão esquerdo em alguma celula

        Args:
            i (int): coordenada x
            j (int): coordenada y
        """

        self.adaptador.abrirCelula(i, j)
        self.atualizarBotoes()

    def cliqueDireito(self, event, i: int, j: int)-> None:
        """ Clique com o botão direito em alguma celula

        Args:
            i (int): coordenada x
            j (int): coordenada y
        """

        self.adaptador.flagCelula(i, j)
        self.atualizarBotoes()

    def atualizarBotoes(self)-> None:
        """ Atualiza todos os botões e placar para mostrar as casas abertas 
        """
        for i in range(self.linhas):
            for j in range(self.colunas):
                nova_imagem = self.getCell_Image(i, j)
                self.botoes[i][j].configure(image=nova_imagem)
                self.botoes[i][j].image = nova_imagem

        self.atualizarPlacar(self.adaptador.getBombas(), self.adaptador.getCasas())

    def criarMenu(self)-> None:
        """ Cria a barra de menu com os menus adicionais
        """

        def setDificuldade(dificuldade)-> None:
            self.adaptador.setDificuldade(dificuldade)
            self.stop()

        menu = Menu(self.root)

        menuAjuda = Menu(menu, tearoff=0)
        menuAjuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Este é um exemplo de menu Tkinter."))
        menuAjuda.add_separator()
        menuAjuda.add_command(label="Regras", command=lambda: messagebox.showinfo("Regras", regras))
        menu.add_cascade(label="Ajuda", menu=menuAjuda)

        menuArquivo = Menu(menu, tearoff=0)
        menuArquivo.add_command(label="Fácil", command=lambda: setDificuldade("facil"))
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Médio", command=lambda: setDificuldade("medio"))
        menuArquivo.add_separator()
        menuArquivo.add_command(label="Difícil", command=lambda: setDificuldade("dificil"))
        menu.add_cascade(label="Dificuldade", menu=menuArquivo)

        self.root.config(menu=menu)


    def criarBotoes(self)-> None:
        """ Cria um botão com imagem para cada celula do tabuleiro
        """

        self.botoes = []

        frame_tabuleiro = Frame(self.root, bg=cinza_claro)
        frame_tabuleiro.place(x=altura_bordas, y=altura_bordas * 4, width=altura_celula * self.colunas, height=altura_celula * self.linhas)
        frame_tabuleiro.grid_propagate(False)
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                btn = Button(frame_tabuleiro,
                            image=self.getCell_Image(i, j),
                            width=32,
                            height=32,
                            bd=0,      
                            highlightthickness=0,  
                            padx=0, pady=0,  
                            relief="flat" 
                                )
                btn.grid(row=i, column=j)

                btn.bind("<Button-1>", lambda event, i=i, j=j: self.cliqueEsquerdo(event, i, j))
                btn.bind("<Button-3>", lambda event, i=i, j=j: self.cliqueDireito(event, i, j))

                linha.append(btn)
            self.botoes.append(linha)

    def resetDisplay(self)-> None:
        """ Desliga todos os segmentos dos placares
        """

        self.display_Bomb_Centena.limpar()
        self.display_Bomb_Dezena.limpar()   
        self.display_Bomb_Unidade.limpar()
        self.display_Casa_Centena.limpar()
        self.display_Casa_Dezena.limpar()
        self.display_Casa_Unidade.limpar()

    def criarPlacar(self)-> None:
        """ Cria os placares de 7 segmentos e o botão de reset com emoji
        """

        def reset()-> None:
            self.adaptador.reset()
            self.atualizarBotoes()
            self.resetDisplay()

        ligado = 'red'
        self.display_Bomb_Centena = Display(self.root, cor_ativa=ligado, x=altura_bordas + 3, y=altura_bordas + 3)
        self.display_Bomb_Dezena = Display(self.root, cor_ativa=ligado, x=altura_bordas + 31, y=altura_bordas + 3)
        self.display_Bomb_Unidade = Display(self.root, cor_ativa=ligado, x=altura_bordas + 59, y=altura_bordas + 3)

        self.display_Casa_Centena = Display(self.root, cor_ativa=ligado, x=self.largura_root - (altura_bordas + 88), y=altura_bordas + 3)
        self.display_Casa_Dezena = Display(self.root, cor_ativa=ligado, x=self.largura_root - (altura_bordas + 60), y=altura_bordas + 3)
        self.display_Casa_Unidade = Display(self.root, cor_ativa=ligado, x=self.largura_root - (altura_bordas + 32), y=altura_bordas + 3)

        self.face = Button(self.root, image=self.imagens["jogando"], bd=0, highlightthickness=0, padx=0, pady=0, relief="flat", command=reset)
        self.face.place(x=(self.largura_root - 31) // 2, y=altura_bordas + 15)

    def getLog(self)-> None:

        janela = Toplevel(self.root)

        notebook = ttk.Notebook(janela)
        notebook.pack(fill='both', expand=True)

        aba1 = Frame(notebook)
        notebook.add(aba1, text="Histórico")

        def getHistorico()-> str:
            with open("App/teste/arquivo.txt", "r", encoding="utf-8") as f:
                conteudo = f.read()
                return conteudo
            
        def setHistorico(texto: str)-> None:
            with open("App/teste/arquivo.txt", "a", encoding="utf-8") as f:
                agora = datetime.now().strftime("%d/%m/%Y")
                dificuldade = self.adaptador.getDificuldade()
                pontos = "." * (25 - len(texto) - len(dificuldade))
                escrever = f"\n{texto}{pontos}{dificuldade}...{agora}"
                f.write(escrever)
                fecharJanela()

        def clearHistorico()-> None:
            with open("App/teste/arquivo.txt", "w", encoding="utf-8") as f:
                f.truncate(0)
                fecharJanela()

        def fecharJanela()-> None:
            janela.destroy()

        Label(aba1, text=getHistorico()).pack(pady=10)
        Button(aba1, text="Limpar Historico", command=lambda: clearHistorico()).pack()

        aba2 = Frame(notebook)
        notebook.add(aba2, text="Cadastro")

        Label(aba2, text="Coloque seu nome aqui:").pack()
        comentario = Text(aba2, height=1, width=10)
        comentario.pack(pady=5)
        Button(aba2, text="Enviar", command=lambda: setHistorico(comentario.get("1.0", END).strip())).pack()

    def atualizarPlacar(self, bombas: int = 0, casas: int = 0)-> None:
        """ Atualiza os placares de pontuação com o numero de casas e bombas
        """

        bombas_str = str(bombas).zfill(3)
        casas_str = str(casas).zfill(3)

        self.display_Bomb_Centena.mostrarNumero(bombas_str[0])
        self.display_Bomb_Dezena.mostrarNumero(bombas_str[1])
        self.display_Bomb_Unidade.mostrarNumero(bombas_str[2])

        self.display_Casa_Centena.mostrarNumero(casas_str[0])
        self.display_Casa_Dezena.mostrarNumero(casas_str[1])
        self.display_Casa_Unidade.mostrarNumero(casas_str[2])

        self.face
        estado = self.adaptador.getEstado()
        if estado == "ganhou":
            self.getLog()
        nova_imagem = self.imagens[estado]
        self.face.configure(image=nova_imagem)
        self.face.image = nova_imagem

regras = """
Regras do Campo Minado
Campo Minado é um jogo de lógica onde o objetivo é abrir todas as células que não contêm minas, usando como pista os números que aparecem ao redor das células abertas — cada número indica quantas minas existem nas oito células adjacentes. O jogador usa o botão esquerdo do mouse para abrir células e o botão direito para marcar minas com bandeiras. Se abrir uma célula com mina, perde o jogo; se abrir todas as células seguras, vence. A primeira jogada é sempre segura, e o desafio está em deduzir a posição das minas com base na lógica dos números.
"""
