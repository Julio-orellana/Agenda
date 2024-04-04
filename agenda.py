#Importar todo el contenido del modulo main
from main import *

#---------------------------------------------------------------------------------------

#Programa principal

#---------------------------------------------------------------------------------------
def main():
    while True:
        if menu_principal():
            choice = input("Ingrese una opcion: ")
            if choice ==  "1":
                    Agenda.ingresarDato()
        else:
            break

#---------------------------------------------------------------------------------------
#Cerrar conexión
conn.close()