#Importar el modulo del proyecto
from main import *

#---------------------------------------------------------------------------------------

#RECUERDEN NO UTILIZAR EL MISMO NOMBRE DE VARIABLES GLOBALES DE AGENDA O DE MAIN A MENOS QUE SE DESEE REESCRIBIR SU VALOR

#Programa principal

#---------------------------------------------------------------------------------------
def main():
    flujo = True
    while True:
        print(f"\n{date}")
        if not menu_principal():
            break  # Salir del bucle si el inicio de sesión no es exitoso
        print('''
                1. Ingresar tareas a la agenda
                2. Eliminar una tarea de la agenda
                3. Buscar tarea por id
                4. Listar todas las tareas de la agenda
                5. Actualizar una tarea en la agenda
                ''')# Se deben imprimir las posibles opciones de la agenda
        opcion = input("Ingrese una opcion: ")
        while flujo:
            if opcion == "1": #Opcion 1 ingresa una tarea a la agenda

                Agenda.ingresarTarea()
                    
            else:
                flujo = False
                
#Ejecutar el programa
main()

#---------------------------------------------------------------------------------------
# Cerrar conexión a la base de datos data
conn.close()