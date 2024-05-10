# main ejecutable
# los print() son únicamente para visualizar la ejecución del código y localizar errores

# Para iniciar, se necesita tener instalados:
# python -m pip install mysql-connector-python
# python.exe -m pip install --upgrade pip
# pip install pandas
# pip install sqlalchemy
# pip install sqlalchemy mysql-connector-python
# pip install seaborn
# pip install matplotlip




import tkinter as tk
from tkinter import messagebox

from funciones import *
from home import AppHome

class AppLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Control Escolar")
        self.geometry("500x290")
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):    
        PAD = 10
        self.lbltitulo = tk.Label(self, text="CONTROL ESCOLAR", font=("Arial", 32, "bold"), padx=PAD, pady=PAD)
        self.lbltitulo.grid(row=0, column=0, columnspan=2, sticky="n")
        self.lbltitulo.grid_columnconfigure(0, weight=1)

        self.lblcorreo = tk.Label(self, text="Correo:", font=("Arial", 12), padx=PAD, pady=PAD)
        self.lblcorreo.grid(row=1, column=0, sticky="e")

        self.txcorreo = tk.Entry(self)
        self.txcorreo.grid(row=1, column=1, sticky="w")
        self.txcorreo.config(font=("Arial", 12), width=30)

        self.lblcontraseña = tk.Label(self, text="Contraseña:", font=("Arial", 12), padx=PAD, pady=PAD)
        self.lblcontraseña.grid(row=2, column=0, sticky="e")

        self.txcontrasena = tk.Entry(self, show="*")
        self.txcontrasena.grid(row=2, column=1, sticky="w")
        self.txcontrasena.config(font=("Arial", 12), width= 30)

        self.btnLogin = tk.Button(self, 
                                  text="Iniciar Sesión", 
                                  command=self.abrir_app, 
                                  width=15)
        self.btnLogin.grid(row=3, column=0, columnspan=2, sticky="n")
        self.btnLogin.grid_columnconfigure(0, weight=1)
        self.btnLogin.config(font=("Arial", 12))
        
        self.Registrarse = tk.Label(self, text="¿No estás registrado? Registrate aquí", fg="blue", cursor="hand2", padx=PAD, pady=PAD)
        self.Registrarse.grid(row=4, column=0, columnspan=2, sticky="n")
        self.Registrarse.grid_columnconfigure(0, weight=1)
        self.Registrarse.bind("<Button-1>", lambda e: self.registro_app())
        

    def abrir_app(self):
        correo = self.txcorreo.get()
        contrasena = self.txcontrasena.get()

        usuario = verificar_login(correo, contrasena)
        # [0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status 	

        if usuario:
            self.destroy()  # Cerrar la ventana de inicio de sesión
            home = AppHome(usuario[4], ', '.join(usuario[6]))  # Pasar el argumento 'usuario' a la inicialización de la ventana
            home.mainloop()  # Iniciar el bucle de eventos de la ventana
            
        else:
            messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas.")

    def registro_app(self):
        self.registroVentana = tk.Toplevel(self)
        from registro_app import AppRegistro
        registro = AppRegistro(self.registroVentana)
        registro.grid(row=0, column=0, padx=10, pady=10)


if __name__ == "__main__":
    login = AppLogin()
    login.mainloop()
