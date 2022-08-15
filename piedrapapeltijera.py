
from ast import While
from random import randint
import pyfiglet
from pyfiglet import Figlet

bienvenida = pyfiglet.figlet_format("ELIJA SU JUGADA!", font="chunky")
adios = pyfiglet.figlet_format("BYE BYE!", font="chunky")
vs = pyfiglet.figlet_format("vs", font="chunky")
separador = pyfiglet.figlet_format("00000000000", font="chunky")
separador2 = pyfiglet.figlet_format("------------", font="bubble")

uno = pyfiglet.figlet_format("1_ Piedra", font="chunky")
dos = pyfiglet.figlet_format("2_ Papel", font="chunky")
tres = pyfiglet.figlet_format("3_ Tijeras", font="chunky")

piedra = pyfiglet.figlet_format("PIEDRA", font="chunky")
papel = pyfiglet.figlet_format("PAPEL", font="chunky")
tijeras = pyfiglet.figlet_format("TIJERAS", font="chunky")

gano = pyfiglet.figlet_format("ganaste :)", font="chunky")
perdio = pyfiglet.figlet_format("perdiste :(", font="chunky")
empato = pyfiglet.figlet_format("empate :|", font="chunky")

def jugar(jugada, contra):

    if jugada == 1:
        print(piedra)
    elif jugada == 2:
        print(papel)
    elif jugada == 3:
        print(tijeras)  

    print(vs)

    if contra == 1:
        print(piedra)
    elif contra == 2:
        print(papel)
    elif contra == 3:
        print(tijeras)   


    if jugada == 1 and contra == 2:
        print(perdio)

    elif jugada == 2 and contra == 2:
        print(empato)

    elif jugada == 3 and contra == 2:
        print(gano)

    elif jugada == 1 and contra == 1:
        print(empato)

    elif jugada == 2 and contra == 1:
        print(gano)

    elif jugada == 3 and contra == 1:
        print(perdio)

    elif jugada == 1 and contra == 3:
        print(gano)

    elif jugada == 2 and contra == 3:
        print(perdio)

    elif jugada == 3 and contra == 3:
        print(empato)

    else:
        print("laksjf")


while True:

    print(bienvenida)
    print(uno)
    print(dos)
    print(tres)
    print(separador)
    

    jugar(int(input(" ")), randint(1,3))

    jugar_nuevamente = input("Jugar nuevamente (s/n)... ")
    if jugar_nuevamente != "s":
        print(adios)
        break

