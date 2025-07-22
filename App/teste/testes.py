import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Historico")
root.geometry("200x300")

def criarHistorico(self)-> None:

    janela = tk.Toplevel(root)

    notebook = ttk.Notebook(janela)
    notebook.pack(fill='both', expand=True)

    # Criar a primeira aba (ex: Jogo)
    aba1 = tk.Frame(notebook)
    notebook.add(aba1, text="Histórico")

    dificuldade = 'facil'

    def getHistorico()-> str:
        with open("App/teste/arquivo.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
            return conteudo
        
    def setHistorico(texto: str)-> None:
        with open("App/teste/arquivo.txt", "a", encoding="utf-8") as f:
            pontos = "." * (25 - len(texto) - len(dificuldade))
            escrever = f"\n{texto}{pontos}{dificuldade}"
            f.write(escrever)
            fecharJanela()

    def clearHistorico()-> None:
        with open("App/teste/arquivo.txt", "w", encoding="utf-8") as f:
            f.truncate(0)
            fecharJanela()

    def fecharJanela()-> None:
        janela.destroy

    tk.Label(aba1, text=getHistorico()).pack(pady=10)
    tk.Button(aba1, text="Limpar Historico", command=lambda: clearHistorico()).pack()

    aba2 = tk.Frame(notebook)
    notebook.add(aba2, text="Cadastro")

    tk.Label(aba2, text="Coloque seu nome aqui:").pack()
    comentario = tk.Text(aba2, height=1, width=10)
    comentario.pack(pady=5)
    tk.Button(aba2, text="Enviar", command=lambda: setHistorico(comentario.get("1.0", tk.END).strip())).pack()

    with open("arquivo.txt", "a", encoding="utf-8") as f:
        f.write("\nNovo comentário adicionado.")

    root.mainloop()