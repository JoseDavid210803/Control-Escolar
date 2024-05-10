import tkinter as tk
from tkinter import END, messagebox, ttk
import re  # Para usar expresiones regulares

from funciones import *

class AppRegistro(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        titleFrame = tk.Frame(self)
        titleFrame.grid(row=0, column=0, sticky="n")
        dataFrame = tk.Frame(self)
        dataFrame.grid(row=1, column=0, sticky="n")
        buttonFrame = tk.Frame(self)
        buttonFrame.grid(row=2, column=0, sticky="s")

        tk.Label(titleFrame, text="REGISTRO", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")
        
        # Texto id
        tk.Label(dataFrame, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txIdUsuario = tk.Entry(dataFrame, width=20)
        self.txIdUsuario.grid(row=2, column=1)
        self.txIdUsuario.config(state="disabled")

        # Casilla nombre
        tk.Label(dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txNombreUsuario = tk.Entry(dataFrame, width=20)
        self.txNombreUsuario.grid(row=3, column=1)

        # Casilla apellido paterno
        tk.Label(dataFrame, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.txAPaterno = tk.Entry(dataFrame, width=20)
        self.txAPaterno.grid(row=4, column=1)

        # Casilla apellido materno
        tk.Label(dataFrame, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.txAMaterno = tk.Entry(dataFrame, width=20)
        self.txAMaterno.grid(row=5, column=1)

        # Casilla correo
        tk.Label(dataFrame, text="Correo:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.txCorreo = tk.Entry(dataFrame, width=20)
        self.txCorreo.grid(row=2, column=3)

        # Casilla contraseña
        tk.Label(dataFrame, text="Contraseña:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
        self.txContrasena = tk.Entry(dataFrame, width=20, show='*')
        self.txContrasena.grid(row=3, column=3)

        # Casilla perfil
        tk.Label(dataFrame, text="Perfil:").grid(row=4, column=2, padx=10, pady=5, sticky="w")
        self.cbPerfiles = ttk.Combobox(dataFrame, width=20-3, values=["Maestro", "Alumno"])
        self.cbPerfiles.grid(row=4, column=3)

        button_width = 10
        BUTTON_PAD = 5

        self.btnNuevoUsuario = tk.Button(buttonFrame, text="Guardar", width=button_width, command=self.registrarUsuario)
        self.btnNuevoUsuario.grid(row=0, column=0, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="n")
        self.btnCancelarUsuario = tk.Button(buttonFrame, text="Cancelar", width=button_width, command=self.cancelarRegistro)
        self.btnCancelarUsuario.grid(row=0, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="n")

        self.mostrarProximoID()

    def contrasenaSegura(self, contraseña):
        # La contraseña debe tener al menos 8 caracteres
        # Al menos una letra mayúscula, una minúscula y un número
        # Y puede contener caracteres especiales
        return len(contraseña) >= 8 and \
               any(c.isupper() for c in contraseña) and \
               any(c.islower() for c in contraseña) and \
               any(c.isdigit() for c in contraseña)

    def correoValido(self, correo):
        # Verifica si el correo contiene el símbolo '@' y al menos un punto después del '@'
        return re.match(r"[^@]+@[^@]+\.[^@]+", correo)

    def registrarUsuario(self):
        nombre = self.txNombreUsuario.get()
        ap_paterno = self.txAPaterno.get()
        ap_materno = self.txAMaterno.get()
        correo = self.txCorreo.get()
        contrasena = self.txContrasena.get()
        perfil = self.cbPerfiles.get()

        if nombre and ap_paterno and ap_materno and correo and contrasena and perfil:
            if not self.contrasenaSegura(contrasena):
                messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula, y un número.")
                return
            if not self.correoValido(correo):
                messagebox.showerror("Error", "El correo electrónico no es válido.")
                return

            # Si todos los campos están llenos y la contraseña y el correo son válidos, guarda el usuario
            status = "Activo"
            nuevoUsuario(nombre, ap_paterno, ap_materno, correo, contrasena, perfil)
            messagebox.showinfo("Registro", "Usuario registrado exitosamente.")
            self.limpiarCampos()
            self.mostrarProximoID()
            self.master.destroy()  # Cierra la ventana actual
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")


    def cancelarRegistro(self):
        self.master.destroy()

    def limpiarCampos(self):
        self.txNombreUsuario.delete(0, END)
        self.txAPaterno.delete(0, END)
        self.txAMaterno.delete(0, END)
        self.txCorreo.delete(0, END)
        self.txUsuario.delete(0, END)
        self.txContrasena.delete(0, END)
        self.cbPerfiles.set('')

    def mostrarProximoID(self):
        proximo_id = getUltimoIdUsuarios() + 1
        self.txIdUsuario.config(state="normal")
        self.txIdUsuario.delete(0, END)
        self.txIdUsuario.insert(0, proximo_id)
        self.txIdUsuario.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("750x350")  # Tamaño fijo de la ventana
    root.resizable(False, False)  # Ventana no redimensionable
    registro = AppRegistro(root)
    registro.pack(fill="both", expand=True)  # Para que se expanda correctamente
    root.mainloop()