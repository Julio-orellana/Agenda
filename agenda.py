#Importar el modulo del proyecto
from main import *

#---------------------------------------------------------------------------------------

#RECUERDEN NO UTILIZAR EL MISMO NOMBRE DE VARIABLES GLOBALES DE AGENDA O DE MAIN A MENOS QUE SE DESEE REESCRIBIR SU VALOR

#Programa principal

#---------------------------------------------------------------------------------------
def main():
    flujo = True
    while True:
        print("\n------------------------------------------------------------------")
        print(f"\n{date}")
        if not menu_principal():
            break  # Salir del bucle si el inicio de sesión no es exitoso
        print('''
                1. Ingresar tareas a la agenda
                2. Buscar tarea por id
                3. Listar todas las tareas de la agenda
                4. Actualizar una tarea en la agenda
                ''')# Se deben imprimir las posibles opciones de la agenda
        opcion = input("Ingrese una opcion: ")
        while flujo:
            if opcion == "1": #Opcion 1 ingresa una tarea a la agenda

                Agenda.ingresarTarea()
                flujo = False

            elif opcion == "2": #Opcion 2 buscar tarera por id

                Agenda.buscarTareaPorID()
                flujo = False

            elif opcion == "3": #Opcion 3 listar todas las tareas de la agenda

                Agenda.desplegarTareas()

            else:
                flujo = False
                
#Ejecutar el programa
main()

#---------------------------------------------------------------------------------------
# Cerrar conexión a la base de datos data
conn.close()