#INICIO
#-----------------------------------------------------------------------------------------------------------------------------------------------

#RECUERDEN NO UTILIZAR EL MISMO NOMBRE DE VARIABLES GLOBALES DE LOS MODULOS AGENDA O MAIN A MENOS QUE SE DESEE REESCRIBIR SU VALOR

#Importar Librerias
import sqlite3
import datetime as dt

#-----------------------------------------------------------------------------------------------------------------------------------------------

date = dt.datetime.now() #Fecha actual del sistema

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Creacion base de datos local

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Conexión a la base de datos data
conn = sqlite3.connect('data.db')
cursor = conn.cursor()


# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS data
                (usuario TEXT PRIMARY KEY, contraseña TEXT)''')
conn.commit()

def registrar_usuario(usuario, contraseña):
    # Verificar si el usuario ya existe
    cursor.execute('SELECT * FROM data WHERE usuario = ?', (usuario,))
    existe_usuario = cursor.fetchone()
    if existe_usuario:
        print("\nEl usuario ya existe.")
        return

    # Verificar la contraseña
    if len(contraseña) < 8 or not any(char.isdigit() for char in contraseña):
        print("\nLa contraseña debe contener al menos 8 caracteres y un número.")
        return

    # Insertar usuario en la base de datos
    cursor.execute('INSERT INTO data (usuario, contraseña) VALUES (?, ?)',
                   (usuario, contraseña))
    conn.commit()
    print("\nUsuario registrado con éxito.")


def iniciar_sesion(usuario, contraseña):
    # Verificar credenciales
    cursor.execute('SELECT * FROM data WHERE usuario = ? AND contraseña = ?',
                   (usuario, contraseña))
    usuario_encontrado = cursor.fetchone()
    if usuario_encontrado:
        print("\nInicio de sesión exitoso.")
        return True
    else:
        print("\nCredenciales incorrectas.")
        return False

def eliminar_usuario(usuario):
    # Verificar si el usuario existe
    cursor.execute('SELECT * FROM data WHERE usuario = ?', (usuario,))
    existe_usuario = cursor.fetchone()
    if existe_usuario:
        cursor.execute('DELETE FROM data WHERE usuario = ?', (usuario,))
        conn.commit()
        print("\nUsuario eliminado con éxito.")
    else:
        print("\nEl usuario no existe.")

# Función para registrar, iniciar sesión, eliminar o salir
def menu_principal():

    while True:
        print("\nOPCIONES DISPONIBLES:\n")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Eliminar usuario")
        print("4. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("\nIngrese nombre de usuario: ")
            contraseña = input("Ingrese contraseña: ")
            registrar_usuario(usuario, contraseña)
            
        elif opcion == "2":
            usuario = input("\nIngrese nombre de usuario: ")
            contraseña = input("Ingrese contraseña: ")
            inicio_exitoso = iniciar_sesion(usuario, contraseña)
            if inicio_exitoso:
                break  # Salir del bucle si el inicio de sesión es exitoso
            else:
                print("\nPor favor vuelva a intentarlo")

        elif opcion == "3":
            usuario = input("\nIngrese el nombre de usuario a eliminar: ")
            eliminar_usuario(usuario)
        elif opcion == "4":
            print("\nSaliendo del programa...")
            conn.close()
            return False
            
        else:
            print("\nOpción no válida. Inténtelo de nuevo.")

    return True  # Indica que el inicio de sesión fue exitoso

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Cracion de la clase para la agenda
class Agenda:
    #AQUI ADENTRO SE DEBE ESCRIBIR NUESTRO PROGRAMA!

    #Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agenda (
            id INTEGER PRIMARY KEY,
            fecha TEXT,
            tarea TEXT
        )
    ''')
    conn.commit()

    def ingresarTarea():  # Función para ingresar una nueva tarea

        conn #Conexion a la base de datos

        # Función para ingresar los valores
        def ingresarDato( identificador=None, 
            fecha_tarea = {
                    "day": None,
                    "month": None,
                    "year": None
                },
                 tarea=None):

            global id, fecha, task  # Otorgar valor global a los datos
            code = True
            while code:
                if identificador is None:
                    identificador = int(input("Ingrese un numero de ID para la tarea: "))
                    continue
                else:
                    id = identificador

                if fecha_tarea["day"] is None or fecha_tarea["month"] is None or fecha_tarea["year"] is None:
                    dia =  input("\nIngrese el día de la tarea [1-31]: ")
                    mes =  input("Ingrese el mes de la tarea [1-12] : ")
                    año =  input("Ingrese el año de la tarea: ")
                    fecha_tarea = {
                        "day": dia,
                        "month": mes,
                        "year": año
                    }
                    continue
                else:
                    fecha = fecha_tarea["day"] + "/" + fecha_tarea["month"] + "/" + fecha_tarea["year"]

                if tarea is None:
                    tarea = input("Ingrese la descripción de la tarea: ")
                    task = tarea
                    code = False
                    return True

        if ingresarDato():
            print("\nIngresando tarea...")
            cursor.execute('INSERT INTO agenda (id, fecha, tarea) VALUES (?, ?, ?)',
                   (id, fecha, task))
            conn.commit()
            print('\nTarea guardada correctamente.\n')
            op = input("Desea visualizar la tarea? S/N: ").lower()
            if op == "s":
                print("\n------------------------------------------------------------------")
                print(f"\nFecha de la tarea: {fecha}\nID: {id}\nDescripcion: {task}")
        conn.close()#Cerrar la conexion a la base de datos


    def eliminarTarea(): #Funcion para eliminar una tarea
        conn #Conectar a la base de datos
        


#-----------------------------------------------------------------------------------------------------------------------------------------------
#FIN