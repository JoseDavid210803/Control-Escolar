# archivo de manejo de las funciones de los usuarios
from mysql.connector import connect, Error
from tkinter import messagebox

# Clase usuarios
# id, nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil (Administrador, Maestro, Alumno), status (Activo, Inactivo)
class UsuariosFunc():
    # Constructor de Usuarios mas una instancia a la base de datos
    def __init__(self):        
        # Conexión a la base de datos "control" en MySQL
        try:
            self.connection = connect(
                host="localhost",
                user="root",
                password="",
                database="control"
            )

            # Cursor para manipular funciones 
            self.cursor = self.connection.cursor()
            
        # Verificación de conexión
        except Error as e:
            messagebox.showerror("Error", f"Error en conectar la BD: {e}")

    

    # Creación de usuario, se usará como "Guardar" en el programa
    def nuevoUsuario(self, nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status):
        # Revisar que no se registren dos usuarios con el mismo correo
        if not self.verifica_correo(correo):
            insert_user = ("""
            INSERT INTO 
                usuarios
                    (nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status) 
            VALUES 
                ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
            """, (nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status)) 

            self.cursor.execute(insert_user)

        else:
            messagebox.showwarning("Error","El correo ya está registrado!")



    # Editar usuario
    def editarUsuario(self, id, nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status):
        # Edita todos los atributos del usuario que tenga el id "key"

        if not self.verifica_correo(correo):
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
                    id = %d
            """,(nombre, a_paterno, a_materno, correo, usuario, contrasena, perfil, status, id))

            self.cursor.execute(editar_usuario)

            # Regresa el usuario editado 
            return self.buscarIdUsuario(id)
        else:
            messagebox.showwarning("Error","El correo ya está registrado!")
    

    # Eliminar usuario PERMANENTEMENTE
    # (es de apoyo pero en el código no se necesitará)
    def eliminarUsuario(self, id):
        eliminar_usuario = "DELETE FROM usuarios WHERE id = %d"

        self.cursor.execute(eliminar_usuario, id)


    # "Elimina" al usuario (lo deja inactivo) dejando sus datos
    def inactivarUsuario(self, id):
        inactivar_usuario = ("""
            UPDATE
                usuarios
            SET
                status = 'Inactivo'
            WHERE
                id = %d
        """, id)

        self.cursor.execute(inactivar_usuario)


    # Busca un usuario por su id
    def buscarIdUsuario(self, id):
        try:
            buscar_usuario = ("SELECT * FROM usuarios WHERE id = %d", id)
            self.cursor.execute(buscar_usuario)
            found_user = self.cursor.fetchone()

            # Se regresa el usuario encontrado de forma
            # [0]=id, [1]=nombre, [2]=a_paterno, [3]=a_materno, [4]=correo, [5]=usuario, [6]=contrasena, [7]=perfil, [8]=status
            return found_user
        except:
            return None


    # Mostrar lista de usuarios
    def getListaUsuarios(self):
        show_user = "SELECT * FROM users"
        list_users = []
        list_users = self.cursor.fetchall(show_user)

        # Se regresa como matriz de usuarios [m][n] donde 
            # m = usuarios registrados
            # n = atributos ([0]=id, [1]=nombre, [2]=a_paterno, [3]=a_materno, [4]=correo, [5]=usuario, [6]=contrasena, [7]=perfil, [8]=status)
        return list_users
    
    # Verificar si existe el correo
    def verifica_correo(self, correo):
        # Busca correos "parecidos" al ingresado por si ya está repetido
        self.cursor.execute("SELECT * FROM usuarios WHERE correo LIKE %s", (correo))
        usuario_existe = self.cursor.fetchone()
        
        if usuario_existe: 
            return True
        else: 
            return False
        
    
    # Último id ingresado (no necesario, sólo si se necesita)
    def getUltimoId(self):
        command = "SELECT MAX(id) FROM usuarios"
        result = self.cursor.fetchall(command)[0]
        
        if result[0] is not None:
            return result[0]
        else:
            return 0