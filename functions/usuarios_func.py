# archivo de manejo de las funciones de los usuarios
from mysql.connector import connect, Error
from tkinter import messagebox

import re

# Archivo de donde se abre la base de datos
from database.db_manager import DB

# Clase usuarios
# id, nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil (Administrador, Maestro, Alumno), status (Activo, Inactivo)
class UsuariosFunc():
    # Instancias para la verificación y el usuario
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()
    

    # Creación de usuario, se usará como "Guardar" en el programa
    def nuevoUsuario(self, nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status):
        # Revisar que no se registren dos usuarios con el mismo correo
        if not self.verifica_correo(correo):
            insert_user = ("""
            INSERT INTO 
                usuarios 
                    (nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status) 
            VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s)
            """)
            
            values = (nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status)

            self.cursor.execute(insert_user, values)

            # Guarda los cambios en la base de datos
            self.connection.commit()

        else:
            messagebox.showwarning("Error","El correo ya está registrado!")



    # Editar usuario
    def editarUsuario(self, id, nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status):
        # Edita todos los atributos del usuario que tenga el id "key"

        editar_usuario = ("""
            UPDATE
                usuarios
            SET
                nombre = %s,
                a_paterno = %s,
                a_materno = %s,
                correo = %s,
                usuario = %s,
                contrasena = %s,
                perfil = %s,
                status = %s
            WHERE
                id = %s
        """)
        values = (nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status, id)

        self.cursor.execute(editar_usuario, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()
    

    # Eliminar usuario PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarUsuario(self, id):
        eliminar_usuario = "DELETE FROM usuarios WHERE id = %s"

        self.cursor.execute(eliminar_usuario, id)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # "Elimina" al usuario (lo deja inactivo) dejando sus datos
    def desactivarUsuario(self, id):
        desactivar_usuario = ("""
            UPDATE
                usuarios
            SET
                status = 'Inactivo'
            WHERE
                id = %s
        """)
        values = (id,)

        self.cursor.execute(desactivar_usuario, values)
        
        # Guarda los cambios en la base de datos
        self.connection.commit()


    # Busca un usuario por su id
    def buscarIdUsuario(self, id):
        try:
            buscar_usuario = (f"SELECT * FROM usuarios WHERE id = {id}")
            self.cursor.execute(buscar_usuario)
            found_user = self.cursor.fetchone()

            # Se regresa el usuario encontrado de forma
            # [0]=id, [1]=nombre, [2]=a_paterno, [3]=a_materno, [4]=correo, [5]=usuario, [6]=contrasena, [7]=perfil, [8]=status
            return found_user
        except:
            return None


    # Mostrar lista de usuarios
    def getListaUsuarios(self):
        show_user = "SELECT * FROM usuarios"
        list_users = []
        list_users = self.cursor.fetchall(show_user)

        # Se regresa como matriz de usuarios [m][n] donde 
            # m = usuarios registrados
            # n = atributos ([0]=id, [1]=nombre, [2]=a_paterno, [3]=a_materno, [4]=correo, [5]=usuario, [6]=contrasena, [7]=perfil, [8]=status)
        return list_users
    
    # Verificar si existe el correo
    def verifica_correo(self, correo):
        # Busca correos parecidos al ingresado por si ya está repetido
        self.cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        return self.cursor.fetchone() is not None


    # Último id ingresado (Para la hora de agregar un nuevo)
    def getUltimoId(self):
        self.cursor.execute("SELECT MAX(id) FROM usuarios")
        result = self.cursor.fetchall()[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0
        
        
    def validarContrasena(self, contrasena):
        # Verificar si la contraseña tiene al menos 8 caracteres
        if len(contrasena) < 8:
            messagebox.showwarning("Error","Contraseña debe de ser mayor a 8 dígitos!")
            return False
        
        # Verificar si la contraseña tiene al menos una mayúscula
        if not re.search(r"[A-Z]", contrasena):
            messagebox.showwarning("Error","Contraseña Debe de tener como mínimo una mayúscula!")
            return False
        
        # Verificar si la contraseña tiene al menos un carácter especial
        if not re.search(r"[!@#$%^&*()\-_=+{};:,]", contrasena):
            messagebox.showwarning("Error","Contraseña debe de tener un carácter especial!")
            return False
        
        # Verificar si la contraseña tiene al menos un número
        if not re.search(r"\d", contrasena):
            messagebox.showwarning("Error","Contraseña debe de contener mínimo un número!")
            return False
        
        
        return True