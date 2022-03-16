#Nombre de autores: Cristobal Galindo y Javier Rehbein
#Curso: Lenguaje de programacion 2022
#Nombre de Profesor: Cristhian Aguilera
#Fecha: 16/03/2022


import typer
import time
from random import seed
from random import randint


app = typer.Typer()
seed(time.time())


def get_random_number(max_number: int = 100) -> int:
    """
    Generates a random number

    Parameters
    ----------
    max_number : int
       Maximun possible of the random number

    Returns
    -------
    int
        randon number
    """
    return randint(0, max_number)


@app.command()
def guess_the_number():
    """
    Guess number game
    """
    # -----------------------------------
    # Add your code here
    print("\n             BIENVENIDO A THE GAME\n Las instrucciones del juego son las siguientes:\n 1-THE GAME escogera una posicion al azar entre 1 y 100.\n 2-Debes adivinar donde esta escondido el secreto escondido de THE GAME.\n 3-El juego te señalara si la posicion que escogiste es MAYOR o MENOR donde esta oculto el secreto.\n 4-¡¡¡Empieza a jugar!!! ")
    random = get_random_number()
    #print(f"{random}")

    num_us = int(input("Introduzca una coodenada que crea ser la correcta: \n"))
    print(f"Su primera posicion es:{num_us} \n")

    while num_us != random:

         if(num_us < random):
            print(f"Tu posicion actual es MENOR de donde está la ubicacion \n")
            num_us = int(input("Introduzca otra posicion:\n"))
         else:
             print(f"Tu posicion actual es MAYOR de donde está la ubicacion \n")
             num_us = int(input("Introduzca otra posicion: \n"))
    
    pass
    print(f"\n Has llegado a la ubicacion \n")
    print(f"¡¡¡ Encontraste un Tesoro !!!\n")
    print(f"¡¡¡ Ganaste OwO, eres muy genial !!!\n")


    pass
    # -----------------------------------
    # End
    # -----------------------------------


def main():
    app()


if __name__ == '__main__':
    main()
