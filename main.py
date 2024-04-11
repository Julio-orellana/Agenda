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

# Crear conexion a la base de datos data
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

#-----------------------------------------------------------------------------------------------------------------------------------------------

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

        # Función para ingresar los valores
        def ingresarDato(identificador=None, fecha_tarea=None, tarea=None):
            global id, fecha, task  # Otorgar valor global a los datos
            code = True
            while code:
                if identificador is None:
                    identificador = int(input("Ingrese un numero de ID para la tarea: "))
                    continue
                else:
                    id = identificador

                if fecha_tarea is None:
                    dia = input("\nIngrese el día de la tarea [1-31]: ")
                    mes = input("Ingrese el mes de la tarea [1-12] : ")
                    año = input("Ingrese el año de la tarea: ")
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

        if ingresarDato():  # Si la funcion ingresarDato() retorna True, se ejecuta el codigo

            print("\nIngresando tarea...")
            cursor.execute('INSERT INTO agenda (id, fecha, tarea) VALUES (?, ?, ?)',
                        (id, fecha, task))
            conn.commit()
            print('\nTarea guardada correctamente.\n')
            op = input("Desea visualizar la tarea? S/N: ").lower()
            if op == "s":
                print("\n------------------------------------------------------------------")
                print(f"\nFecha de la tarea: {fecha}\nID: {id}\nDescripcion: {task}")
        conn.close()  # Cerrar la conexion a la base de datos


    def eliminarTareaPorID():#Funcion para eliminar una tarea por ID
        conn #Conexion a la base de datos
    
        # Pedir el ID de la tarea a eliminar
        eliminarId = int(input("Ingrese el ID de la tarea que desea eliminar: "))
        cursor.execute('SELECT * FROM agenda WHERE id=?', (eliminarId,))
        verificarId = cursor.fetchone()
        if verificarId:
            cursor.execute('DELETE FROM agenda WHERE id=?', (eliminarId,))
            conn.commit()
            print("Tarea eliminada correctamente.")
            conn.close()
        # Si no se encuentra la tarea
        else:
            print("No se ha encontrado la tarea.")
            conn.close()  # Cerrar la conexion a la base de datos

    def buscarTareaPorID():#Funcion para buscar una tarea por ID en la tabla agenda
        conn #Conexion a la base de datos

        # Pedir el ID de la tarea a buscar
        buscarId = int(input("Ingrese el ID de la tarea que desea buscar: "))
        cursor.execute('SELECT * FROM agenda WHERE id=?', (buscarId,))
        tareaEncontrada = cursor.fetchone()
        if tareaEncontrada:
            fecha = tareaEncontrada[1]
            descripcion = tareaEncontrada[2]
            print("\n------------------------------------------------------------------")
            print(f"\nFecha de la tarea: {fecha}\nID: {buscarId}\nDescripcion: {descripcion}")
        else:
            print("No se ha encontrado la tarea.")

        conn.close() # Cerrar la conexion a la base de datos

    def desplegarTareas():#Funcion para mostrar todas las tareas de la tabla agenda
        conn #Conexion a la base de datos
    
        cursor.execute('SELECT * FROM agenda')
        tareas = cursor.fetchall()

        if len(tareas) > 0:
            print("\nListado de Tareas:")
            print("------------------------------------------------------------------")
            for tarea in tareas:
                fecha = tarea[1]
                descripcion = tarea[2]
                print(f"\nFecha de la tarea: {fecha}\nID: {tarea[0]}\nDescripcion: {descripcion}")
                print("------------------------------------------------------------------")
        else:
            print("\nNo hay tareas registradas.")

            conn.close()  # Cerrar la conexion a la base de datos

    def buscarTareasPorFecha():
        conn
        # Solicitar al usuario la fecha para buscar tareas
        dia = input("Ingrese el día de la tarea [1-31]: ")
        mes = input("Ingrese el mes de la tarea [1-12]: ")
        año = input("Ingrese el año de la tarea: ")
        fecha_buscada = f"{dia}/{mes}/{año}"

        cursor.execute('SELECT * FROM agenda WHERE fecha=?', (fecha_buscada,))
        tareas_encontradas = cursor.fetchall()

        if len(tareas_encontradas) > 0:
            print("\nTareas encontradas para la fecha buscada:")
            print("------------------------------------------------------------------")
            for tarea in tareas_encontradas:
                fecha = tarea[1]
                descripcion = tarea[2]
                print(f"\nFecha de la tarea: {fecha}\nID: {tarea[0]}\nDescripcion: {descripcion}")
                print("------------------------------------------------------------------")
        else:
            print("\nNo se encontraron tareas para la fecha buscada.")

        conn.close()  # Cerrar la conexión a la base de datos

    def modificarTarea():
        conn
        # Solicitar al usuario el ID de la tarea a modificar
        id_tarea = int(input("Ingrese el ID de la tarea que desea modificar: "))

        cursor.execute('SELECT * FROM agenda WHERE id=?', (id_tarea,))
        tarea_existente = cursor.fetchone()

        if tarea_existente:
            nueva_fecha = input("Ingrese la nueva fecha de la tarea (DD/MM/AAAA): ")
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")

            cursor.execute('UPDATE agenda SET fecha=?, tarea=? WHERE id=?', (nueva_fecha, nueva_descripcion, id_tarea))
            conn.commit()
            print("Tarea modificada correctamente.")
        else:
            print("No se encontró la tarea.")

        conn.close()  # Cerrar la conexión a la base de datos

    def buscarTareaPorDescripcion():
        conn
        # Solicitar al usuario la descripción para buscar tareas
        descripcion_buscada = input("Ingrese la descripción de la tarea que desea buscar: ")

        cursor.execute('SELECT * FROM agenda WHERE tarea LIKE ?', ('%' + descripcion_buscada + '%',))
        tareas_encontradas = cursor.fetchall()

        if len(tareas_encontradas) > 0:
            print("\nTareas encontradas para la descripción buscada:")
            print("------------------------------------------------------------------")
            for tarea in tareas_encontradas:
                fecha = tarea[1]
                descripcion = tarea[2]
                print(f"\nFecha de la tarea: {fecha}\nID: {tarea[0]}\nDescripcion: {descripcion}")
                print("------------------------------------------------------------------")
        else:
            print("\nNo se encontraron tareas para la descripción buscada.")

        conn.close()  # Cerrar la conexión a la base de datos

    def tareasPendientes():
        conn
        cursor.execute('SELECT * FROM agenda WHERE completada=0')
        tareas_pendientes = cursor.fetchall()

        if len(tareas_pendientes) > 0:
            print("\nTareas Pendientes:")
            print("------------------------------------------------------------------")
            for tarea in tareas_pendientes:
                fecha = tarea[1]
                descripcion = tarea[2]
                print(f"\nFecha de la tarea: {fecha}\nID: {tarea[0]}\nDescripcion: {descripcion}")
                print("------------------------------------------------------------------")
        else:
            print("\nNo hay tareas pendientes.")

        conn.close()  # Cerrar la conexión a la base de datos

    def marcarTareaCompleta():
        conn
        # Solicitar al usuario el ID de la tarea a marcar como completada
        id_tarea = int(input("Ingrese el ID de la tarea que desea marcar como completada: "))

        cursor.execute('SELECT * FROM agenda WHERE id=?', (id_tarea,))
        tarea_existente = cursor.fetchone()

        if tarea_existente:
            cursor.execute('UPDATE agenda SET completada=1 WHERE id=?', (id_tarea,))
            conn.commit()
            print("Tarea marcada como completada.")
        else:
            print("No se encontró la tarea.")

        conn.close()  # Cerrar la conexión a la base de datos

    def desplegarTareasPendientes():
        conn

        cursor.execute('SELECT * FROM agenda WHERE completada=0')
        tareas_pendientes = cursor.fetchall()

        if len(tareas_pendientes) > 0:
            print("\nTareas Pendientes:")
            print("------------------------------------------------------------------")
            for tarea in tareas_pendientes:
                fecha = tarea[1]
                descripcion = tarea[2]
                print(f"\nFecha de la tarea: {fecha}\nID: {tarea[0]}\nDescripcion: {descripcion}")
                print("------------------------------------------------------------------")
        else:
            print("\nNo hay tareas pendientes.")

        conn.close()  # Cerrar la conexión a la base de datos

    def desplegarTareasCompletadas():
        conn
        cursor.execute('SELECT * FROM agenda WHERE completada=1')
        tareas_completadas = cursor.fetchall()

        if len(tareas_completadas) > 0:
            print("\nTareas Completadas:")
            print("------------------------------------------------------------------")
            for tarea in tareas_completadas:
                fecha = tarea[1]
                descripcion = tarea[2]
                print(f"\nFecha de la tarea: {fecha}\nID: {tarea[0]}\nDescripcion: {descripcion}")
                print("------------------------------------------------------------------")
        else:
            print("\nNo hay tareas completadas.")

        conn.close()  # Cerrar la conexión a la base de datos

    def marcarTareaIncompleta():
        conn
        # Solicitar al usuario el ID de la tarea a marcar como incompleta
        id_tarea = int(input("Ingrese el ID de la tarea que desea marcar como incompleta: "))

        cursor.execute('SELECT * FROM agenda WHERE id=?', (id_tarea,))
        tarea_existente = cursor.fetchone()

        if tarea_existente:
            cursor.execute('UPDATE agenda SET completada=0 WHERE id=?', (id_tarea,))
            conn.commit()
            print("Tarea marcada como incompleta.")
        else:
            print("No se encontró la tarea.")

        conn.close()  # Cerrar la conexión a la base de datos

#-----------------------------------------------------------------------------------------------------------------------------------------------
#FIN