import tkinter as tk
from tkinter import messagebox
import mysql.connector

from App import APP

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("540x290")
        self.create_widgets()

    def create_widgets(self):    
        self.lbltitulo = tk.Label(self, text="CONTROL ESCOLAR", font=("Arial", 32, "bold"))
        self.lbltitulo.place(x=50, y=10)

        self.lblusuario = tk.Label(self, text="Usuario:", font=("Arial", 12))
        self.lblusuario.place(x=100, y=100)

        self.txusuario = tk.Entry(self)
        self.txusuario.place(x=170, y=103)
        self.txusuario.config(font=("Arial", 12), width=30)

        self.lblcontraseña = tk.Label(self, text="Contraseña:", font=("Arial", 12))
        self.lblcontraseña.place(x=75, y=140)

        self.txcontraseña = tk.Entry(self, show="*")
        self.txcontraseña.place(x=168, y=143)
        self.txcontraseña.config(font=("Arial", 12), width= 30)

        self.btnLogin = tk.Button(self, text="Iniciar Sesión", command=self.verificar_login)
        self.btnLogin.place(x=240, y=180)
        self.btnLogin.config(font=("Arial", 12))

    def verificar_login(self):
        usuario = self.txusuario.get()
        contraseña = self.txcontraseña.get()

        # Conectar BD
        try:
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="control"
            )
            cursor = db_connection.cursor()
            cursor.execute("SELECT nombre, perfil FROM usuarios WHERE BINARY username = %s AND BINARY contraseña = %s AND status = 'Activo'", (usuario, contraseña))  # Binary es para que sea sensible a mayus y minus
            user_data = cursor.fetchone()  # Regresar tupla de datos

            if user_data:
                messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
                self.destroy()  # Cerrar la ventana de inicio de sesión
                self.abrir_app(usuario)  # Pasar los datos del usuario a la ventana de app
            else:
                messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas.")
                db_connection.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error en conectar la BD: {e}")

    def abrir_app(self, usuario):
        app = APP(usuario)  # Pasar el argumento 'usuario' a la inicialización de la ventana
        app.mainloop()  # Iniciar el bucle de eventos de la ventana 

if __name__ == "__main__":
    login = Login()
    login.mainloop()
