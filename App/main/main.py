from comando import Comando
from GUI.Interface import Interface
from adaptador import Adaptador
from TrocarDificuldadeException import TrocarDificuldadeException
from FimdeJogoException import FimdeJogoException

def main():
    comando = Comando()

    while True:
        try:
            tabuleiro = comando.getTabuleiro()
            controle = comando.getControle()

            adaptador = Adaptador(controle, tabuleiro)
            adaptador.setComando(comando)

            interface = Interface(adaptador)
            interface.run()
        except TrocarDificuldadeException:
            pass
        except FimdeJogoException:
            break

if __name__ == "__main__":
    main()