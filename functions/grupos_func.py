# archivo de manejo de las funciones de los grupos
from tkinter import messagebox

# Archivo de donde se abre la base de datos
from database.db_manager import DB

# Clase grupos
# id_grupos, id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn
class GruposFunc():
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()

        
    # Creación de grupo, se usará como "Guardar" en el programa
    def nuevoGrupo(self, id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn):
        agregar_grupo = ("""
        INSERT INTO 
            grupos 
                (id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn) 
        VALUES 
            (%s, %s, %s, %s, %s, %s)
        """)
        
        values = (id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn)

        self.cursor.execute(agregar_grupo, values)

        # Guarda los cambios en la base de datos
        self.connection.commit()



    # Editar grupo
    def editarGrupo(self, id_grupos, id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn):
        # Edita todos los atributos del grupo que tenga el id "id_grupos"

        editar_grupo = ("""
            UPDATE
                grupos
            SET
                id_carrera = %s, 
                id_materia = %s, 
                id_alumnos = %s, 
                salon = %s, 
                semestre = %s, 
                max_alumn = %s
            WHERE
                id_grupos = %s
        """)
        values = (id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn, id_grupos)

        self.cursor.execute(editar_grupo, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()
    

    # Eliminar grupo PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarGrupo(self, id_grupos):
        eliminar_grupo = "DELETE FROM grupos WHERE id_grupos = %s"

        self.cursor.execute(eliminar_grupo, id_grupos)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # Busca un grupo por su id
    def buscarIdGrupo(self, id_grupos):
        try:
            buscar_grupo = (f"SELECT * FROM grupos WHERE id_grupos = {id_grupos}")
            self.cursor.execute(buscar_grupo)
            grupo_encontrado = self.cursor.fetchone()

            # Se regresa el grupo encontrada de forma
            # [0]=id_grupos, [1]=id_carrera, [2]=id_materia, [3]=id_alumnos, [4]=salon, [5]=semestre, [6]=max_alumn
            return grupo_encontrado
        except:
            return None


    # Mostrar lista de grupos
    def getListaGrupos(self):
        mostrar_grupos = "SELECT * FROM grupos"
        lista_grupos = []
        lista_grupos = self.cursor.fetchall(mostrar_grupos)

        # Se regresa como matriz de grupos [m][n] donde 
            # m = grupos registrados
            # n = atributos ([0]=id_grupos, [1]=id_carrera, [2]=id_materia, [3]=id_alumnos, [4]=salon, [5]=semestre, [6]=max_alumn)
        return lista_grupos
    


    # Último id ingresado (Para la hora de agregar uno nuevo)
    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id_grupos) FROM grupos")
        result = self.cursor.fetchall()[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0