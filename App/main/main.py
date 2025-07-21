from comando import Comando
from GUI.Interface import Interface
from adaptador import Adaptador

def main():
    comando = Comando()

    while True:
        tabuleiro = comando.getTabuleiro()
        controle = comando.getControle()

        adaptador = Adaptador(controle, tabuleiro)
        adaptador.setComando(comando)

        interface = Interface(adaptador)
        valor = interface.run()
        if valor == 0:
            break

if __name__ == "__main__":
    main()