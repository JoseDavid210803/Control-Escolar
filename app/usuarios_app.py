import tkinter as tk
from tkinter import END, messagebox, ttk
from functions.usuarios_func import UsuariosFunc


class AppUsers(tk.Tk):
    # Constructor y ventana de usuarios
    def __init__(self, correo, perfil):
        super().__init__()
        self.width = 550
        self.height = 550
        self.title("Control Escolar")
        self.geometry(f"{self.width}x{self.height}")
        self.usuario = UsuariosFunc()

        self.correo = correo
        self.perfil = perfil
        casilla_width = 30

        print("App users")
        

# APLICACIÓN (demo, sólo para verificar funcionamiento) ----------------------------------

        # Casilla buscar usuario
        tk.Label(self,text="ID Usuario:").pack()
        self.txBuscarUsuario=tk.Entry(self, width=20)
        self.txBuscarUsuario.pack()
        
        # Texto id 
        tk.Label(self,text="ID:").pack()
        self.txIdUsuario=tk.Label(self)
        self.txIdUsuario.pack()
        
        # Casilla nombre 
        tk.Label(self,text="Nombre:").pack()
        self.txNombreUsuario=tk.Entry(self, width=casilla_width)
        self.txNombreUsuario.pack()
        self.txNombreUsuario.config(state="disabled")
        
        # Casilla apellido paterno
        tk.Label(self,text="Apellido Paterno:").pack()
        self.txAPaterno=tk.Entry(self, width=casilla_width)
        self.txAPaterno.pack()
        self.txAPaterno.config(state="disabled")
        
        # Casilla apellido materno
        tk.Label(self,text="Apellido Materno:").pack()
        self.txAMaterno=tk.Entry(self, width=casilla_width)
        self.txAMaterno.pack()
        self.txAMaterno.config(state="disabled")
        
        # Casilla correo
        tk.Label(self,text="Correo:").pack()
        self.txCorreo=tk.Entry(self, width=casilla_width)
        self.txCorreo.pack()
        self.txCorreo.config(state="disabled")

        # Casilla usuario
        tk.Label(self,text="Usuario:").pack()
        self.txUsuario=tk.Entry(self, width=casilla_width)
        self.txUsuario.pack()
        self.txUsuario.config(state="disabled")

        # Casilla contrasena
        tk.Label(self,text="Contraseña:").pack()
        self.txContrasena=tk.Entry(self, width=casilla_width, show='*')
        self.txContrasena.pack()
        self.txContrasena.config(state="disabled")

        profiles_values = ["Maestro", "Alumno"]
        if self.perfil == "Administrador":
            profiles_values.append("Administrador")

        # Casilla perfil
        tk.Label(self,text="Perfil:").pack()
        self.cbPerfiles=ttk.Combobox(self, width=casilla_width-3, values=profiles_values)
        self.cbPerfiles.pack()
        self.cbPerfiles.config(state="disabled")
        
        # Casilla status
        tk.Label(self,text="Status:").pack()
        self.cbStatus=ttk.Combobox(self, width=casilla_width-3, values=["Activo", "Inactivo"])
        self.cbStatus.pack()
        self.cbStatus.config(state="disabled")



        # Boton Salir
        #self.btnSalir=tk.Button(self,text="Salir", 
        #                       command=self.salir)
        #self.btnSalir.place(x=0,y=0)
        
        # Boton Buscar
        self.btnBuscarUsuario=tk.Button(self,text="Buscar", 
                                     command=self.buscarUsuario)
        self.btnBuscarUsuario.place(x=340,y=5)
        
        # Nuevo cliente
        self.btnNuevoUsuario=tk.Button(self,text="Nuevo", 
                                  width=8, 
                                  command=self.nuevoUsuario)
        self.btnNuevoUsuario.config(state="normal")
        self.btnNuevoUsuario.place(x=70,y=440)

        # Guardar
        self.btnGuardarUsuario=tk.Button(self,text="Crear", 
                                   width=8, 
                                   command=lambda: self.handle_error_window("Guardar"))
        self.btnGuardarUsuario.config(state="disabled")
        self.btnGuardarUsuario.place(x=150,y=440)

        # Cancelar
        self.btnCancelarUsuario=tk.Button(self,text="Cancelar", 
                                     width=8, 
                                     command=self.cancelarUsuario)
        self.btnCancelarUsuario.config(state="disabled")
        self.btnCancelarUsuario.place(x=230,y=440)

        # Editar
        self.btnEditarUsuario=tk.Button(self,text="Editar", 
                                   width=8, 
                                   command=self.editarUsuario)
        self.btnEditarUsuario.config(state="disabled")
        self.btnEditarUsuario.place(x=310,y=440)
        
        
        if self.perfil == "Administrador":
            # Eliminar
            self.btnEliminarUsuario=tk.Button(self,text="Eliminar", 
                                        width=8, 
                                        command=self.deleteUser)
            self.btnEliminarUsuario.config(state="disabled")
            self.btnEliminarUsuario.place(x=390,y=440)





# FUNCIONES ----------------------------------------------------------------------

    def salir(self):
        # No funciona en caso de utilizar menú despegable, esto es en caso de que se usaran ventanas individuales por cada pantalla
        print("Salir")
        import app.home_app
        app.home_app.AppHome(self.correo)
        self.destroy()

    # Función del botón Buscar Usuario 
    def buscarUsuario(self):
        id = self.txBuscarUsuario.get()
        result = self.usuario.buscarIdUsuario(id)

        print(f"Buscar usuario: <ID: {id}>")
        if result:
            print(result)
            # [0]=id, [1]=nombre, [2]=a_paterno, [3]=a_materno, [4]=correo, [5]=usuario, [6]=contrasena, [7]=perfil, [8]=status
            self.cleanUser()
            self.actUser()

            perfil_str = ', '.join(result[7])
            status_str = ', '.join(result[8])

            self.txIdUsuario.config(text=result[0])
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

    # función nuevo usuario
    # solamente activa casillas y botones, no agrega nada
    def nuevoUsuario(self):
        print("Nuevo usuario")

        self.cleanUser()
        self.txBuscarUsuario.delete(0, END)
        self.actUser()

        self.txIdUsuario.config(text= self.usuario.getUltimoId()+1)

        self.btnBuscarUsuario.config(state="disabled")
        self.txBuscarUsuario.config(state="disabled")
        self.btnNuevoUsuario.config(state="disabled")
        self.btnGuardarUsuario.config(state="normal")
        self.btnCancelarUsuario.config(state="normal")
        self.btnEditarUsuario.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarUsuario.config(state="disabled")


    # función guardar usuario
    def guardarUsuario(self):
        
        # si el botón dice crear, crea un usuario
        if self.btnGuardarUsuario.cget("text") == "Crear":
            print("Crear usuario")
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

        # si el botón dice guardar, lo edita
        elif self.btnGuardarUsuario.cget("text") == "Guardar":
            print("Guardar usuario")
            usuario_id = self.txIdUsuario.cget("text")
            try:
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
                # se regresa el botón al modo "crear"
                self.btnGuardarUsuario.config(text="Crear")
                messagebox.showinfo("Editado",f"El usuario con ID: {usuario_id} ha sido editado")
                self.deactUser()
            except:
                pass

    def cancelarUsuario(self):
        print("Cancelar usuario")
        
        self.cleanUser()
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

        
    # Ventana de errores
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
    usuarios = AppUsers("andre@gmail.com", "Administrador")
    usuarios.mainloop()
