# archivo de manejo de las funciones de los horarios
from tkinter import messagebox

# Archivo de donde se abre la base de datos
from database.db_manager import DB

# Clase horarios
# id_horarios, turno, hora
class HorariosFunc():
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()

        
    # Creación de horario, se usará como "Guardar" en el programa
    def nuevoHorario(self, turno, hora):
        agregar_horario = ("""
        INSERT INTO 
            horarios 
                (turno, hora) 
        VALUES 
            (%s, %s)
        """)
        
        values = (turno, hora)

        self.cursor.execute(agregar_horario, values)

        # Guarda los cambios en la base de datos
        self.connection.commit()



    # Editar horario
    def editarHorario(self, id_horarios, turno, hora):
        # Edita todos los atributos del horario que tenga el id "id_horarios"

        editar_horario = ("""
            UPDATE
                horarios
            SET
                turno = %s, 
                hora = %s
            WHERE
                id_horarios = %s
        """)
        values = (turno, hora, id_horarios)

        self.cursor.execute(editar_horario, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()
    

    # Eliminar horario PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarHorario(self, id_horarios):
        eliminar_horario = "DELETE FROM horarios WHERE id_horarios = %s"

        self.cursor.execute(eliminar_horario, id_horarios)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # Busca un horario por su id
    def buscarIdHorario(self, id_horarios):
        try:
            buscar_horarios = (f"SELECT * FROM horarios WHERE id_horarios = {id_horarios}")
            self.cursor.execute(buscar_horarios)
            horario_encontrado = self.cursor.fetchone()

            # Se regresa el horario encontrado de forma
            # [0]=id_horarios, [1]=turno, [2]=hora
            return horario_encontrado
        except:
            return None


    # Mostrar lista de horarios
    def getListaHorarios(self):
        mostrar_horarios = "SELECT * FROM horarios"
        lista_horarios = []
        lista_horarios = self.cursor.fetchall(mostrar_horarios)

        # Se regresa como matriz de horarios [m][n] donde 
            # m = horarios registrados
            # n = atributos ([0]=id_horarios, [1]=turno, [2]=hora)
        return lista_horarios
    


    # Último id ingresado (Para la hora de agregar uno nuevo)
    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id_horarios) FROM horarios")
        result = self.cursor.fetchall()[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0
