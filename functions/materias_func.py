# archivo de manejo de las funciones de las materias
from tkinter import messagebox

# Archivo de donde se abre la base de datos
from database.db_manager import DB

# Clase materias
# id_materia, id_horario, id_maestro, asignatura, creditos, semestre, carrera
class MateriasFunc():
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()

        
    # Creación de materia, se usará como "Guardar" en el programa
    def nuevaMateria(self, id_horario, id_maestro, asignatura, creditos, semestre, carrera):
        agregar_materia = ("""
        INSERT INTO 
            materias 
                (id_horario, id_maestro, asignatura, creditos, semestre, carrera) 
        VALUES 
            (%s, %s, %s, %s, %s, %s)
        """)
        
        values = (id_horario, id_maestro, asignatura, creditos, semestre, carrera)

        self.cursor.execute(agregar_materia, values)

        # Guarda los cambios en la base de datos
        self.connection.commit()



    # Editar materia
    def editarMateria(self, id_materia, id_horario, id_maestro, asignatura, creditos, semestre, carrera):
        # Edita todos los atributos de la materia que tenga el id "id_materia"

        editar_materia = ("""
            UPDATE
                materias
            SET
                id_horario = %s, 
                id_maestro = %s, 
                asignatura = %s, 
                creditos = %s, 
                semestre = %s, 
                carrera = %s
            WHERE
                id_materia = %s
        """)
        values = (id_horario, id_maestro, asignatura, creditos, semestre, carrera, id_materia)

        self.cursor.execute(editar_materia, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()
    

    # Eliminar materia PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarMateria(self, id_materias):
        eliminar_materia = "DELETE FROM materias WHERE id_materia = %s"

        self.cursor.execute(eliminar_materia, id_materias)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # Busca una materia por su id
    def buscarIdMateria(self, id_materia):
        try:
            buscar_materia = (f"SELECT * FROM materias WHERE id_materia = {id_materia}")
            self.cursor.execute(buscar_materia)
            materia_encontrada = self.cursor.fetchone()

            # Se regresa la materia encontrada de forma
            # [0]=id_materia, [1]=id_horario, [2]=id_maestro, [3]=asignatura, [4]=creditos, [5]=semestre, [6]=carrera
            return materia_encontrada
        except:
            return None


    # Mostrar lista de materias
    def getListaMaterias(self):
        mostrar_materias = "SELECT * FROM materias"
        lista_materias = []
        lista_materias = self.cursor.fetchall(mostrar_materias)

        # Se regresa como matriz de materias [m][n] donde 
            # m = materias registradas
            # n = atributos ([0]=id_materia, [1]=id_horario, [2]=id_maestro, [3]=asignatura, [4]=creditos, [5]=semestre, [6]=carrera)
        return lista_materias
    


    # Último id ingresado (Para la hora de agregar una nueva)
    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id_materia) FROM materias")
        result = self.cursor.fetchall()[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0