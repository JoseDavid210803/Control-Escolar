# Manejo de la base de datos para el programa de control escolar
# Importar el archivo "control_escolar_db.sql" a la base de datos "control"
from mysql.connector import connect, Error


class DB():
    def __init__(self, host="localhost", user="root", password="", database="control"):
        self.host    = host
        self.user    = user
        self.password= password
        self.database= database

        # Conexión a la base de datos "control" en MySQL
        try:
            self.connection = connect(
                host    = self.host,
                user    = self.user,
                password= self.password,
                database= self.database
            )
            
            print("connected: ", self.connection)

            # Cursor para manipular funciones 
            self.cursor = self.connection.cursor()
            
        # Verificación de conexión
        except Error as e:
            print(f"Error en conectar la BD: {e}")

    
    # Manejo del cursor para utilizarlo desde cualquier archivo
    def getCursor(self):
        return self.cursor