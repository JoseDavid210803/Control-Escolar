# pantalla de login

import tkinter as tk
from tkinter import messagebox

from functions.login_func import LoginFunc
from app.home_app import AppHome

class AppLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Control Escolar")
        self.geometry("540x290")
        self.resizable(0, 0)
        self.create_widgets()
        self.iconbitmap(r"C:\Users\sofia\Desktop\Control Escolar\img\01.ico")


        self.login = LoginFunc()
        

    def create_widgets(self):    
        self.lbltitulo = tk.Label(self, text="CONTROL ESCOLAR", font=("Arial", 32, "bold"))
        self.lbltitulo.place(x=50, y=15)

        self.lblcorreo = tk.Label(self, text="Correo:", font=("Arial", 12))
        self.lblcorreo.place(x=75, y=100)

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
        self.btnLogin.place(x=200, y=200)
        self.btnLogin.config(font=("Arial", 12))
        
        self.Registrarse = tk.Label(self, text="¿No estás registrado? Registrate aquí", fg="blue", cursor="hand2")
        self.Registrarse.place(x=155, y=240)
        self.Registrarse.bind("<Button-1>", lambda e: self.registro_app())
        

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

    def registro_app(self):
        self.registroVentana = tk.Toplevel(self)
        self.registroVentana.title("Registrar Usuario")
        self.registroVentana.geometry("600x350")
        self.registroVentana.resizable(0, 0)
        
        self.Titlo = tk.Label(self.registroVentana, text="REGISTRO DE USUARIOS").grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="n")

        
        

        

if __name__ == "__main__":
    login = AppLogin()
    login.mainloop()
