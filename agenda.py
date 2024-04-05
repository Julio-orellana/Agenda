#Importar el modulo del proyecto
from main import *

#---------------------------------------------------------------------------------------

#RECUERDEN NO UTILIZAR EL MISMO NOMBRE DE VARIABLES GLOBALES DE AGENDA O DE MAIN A MENOS QUE SE DESEE REESCRIBIR SU VALOR

#Programa principal

#---------------------------------------------------------------------------------------
def main():
    flujo = True
    while True:
        if not menu_principal():
            break  # Salir del bucle si el inicio de sesión no es exitoso
        print('''''')# Se deben imprimir las posibles opciones de la agenda
        opcion = input("Ingrese una opcion: ")
        while flujo:
            if opcion == "1": #Opcion 1 ingresa una tarea a la agenda
                fecha = input("Ingrese la fecha: ")
                tarea = input("Ingrese la descripción de la tarea: ")
                Agenda.ingresarTarea(fecha, tarea)
            else:
                flujo = False
                
#Ejecutar el programa
main()

#---------------------------------------------------------------------------------------
# Cerrar conexión a la base de datos data
conn.close()