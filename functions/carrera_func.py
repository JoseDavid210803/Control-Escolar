# archivo de manejo de las funciones de las carreras
from tkinter import messagebox

# Archivo de donde se abre la base de datos
from database.db_manager import DB

# Clase carrera
# id_carrera, nombre, semestre
class CarrerasFunc():
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()

        
    # Creación de carrera, se usará como "Guardar" en el programa
    def nuevaCarrera(self, nombre, semestre):
        agregar_carrera = ("""
        INSERT INTO 
            carrera 
                (nombre, semestre) 
        VALUES 
            (%s, %s)
        """)
        
        values = (nombre, semestre)

        self.cursor.execute(agregar_carrera, values)

        # Guarda los cambios en la base de datos
        self.connection.commit()



    # Editar carrera
    def editarCarrera(self, id_carrera, nombre, semestre):
        # Edita todos los atributos del carrera que tenga el id "id_carrera"

        editar_carrera = ("""
            UPDATE
                carrera
            SET
                nombre = %s, 
                semestre = %s
            WHERE
                id_carrera = %s
        """)
        values = (nombre, semestre, id_carrera)

        self.cursor.execute(editar_carrera, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()
    

    # Eliminar carrera PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarCarrera(self, id_carrera):
        eliminar_carrera = "DELETE FROM carrera WHERE id_carrera = %s"

        self.cursor.execute(eliminar_carrera, id_carrera)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # Busca una carrera por su id
    def buscarIdCarrera(self, id_carrera):
        try:
            buscar_carrera = (f"SELECT * FROM carrera WHERE id_carrera = {id_carrera}")
            self.cursor.execute(buscar_carrera)
            carrera_encontrada = self.cursor.fetchone()

            # Se regresa el carrera encontrada de forma
            # [0]=id_carrera, [1]=nombre, [2]=semestre
            return carrera_encontrada
        except:
            return None


    # Mostrar lista de carreras
    def getListaCarreras(self):
        mostrar_carreras = "SELECT * FROM carrera"
        lista_carreras = []
        lista_carreras = self.cursor.fetchall(mostrar_carreras)

        # Se regresa como matriz de carreras [m][n] donde 
            # m = carreras registradas
            # n = atributos ([0]=id_carrera, [1]=nombre, [2]=semestre)
        return lista_carreras
    


    # Último id ingresado (Para la hora de agregar uno nuevo)
    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id_carrera) FROM carrera")
        result = self.cursor.fetchall()[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0