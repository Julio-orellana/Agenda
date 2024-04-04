# Cerrar conexión
from main import *

if menu_principal():
    Agenda.ingresarDato()
else:
    exit()
conn.close()