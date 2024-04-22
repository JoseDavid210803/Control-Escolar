# pantalla de login

import tkinter as tk
from tkinter import messagebox

from functions.login_func import LoginFunc
from app.home_app import AppHome

class AppLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("540x290")
        self.create_widgets()

        self.login = LoginFunc()
        

    def create_widgets(self):    
        self.lbltitulo = tk.Label(self, text="CONTROL ESCOLAR", font=("Arial", 32, "bold"))
        self.lbltitulo.place(x=50, y=10)

        self.lblcorreo = tk.Label(self, text="Correo:", font=("Arial", 12))
        self.lblcorreo.place(x=100, y=100)

        self.txcorreo = tk.Entry(self)
        self.txcorreo.place(x=170, y=103)
        self.txcorreo.config(font=("Arial", 12), width=30)

        self.lblcontraseña = tk.Label(self, text="Contraseña:", font=("Arial", 12))
        self.lblcontraseña.place(x=75, y=140)

        self.txcontrasena = tk.Entry(self, show="*")
        self.txcontrasena.place(x=168, y=143)
        self.txcontrasena.config(font=("Arial", 12), width= 30)

        self.btnLogin = tk.Button(self, 
                                  text="Iniciar Sesión", 
                                  command=self.abrir_app)
        self.btnLogin.place(x=240, y=180)
        self.btnLogin.config(font=("Arial", 12))
        

    def abrir_app(self):
        correo = self.txcorreo.get()
        contrasena = self.txcontrasena.get()

        usuario = self.login.verificar_login(correo, contrasena)

        if usuario:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            self.destroy()  # Cerrar la ventana de inicio de sesión
            home = AppHome(usuario[5])  # Pasar el argumento 'usuario' a la inicialización de la ventana
            home.mainloop()  # Iniciar el bucle de eventos de la ventana
            
        else:
            messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas.")


if __name__ == "__main__":
    login = AppLogin()
    login.mainloop()