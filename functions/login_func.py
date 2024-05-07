# archivo de manejo de las funciones del login
from mysql.connector import connect, Error
from tkinter import messagebox

# Archivo de donde se abre la base de datos
from database.db_manager import DB


class LoginFunc():
    # Instancias para la verificación y el usuario
    def __init__(self):
        # La declaración de la base de datos        
        self.db = DB()
        # Manejo del connection y cursor() desde archivo externo
        self.connection = self.db.getConnection()
        self.cursor = self.connection.cursor()


    def verificar_login(self, correo, contrasena):
        self.cursor.execute("SELECT * FROM usuarios WHERE BINARY correo = %s AND BINARY contrasena = %s", (correo, contrasena))  # Binary es para que sea sensible a mayus y minus

        user_data = self.cursor.fetchone() # Regresar tupla de datos

        if user_data: 
            print(f"Login user:   {user_data[1]} {user_data[2]} {user_data[3]} \nuser profile: {user_data[7]}\nuser status:  {user_data[8]}")
            if user_data[8] == 'Inactivo':
                print("Usuario Inactivo!")
                return None
            
            # Regresa todos los valores de un usuario en la forma
            # [0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=username  [6]=contraseña  [7]=perfil  [8]=status 	
            return user_data
        else: 
            print("Login fail!")
            return None
