from comando import Comando
from GUI.Interface import Interface

def main():
    comando = Comando()

    while True:
        tabuleiro = comando.getTabuleiro()
        controle = comando.getControle()

        interface = Interface(tabuleiro, controle)
        interface.adicionarObserver(comando)
        valor = interface.run()
        if valor == 0:
            break

if __name__ == "__main__":
    main()