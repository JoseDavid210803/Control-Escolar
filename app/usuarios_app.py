import tkinter as tk
from tkinter import END, messagebox, ttk, font
from functions.usuarios_func import UsuariosFunc
import re

class AppUsers(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.usuario = UsuariosFunc()
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.width = 550
        self.height = 550

        tk.Label(self, text="USUARIOS", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

        tk.Label(self, text="ID Usuario:").grid(row=1, column=1)
        self.txBuscarUsuario = tk.Entry(self, width=20)
        self.txBuscarUsuario.grid(row=1, column=2)
        self.btnBuscarUsuario = tk.Button(self, text="Buscar", command=self.buscarUsuario, width=10)
        self.btnBuscarUsuario.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self, text="ID:").grid(row=2, column=0, padx=40, pady=5, sticky="w")
        self.txIdUsuario = tk.Entry(self, width=20)
        self.txIdUsuario.grid(row=2, column=1)
        self.txIdUsuario.config(state="disabled")

        tk.Label(self, text="Nombre:").grid(row=3, column=0, padx=40, pady=5, sticky="w")
        self.txNombreUsuario = tk.Entry(self, width=20)
        self.txNombreUsuario.grid(row=3, column=1)
        self.txNombreUsuario.config(state="disabled")

        tk.Label(self, text="Apellido Paterno:").grid(row=4, column=0, padx=40, pady=5, sticky="w")
        self.txAPaterno = tk.Entry(self, width=20)
        self.txAPaterno.grid(row=4, column=1)
        self.txAPaterno.config(state="disabled")

        tk.Label(self, text="Apellido Materno:").grid(row=5, column=0, padx=40, pady=5, sticky="w")
        self.txAMaterno = tk.Entry(self, width=20)
        self.txAMaterno.grid(row=5, column=1)
        self.txAMaterno.config(state="disabled")

        tk.Label(self, text="Correo:").grid(row=6, column=0, padx=40, pady=5, sticky="w")
        self.txCorreo = tk.Entry(self, width=20)
        self.txCorreo.grid(row=6, column=1)
        self.txCorreo.config(state="disabled")

        tk.Label(self, text="Usuario:").grid(row=2, column=2, padx=40, pady=5, sticky="w")
        self.txUsuario = tk.Entry(self, width=20)
        self.txUsuario.grid(row=2, column=3)
        self.txUsuario.config(state="disabled")

        tk.Label(self, text="Contraseña:").grid(row=3, column=2, padx=40, pady=5, sticky="w")
        self.txContrasena = tk.Entry(self, width=20, show='*')
        self.txContrasena.grid(row=3, column=3)
        self.txContrasena.config(state="disabled")

        profiles_values = ["Maestro", "Alumno"]
        if self.perfil == "Administrador":
            profiles_values.append("Administrador")

        tk.Label(self, text="Perfil:").grid(row=4, column=2, padx=40, pady=5, sticky="w")
        self.cbPerfiles = ttk.Combobox(self, width=20-3, values=profiles_values)
        self.cbPerfiles.grid(row=4, column=3)
        self.cbPerfiles.config(state="disabled")

        tk.Label(self, text="Status:").grid(row=5, column=2, padx=40, pady=5, sticky="w")
        self.cbStatus = ttk.Combobox(self, width=20-3, values=["Activo", "Inactivo"])
        self.cbStatus.grid(row=5, column=3)
        self.cbStatus.config(state="disabled")

        button_width = 10
        padx_between_buttons = 5

        self.btnNuevoUsuario = tk.Button(self, text="Nuevo", width=button_width, command=self.nuevoUsuario)
        self.btnNuevoUsuario.grid(row=11, column=0, padx=(40, padx_between_buttons), pady=5, sticky="ew")

        self.btnGuardarUsuario = tk.Button(self, text="Guardar", width=button_width, command=lambda: self.handle_error_window("Guardar"))
        self.btnGuardarUsuario.grid(row=11, column=1, padx=padx_between_buttons, pady=5, sticky="ew")

        self.btnCancelarUsuario = tk.Button(self, text="Cancelar", width=button_width, command=self.cancelarUsuario)
        self.btnCancelarUsuario.grid(row=11, column=2, padx=padx_between_buttons, pady=5, sticky="ew")

        self.btnEditarUsuario = tk.Button(self, text="Editar", width=button_width, command=self.editarUsuario)
        self.btnEditarUsuario.grid(row=11, column=3, padx=padx_between_buttons, pady=5, sticky="ew")

        self.btnEliminarUsuario = tk.Button(self, text="Eliminar", width=button_width, command=self.deleteUser)
        self.btnEliminarUsuario.grid(row=11, column=4, padx=padx_between_buttons, pady=5, sticky="ew")

        if self.perfil != "Administrador":
            self.btnEliminarUsuario.config(state="disabled")
        
        if self.perfil == "Alumno":
            self.btnNuevoUsuario.config(state="disabled")
            self.btnGuardarUsuario.config(state="disabled")
            self.btnEditarUsuario.config(state="disabled")
            self.btnEliminarUsuario.config(state="disabled")
        elif self.perfil == "Maestro":
            self.btnBuscarUsuario.config(state="normal")
        else:
            pass
            
        self.mostrarProximoID()

    def salir(self):
        self.master.destroy()

    def buscarUsuario(self):
        id = self.txBuscarUsuario.get()
        result = self.usuario.buscarIdUsuario(id)

        print(f"Buscar usuario: <ID: {id}>")
        if result:
            print(result)
            self.cleanUser()
            self.actUser()

            perfil_str = ', '.join(result[7])
            status_str = ', '.join(result[8])

            self.txIdUsuario.config(state="normal")
            self.txIdUsuario.delete(0, END)
            self.txIdUsuario.insert(0, result[0])
            self.txIdUsuario.config(state="readonly")

            self.txNombreUsuario.insert(0, result[1])
            self.txAPaterno.insert(0, result[2])
            self.txAMaterno.insert(0, result[3])
            self.txCorreo.insert(0, result[4])
            self.txUsuario.insert(0, result[5])
            self.txContrasena.insert(0, result[6])

            self.cbPerfiles.config(state="normal")
            self.cbPerfiles.insert(0, perfil_str)
            self.cbPerfiles.config(state="readonly")

            self.cbStatus.config(state="normal")
            self.cbStatus.insert(0, status_str)
            self.cbStatus.config(state="readonly")

            self.deactUser()

            self.btnEditarUsuario.config(state="normal")
            if self.perfil == "Administrador":
                self.btnEliminarUsuario.config(state="normal")

        else:
            print(result)
            messagebox.showwarning("Error", "No existe usuario con ese ID")


    def nuevoUsuario(self):
        print("Nuevo usuario")

        self.cleanUser()
        self.txBuscarUsuario.delete(0, END)
        self.actUser()
        self.txIdUsuario.config(state="normal")
        self.txIdUsuario.config(text= self.usuario.getUltimoId()+1)

        self.btnBuscarUsuario.config(state="disabled")
        self.txBuscarUsuario.config(state="disabled")
        self.btnNuevoUsuario.config(state="disabled")
        self.btnGuardarUsuario.config(state="normal")
        self.btnCancelarUsuario.config(state="normal")
        self.btnEditarUsuario.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarUsuario.config(state="disabled")

    def contrasenaSegura(self, contraseña):
        return len(contraseña) >= 8 and \
               any(c.isupper() for c in contraseña) and \
               any(c.islower() for c in contraseña) and \
               any(c.isdigit() for c in contraseña)

    def correoValido(self, correo):
        return re.match(r"[^@]+@[^@]+\.[^@]+", correo)

    def guardarUsuario(self):
        if self.btnGuardarUsuario.cget("text") == "Crear":
            print("Crear usuario")
            if not self.validarCampos():
                return
            if not self.contrasenaSegura(self.txContrasena.get()):
                messagebox.showwarning("Error", "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")
                return
            if not self.correoValido(self.txCorreo.get()):
                messagebox.showwarning("Error", "El correo electrónico ingresado no es válido.")
                return
            self.usuario.nuevoUsuario(
                self.txNombreUsuario.get(),
                self.txAPaterno.get(),
                self.txAMaterno.get(),
                self.txCorreo.get(),
                self.txUsuario.get(),
                self.txContrasena.get(),
                self.cbPerfiles.get(),
                self.cbStatus.get()
            )

        elif self.btnGuardarUsuario.cget("text") == "Guardar":
            print("Guardar usuario")
            usuario_id = self.txIdUsuario.cget("text")
            try:
                if not self.validarCampos():
                    return
                if not self.correoValido(self.txCorreo.get()):
                    messagebox.showwarning("Error", "El correo electrónico ingresado no es válido.")
                    return
                self.usuario.editarUsuario(
                    usuario_id,
                    self.txNombreUsuario.get(),
                    self.txAPaterno.get(),
                    self.txAMaterno.get(),
                    self.txCorreo.get(),
                    self.txUsuario.get(),
                    self.txContrasena.get(),
                    self.cbPerfiles.get(),
                    self.cbStatus.get()
                )
                self.btnGuardarUsuario.config(text="Crear")
                messagebox.showinfo("Editado", f"El usuario con ID: {usuario_id} ha sido editado")
                self.deactUser()
            except:
                pass

    def validarCampos(self):
        if not self.txNombreUsuario.get() or not self.txAPaterno.get() or not self.txAMaterno.get() or not self.txCorreo.get() or not self.txUsuario.get() or not self.txContrasena.get() or not self.cbPerfiles.get() or not self.cbStatus.get():
            messagebox.showwarning("Error", "Favor de llenar todos los campos")
            return False
        return True

    def cancelarUsuario(self):
        print("Cancelar usuario")

        self.cleanUser()
        self.txIdUsuario.config(state="normal")
        self.txIdUsuario.delete(0, END)
        self.txIdUsuario.config(state="disabled")
        self.btnCancelarUsuario.config(state="disabled")
        self.btnGuardarUsuario.config(state="disabled")
        self.btnEditarUsuario.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarUsuario.config(state="disabled")
        self.btnNuevoUsuario.config(state="normal")
        self.txBuscarUsuario.config(state="normal")
        self.btnBuscarUsuario.config(state="normal")
        self.btnGuardarUsuario.config(text="Crear")

    def editarUsuario(self):
        print("Editar usuario")

        self.actUser()
        if self.correo != self.txCorreo.get():
            self.txContrasena.config(state="disabled")
        self.btnCancelarUsuario.config(state="normal")
        self.btnEditarUsuario.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarUsuario.config(state="normal")
        self.btnGuardarUsuario.config(state="normal")
        self.btnGuardarUsuario.config(text="Guardar")

    def deleteUser(self):
        yesno = messagebox.askyesno("Warning","¿Desea desactivar este usuario?")
        if yesno:
            print("Eliminar usuario")
            self.usuario.desactivarUsuario(self.txIdUsuario.cget("text"))
            user = self.txIdUsuario.cget("text")
            messagebox.showinfo("Desactivado", f"El usuario {user} ha sido desactivado")
            self.cancelarUsuario()

    def cleanUser(self):
        self.actUser()
        self.txIdUsuario.config(text="")
        self.txNombreUsuario.delete(0, END)
        self.txAPaterno.delete(0, END)
        self.txAMaterno.delete(0, END)
        self.txCorreo.delete(0, END)
        self.txUsuario.delete(0, END)
        self.txContrasena.delete(0, END)
        self.cbPerfiles.set('')
        self.cbStatus.set('')
        self.deactUser()

    def actUser(self):
        self.txNombreUsuario.config(state="normal")
        self.txAPaterno.config(state="normal")
        self.txAMaterno.config(state="normal")
        self.txCorreo.config(state="normal")
        self.txUsuario.config(state="normal")
        self.txContrasena.config(state="normal")
        self.cbPerfiles.config(state="readonly")
        self.cbStatus.config(state="readonly")

    def deactUser(self):
        self.txNombreUsuario.config(state="disabled")
        self.txAPaterno.config(state="disabled")
        self.txAMaterno.config(state="disabled")
        self.txCorreo.config(state="disabled")
        self.txUsuario.config(state="disabled")
        self.txContrasena.config(state="disabled")
        self.cbPerfiles.config(state="disabled")
        self.cbStatus.config(state="disabled")
        
    def mostrarProximoID(self):
        usuario_func = UsuariosFunc()
        proximo_id = usuario_func.getUltimoId() + 1
        self.txIdUsuario.config(state="normal")
        self.txIdUsuario.delete(0, END)
        self.txIdUsuario.insert(0, proximo_id)
        self.txIdUsuario.config(state="disabled")

    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Favor de llenar todos los campos")

        if funct == "Guardar":
            if not self.txNombreUsuario.get() or not self.txAPaterno.get() or not self.txAMaterno.get() or not self.txCorreo.get() or not self.txUsuario.get() or not self.txContrasena.get() or not self.cbPerfiles.get() or not self.cbStatus.get():
                warnings()
            else:
                self.guardarUsuario()


if __name__ == "__main__":
    root = tk.Tk()
    usuarios = AppUsers(root, "andre@gmail.com", "Administrador")
    usuarios.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()
