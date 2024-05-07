from tkinter import messagebox
from database.db_manager import DB

class AlumnosFunc():
    def __init__(self):
        self.db = DB()
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()

    def nuevoAlumno(self, id_carrera, id_grupo, id_usuario, fecha_nacimiento):
        agregar_alumno = ("""
        INSERT INTO 
            alumnos 
                (id_carrera, id_grupo, id_usuario, fecha_nacimiento) 
        VALUES 
            (%s, %s, %s, %s)
        """)

        values = (id_carrera, id_grupo, id_usuario, fecha_nacimiento)

        self.cursor.execute(agregar_alumno, values)
        self.connection.commit()

    def editarAlumno(self, id_alumno, id_carrera, id_grupo, id_usuario, fecha_nacimiento):
        editar_alumno = ("""
            UPDATE
                alumnos
            SET
                id_carrera = %s, 
                id_grupo = %s, 
                id_usuario = %s, 
                fecha_nacimiento = %s
            WHERE
                id_alumno = %s
        """)

        values = (id_carrera, id_grupo, id_usuario, fecha_nacimiento, id_alumno)

        self.cursor.execute(editar_alumno, values)
        self.connection.commit()

    def eliminarAlumno(self, id_alumno):
        eliminar_alumno = "DELETE FROM alumnos WHERE id_alumno = %s"

        self.cursor.execute(eliminar_alumno, (id_alumno,))
        self.connection.commit()

    def buscarIdAlumno(self, id_alumno):
        try:
            buscar_alumno = ("SELECT * FROM alumnos WHERE id_alumno = %s")
            self.cursor.execute(buscar_alumno, (id_alumno,))
            alumno_encontrado = self.cursor.fetchone()

            return alumno_encontrado
        except:
            return None

    def getListaAlumnos(self):
        mostrar_alumnos = "SELECT * FROM alumnos"
        self.cursor.execute(mostrar_alumnos)
        lista_alumnos = self.cursor.fetchall()

        return lista_alumnos

    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id_alumno) FROM alumnos")
        result = self.cursor.fetchall()[0]

        if result[0] is not None:
            return result[0]
        else:
            return 0
