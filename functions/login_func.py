# archivo de manejo de las funciones del login
from mysql.connector import connect, Error
from tkinter import messagebox


class LoginFunc():
    # Instancias para la verificación y el usuario
    def __init__(self):        
        # Conexión a la base de datos "control" en MySQL
        try:
            self.connection = connect(
                host="localhost",
                user="root",
                password="",
                database="control"
            )

            print("connected: ", self.connection)

            # Cursor para manipular funciones 
            self.cursor = self.connection.cursor()
            
        # Verificación de conexión
        except Error as e:
            messagebox.showerror("Error", f"Error en conectar la BD: {e}")


    def verificar_login(self, usuario, contrasena):
        self.cursor.execute("SELECT nombre, perfil FROM usuarios WHERE BINARY username = %s AND BINARY contraseña = %s AND status = 'Activo'", (usuario, contrasena))  # Binary es para que sea sensible a mayus y minus

        user_data = self.cursor.fetchone() # Regresar tupla de datos

        print(user_data)

        if user_data: 
            print("Login true")
            return True
        else: 
            print("Login false")
            return False