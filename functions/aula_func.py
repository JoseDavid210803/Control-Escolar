# archivo de manejo de las funciones de las aulas
from tkinter import messagebox

# Archivo de donde se abre la base de datos
from database.db_manager import DB

# Clase aula
# id_aula, nombre, edificio
class AulasFunc():
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()

        
    # Creación de aula, se usará como "Guardar" en el programa
    def nuevaAula(self, nombre, edificio):
        agregar_aula = ("""
        INSERT INTO 
            aula 
                (nombre, edificio) 
        VALUES 
            (%s, %s)
        """)
        
        values = (nombre, edificio)

        self.cursor.execute(agregar_aula, values)

        # Guarda los cambios en la base de datos
        self.connection.commit()



    # Editar aula
    def editarAula(self, id_aula, nombre, edificio):
        # Edita todos los atributos del aula que tenga el id "id_aula"

        editar_aula = ("""
            UPDATE
                aula
            SET
                nombre = %s, 
                edificio = %s
            WHERE
                id_aula = %s
        """)
        values = (nombre, edificio, id_aula)

        self.cursor.execute(editar_aula, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()
    

    # Eliminar aula PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarAula(self, id_aula):
        eliminar_aula = "DELETE FROM aula WHERE id_aula = %s"

        self.cursor.execute(eliminar_aula, id_aula)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # Busca un aula por su id
    def buscarIdAula(self, id_aula):
        try:
            buscar_aulas = (f"SELECT * FROM aula WHERE id_aula = {id_aula}")
            self.cursor.execute(buscar_aulas)
            aula_encontrada = self.cursor.fetchone()

            # Se regresa el aula encontrada de forma
            # [0]=id_aula, [1]=nombre, [2]=edificio
            return aula_encontrada
        except:
            return None


    # Mostrar lista de aulas
    def getListaAulas(self):
        mostrar_aulas = "SELECT * FROM aula"
        lista_aulas = []
        self.cursor.execute(mostrar_aulas)
        lista_aulas = self.cursor.fetchall()

        # Se regresa como matriz de aulas [m][n] donde 
            # m = aula registrados
            # n = atributos ([0]=id_aula, [1]=nombre, [2]=edificio)
        return lista_aulas
    


    # Último id ingresado (Para la hora de agregar uno nuevo)
    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id_aula) FROM aula")
        result = self.cursor.fetchall()[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0
