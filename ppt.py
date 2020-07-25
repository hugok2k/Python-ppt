import random
import os

started = True
ppt = ["PIEDRA", "PAPEL", "TIJERA"]
os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    print('''+----------------------------------------------------------+
| Hola, bienvenido y bievenida a piedra, papel o tijera.   |
+----------------------------------------------------------+
| La piedra aplasta la tijera. (GANA la piedra.)           |
| La tijera corta el papel. (GANA la tijera.)              |
| El papel envuelve la piedra. (GANA el papel.)            |
+----------------------------------------------------------+''')
    print(
        "| "+"\033[32m"+"PARA TERMINAR EL JUEGO ESCRIBE >SALIR<.                  "+"\033[37m"+"|")
    print("+----------------------------------------------------------+")


welcome()


def game():
    global userInput
    global randomPpt
    print("\033[37m"+"")
    userInput = input("Escribe piedra, papel o tijera: >> ").upper()
    check(userInput)


while started == True:
    def check(userInput):
        global randomPpt
        global started
        randomPpt = random.choice(ppt)
        if userInput == randomPpt:
            print("Empataron, la computadora tambien eligio "+randomPpt)
        elif userInput == "PIEDRA" and randomPpt == "PAPEL":
            print("Perdiste, la computadora eligio "+"\033[1;31m"+randomPpt)
        elif userInput == "PIEDRA" and randomPpt == "TIJERA":
            print("Ganaste, la computadora eligio "+"\033[1;32m"+randomPpt)
        elif userInput == "PAPEL" and randomPpt == "TIJERA":
            print("Perdiste, la computadora eligio "+"\033[1;31m"+randomPpt)
        elif userInput == "PAPEL" and randomPpt == "PIEDRA":
            print("Ganaste, la computadora eligio "+"\033[1;32m"+randomPpt)
        elif userInput == "TIJERA" and randomPpt == "PIEDRA":
            print("Perdiste, la computadora eligio "+"\033[1;31m"+randomPpt)
        elif userInput == "TIJERA" and randomPpt == "PAPEL":
            print("Ganaste, la computadora eligio "+"\033[1;32m"+randomPpt)
        elif userInput.startswith('S'):
            started = False
    game()
