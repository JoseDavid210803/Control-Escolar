import tkinter as tk
from tkinter import Menu, messagebox, END, ttk
from tkcalendar import DateEntry

from funciones import *

ENTRY_WIDTH = 22
BUTTON_WIDTH = 10
BUTTON_PAD = 5

class AppHome(tk.Tk):
    def __init__(self, correo, perfil):
        super().__init__()
        self.title("Control Escolar")
        self.geometry("1000x600")
        #self.resizable(0, 0)
        #self.iconbitmap(r"C:\Users\sofia\Desktop\Control Escolar\img\01.ico")
        self.menu()
        self.inicio()

        self.correo = correo
        self.perfil = perfil
        
    def salir(self):
        self.destroy()

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Esta es una aplicación de Control Escolar.")

    def limpiaVentana(self):
        for widget in self.winfo_children():
            widget.destroy()
            
    def inicio(self):
        self.limpiaVentana()
        self.menu()
        lbltitulo = tk.Label(self, text="CONTROL ESCOLAR", font=("Arial", 32))
        lbltitulo.grid(row=0, column=0, padx=10, pady=10, sticky="we")
        lbltitulo.grid_columnconfigure(0, weight=1)
            
    def menu(self):
        # Crear el menú
        self.limpiaVentana()
        self.menu_principal = Menu(self)
        self.config(menu=self.menu_principal)

        # Crear elementos del menú
        self.menu_archivo = Menu(self.menu_principal, tearoff=0)
        self.menu_archivo.add_command(label="Inicio", command=self.inicio)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Usuarios", command=lambda: self.UsuariosVentana(self.correo, self.perfil))
        self.menu_archivo.add_command(label="Alumnos", command=lambda: self.AlumnosVentana(self.correo, self.perfil))
        self.menu_archivo.add_command(label="Aulas", command=lambda: self.AulasVentana(self.correo, self.perfil))
        self.menu_archivo.add_command(label="Maestros", command=lambda: self.MaestrosVentana(self.correo, self.perfil))
        self.menu_archivo.add_command(label="Materia", command=lambda: self.MateriaVentana(self.correo, self.perfil))
        #self.menu_archivo.add_command(label="Grupos", command=lambda: self.GruposVentana(self.correo, self.perfil))
        self.menu_archivo.add_command(label="Planeación", command=lambda: self.PlaneacionVentana(self.correo, self.perfil))
        #self.menu_archivo.add_command(label="Horarios", command=lambda: self.HorariosVentana(self.correo, self.perfil))
        self.menu_archivo.add_command(label="Carrera", command=lambda: self.CarreraVentana(self.correo, self.perfil))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Menú", menu=self.menu_archivo)
        self.grid_columnconfigure(0, weight=1)
            
    def UsuariosVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu()
        usuarios = AppUsuarios(self, correo, perfil)
        usuarios.grid(row=0, column=0, padx=10, pady=10, sticky="we")
        usuarios.grid_columnconfigure(0, weight=1)
    
    def AlumnosVentana(self, correo, perfil):
        #from app.alumnos_app import AlumnosApp
        self.limpiaVentana()
        self.menu()
        alumnos = AppAlumnos(self, correo, perfil)
        alumnos.grid(row=0, column=0, padx=10, pady=10, sticky="we")
        alumnos.grid_columnconfigure(0, weight=1)
        
    def AulasVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu()  
        aulas = AppAulas(self, correo, perfil)
        aulas.grid(row=0, column=0, padx=10, pady=10)
        aulas.grid_columnconfigure(0, weight=1)

    def MaestrosVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu()
        maestros = AppMaestros(self, correo, perfil)
        maestros.grid(row=0, column=0, padx=10, pady=10, sticky="we")
        maestros.grid_columnconfigure(0, weight=1)
    
    def MateriaVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu()
        materia = AppMaterias(self, correo, perfil)
        materia.grid(row=0, column=0, padx=10, pady=10)
        materia.grid_columnconfigure(0, weight=1)
    
    def GruposVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu() 
        #grupos = AppGrupos(self, "", "")
        #grupos.grid(row=0, column=0, padx=10, pady=10)
        #grupos.grid_columnconfigure(0, weight=1)
        
    def PlaneacionVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu()
        planeacion = AppPlaneacion(self, correo, perfil)
        planeacion.grid(row=0, column=0, padx=10, pady=10)
        planeacion.grid_columnconfigure(0, weight=1)
        
    def HorariosVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu() 

    def CarreraVentana(self, correo, perfil):
        self.limpiaVentana()
        self.menu() 
        carrera = AppCarrera(self, correo, perfil)
        carrera.grid(row=0, column=0, padx=10, pady=10)
        carrera.grid_columnconfigure(0, weight=1)


# -----------------------------------------------------------
# --------------------APP DE USUARIOS------------------------
# -----------------------------------------------------------
class AppUsuarios(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=1, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=2, column=0, sticky="s")

        tk.Label(self.titleFrame, text="USUARIOS", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

        tk.Label(self.dataFrame, text="ID Usuario:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txBuscarUsuario = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txBuscarUsuario.grid(row=1, column=1, sticky="w")
        self.btnBuscarUsuario = tk.Button(self.dataFrame, text="Buscar", command=self.buscarUsuario, width=BUTTON_WIDTH)
        self.btnBuscarUsuario.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self.dataFrame, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txIdUsuario = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txIdUsuario.grid(row=2, column=1, sticky="w")
        self.txIdUsuario.config(state="disabled")

        tk.Label(self.dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNombreUsuario = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txNombreUsuario.grid(row=3, column=1, sticky="w")
        self.txNombreUsuario.config(state="disabled")

        tk.Label(self.dataFrame, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txAPaterno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txAPaterno.grid(row=4, column=1, sticky="w")
        self.txAPaterno.config(state="disabled")

        tk.Label(self.dataFrame, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.txAMaterno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txAMaterno.grid(row=5, column=1, sticky="w")
        self.txAMaterno.config(state="disabled")

        tk.Label(self.dataFrame, text="Correo:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
        self.txCorreo = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txCorreo.grid(row=2, column=3, sticky="w")
        self.txCorreo.config(state="disabled")

        tk.Label(self.dataFrame, text="Contraseña:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txContrasena = tk.Entry(self.dataFrame, width=ENTRY_WIDTH, show='*')
        self.txContrasena.grid(row=3, column=3, sticky="w")
        self.txContrasena.config(state="disabled")

        profiles_values = ["Maestro", "Alumno"]

        tk.Label(self.dataFrame, text="Perfil:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.cbPerfiles = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH-3, values=profiles_values)
        self.cbPerfiles.grid(row=4, column=3, sticky="w")
        self.cbPerfiles.config(state="disabled")

        # Botones
        
        self.btnNuevo = tk.Button(self.buttonFrame, text="Nuevo", width=BUTTON_WIDTH, command=self.nuevoUsuario)
        self.btnNuevo.grid(row=11, column=0, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnNuevo.config(state="disabled")

        self.btnGuardar = tk.Button(self.buttonFrame, text="Guardar", width=BUTTON_WIDTH, command=lambda: self.handle_error_window("Guardar"))
        self.btnGuardar.grid(row=11, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnGuardar.config(state="disabled")

        self.btnCancelar = tk.Button(self.buttonFrame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancelarUsuario)
        self.btnCancelar.grid(row=11, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnCancelar.config(state="disabled")

        self.btnEditar = tk.Button(self.buttonFrame, text="Editar", width=BUTTON_WIDTH, command=self.editarUsuario)
        self.btnEditar.grid(row=11, column=3, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEditar.config(state="disabled")

        self.btnEliminar = tk.Button(self.buttonFrame, text="Eliminar", width=BUTTON_WIDTH, command=self.deleteUser)
        self.btnEliminar.grid(row=11, column=4, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEliminar.config(state="disabled")

        if self.perfil == "Administrador":
            self.btnBuscarUsuario.config(state="normal")
            self.btnNuevo.config(state="normal")
            self.btnGuardar.config(state="disabled")
            self.btnCancelar.config(state="disabled")
            self.btnEditar.config(state="disabled")
            self.btnEliminar.config(state="disabled")

    def buscarUsuario(self):
        id = self.txBuscarUsuario.get()
        result = buscarIdUsuario(id)

        if result:
            self.cleanUser()
            self.actUser()

            self.txIdUsuario.config(state="normal")
            self.txIdUsuario.delete(0, END)
            self.txIdUsuario.insert(0, result[0])
            self.txIdUsuario.config(state="readonly")

            self.txNombreUsuario.insert(0, result[1])
            self.txAPaterno.insert(0, result[2])
            self.txAMaterno.insert(0, result[3])
            self.txCorreo.insert(0, result[4])
            self.txContrasena.insert(0, result[5])

            self.cbPerfiles.config(state="normal")
            self.cbPerfiles.insert(0, result[6])
            self.cbPerfiles.config(state="readonly")

            self.deactUser()

            if self.perfil != "Administrador":
                if self.correo == self.txCorreo.get():
                    self.btnGuardar.config(state="disabled")
                    self.btnCancelar.config(state="disabled")
                    self.btnEditar.config(state="normal")
                else: 
                    self.btnGuardar.config(state="disabled")
                    self.btnCancelar.config(state="disabled")
                    self.btnEditar.config(state="disabled")
                
            if self.perfil == "Administrador":
                self.btnNuevo.config(state="normal")
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="disabled")
                self.btnEditar.config(state="normal")
                self.btnEliminar.config(state="normal")

        else:
            messagebox.showwarning("Error", "No existe usuario con ese ID")


    def nuevoUsuario(self):
        self.cleanUser()
        self.txBuscarUsuario.delete(0, END)
        self.actUser()
        self.mostrarProximoID()

        self.btnBuscarUsuario.config(state="disabled")
        self.txBuscarUsuario.config(state="disabled")
        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")
        self.btnGuardar.config(text="Crear")

    def contrasenaSegura(self, contraseña):
        return len(contraseña) >= 8 and \
               any(c.isupper() for c in contraseña) and \
               any(c.islower() for c in contraseña) and \
               any(c.isdigit() for c in contraseña)

    def correoValido(self, correo):
        return re.match(r"[^@]+@[^@]+\.[^@]+", correo)

    def guardarUsuario(self):
        nombre = str(self.txNombreUsuario.get())
        a_Paterno = str(self.txAPaterno.get())
        a_Materno = str(self.txAMaterno.get())
        correo = str(self.txCorreo.get())
        contrasena= str(self.txContrasena.get())
        perfil = str(self.cbPerfiles.get())
        if self.btnGuardar.cget("text") == "Crear":
            if not self.validarCampos():
                return
            if not self.contrasenaSegura(self.txContrasena.get()):
                messagebox.showwarning("Error", "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")
                return
            if not self.correoValido(self.txCorreo.get()):
                messagebox.showwarning("Error", "El correo electrónico ingresado no es válido.")
                return
            nuevoUsuario(nombre,a_Paterno,a_Materno,correo,contrasena,perfil)
            messagebox.showinfo("Creado", "Usuario creado")
            self.deactUser()

        elif self.btnGuardar.cget("text") == "Guardar":
            usuario_id = self.txIdUsuario.get()
            try:
                if self.validarCampos():
                    if not self.correoValido(self.txCorreo.get()):
                        messagebox.showwarning("Error", "El correo electrónico ingresado no es válido.")
                        return
                    editarUsuario(usuario_id,nombre,a_Paterno,a_Materno,correo,contrasena,perfil)
                    if self.perfil == "Administrador":
                        self.btnGuardar.config(text="Crear")
                    messagebox.showinfo("Editado", f"El usuario con ID: {usuario_id} ha sido editado")
                    self.deactUser()
            except Exception as e:
                messagebox.showerror("Error", e)

    def validarCampos(self):
        if not self.txNombreUsuario.get() or not self.txAPaterno.get() or not self.txAMaterno.get() or not self.txCorreo.get() or not self.txContrasena.get() or not self.cbPerfiles.get():
            messagebox.showwarning("Error", "Favor de llenar todos los campos")
            return False
        return True

    def cancelarUsuario(self):
        self.cleanUser()
        self.txIdUsuario.config(state="normal")
        self.txIdUsuario.delete(0, END)
        self.txIdUsuario.config(state="disabled")
        self.txBuscarUsuario.config(state="normal")
        self.btnCancelar.config(state="disabled")
        self.btnGuardar.config(state="disabled")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")
        self.btnNuevo.config(state="normal")
        self.btnBuscarUsuario.config(state="normal")
        self.btnGuardar.config(text="Crear")

    def editarUsuario(self):
        self.actUser()
        self.txContrasena.config(state="disabled")
        if self.correo == self.txCorreo.get():
            self.txContrasena.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminar.config(state="normal")
        self.btnGuardar.config(state="normal")
        self.btnGuardar.config(text="Guardar")

    def deleteUser(self):
        yesno = messagebox.askyesno("Warning","¿Desea desactivar este usuario?")
        if yesno:
            print("Eliminar usuario")
            desactivarUsuario(self.txIdUsuario.cget("text"))
            user = self.txIdUsuario.cget("text")
            messagebox.showinfo("Desactivado", f"El usuario {user} ha sido desactivado")
            self.cancelarUsuario()

    def cleanUser(self):
        self.actUser()
        self.txBuscarUsuario.delete(0, END)
        self.txIdUsuario.delete(0, END)
        self.txNombreUsuario.delete(0, END)
        self.txAPaterno.delete(0, END)
        self.txAMaterno.delete(0, END)
        self.txCorreo.delete(0, END)
        self.txContrasena.delete(0, END)
        self.cbPerfiles.set('')
        self.deactUser()

    def actUser(self):
        self.txNombreUsuario.config(state="normal")
        self.txAPaterno.config(state="normal")
        self.txAMaterno.config(state="normal")
        self.txCorreo.config(state="normal")
        self.txContrasena.config(state="normal")
        self.cbPerfiles.config(state="readonly")

    def deactUser(self):
        self.txNombreUsuario.config(state="disabled")
        self.txAPaterno.config(state="disabled")
        self.txAMaterno.config(state="disabled")
        self.txCorreo.config(state="disabled")
        self.txContrasena.config(state="disabled")
        self.cbPerfiles.config(state="disabled")
        
    def mostrarProximoID(self):
        proximo_id = getUltimoIdUsuarios() + 1
        self.txIdUsuario.config(state="normal")
        self.txIdUsuario.delete(0, END)
        self.txIdUsuario.insert(0, proximo_id)
        self.txIdUsuario.config(state="disabled")

    def handle_error_window(self, funct=""):
        def warnings():
            print(f"Error, {funct}")
            messagebox.showwarning("Error", "Favor de llenar todos los campos")
        if funct == "Guardar":
            if not self.txNombreUsuario.get() or not self.txAPaterno.get() or not self.txAMaterno.get() or not self.txCorreo.get() or not self.txContrasena.get() or not self.cbPerfiles.get():
                warnings()
            else:
                self.guardarUsuario()
        

# -----------------------------------------------------------
# ---------------------APP DE ALUMNOS------------------------
# -----------------------------------------------------------
class AppAlumnos(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=1, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=2, column=0, sticky="s")

        tk.Label(self.titleFrame, text="ALUMNOS", font=("Arial", 20)).grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

        tk.Label(self.dataFrame, text="Buscar por ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIdUsuario = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txIdUsuario.grid(row=1, column=1, sticky="w")
        self.btnBuscarUsuario = tk.Button(self.dataFrame, text="Buscar", command=self.buscarAlumno, width=BUTTON_WIDTH)
        self.btnBuscarUsuario.grid(row=1, column=2, padx=10, pady=5)

        # Etiquetas y entradas para mostrar información del alumno
        tk.Label(self.dataFrame, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txIdAlumno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txIdAlumno.grid(row=2, column=1, sticky="w")
        self.txIdAlumno.config(state="disabled")

        tk.Label(self.dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNombre = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txNombre.grid(row=3, column=1, sticky="w")
        self.txNombre.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txAPaterno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txAPaterno.grid(row=4, column=1, sticky="w")
        self.txAPaterno.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.txAMaterno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txAMaterno.grid(row=5, column=1, sticky="w")
        self.txAMaterno.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Correo:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
        self.txCorreo = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txCorreo.grid(row=2, column=3, sticky="w")
        self.txCorreo.config(state="disabled")

        tk.Label(self.dataFrame, text="Carrera:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.comboCarrera = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH)  
        self.comboCarrera.grid(row=3, column=3, sticky="w")
        carreraValues = []
        for carrera in getListaCarreras():
            carreraValues.append(', '.join(carrera))
        self.comboCarrera['values'] = carreraValues
        self.comboCarrera.config(state="disabled")

        #tk.Label(self.dataFrame, text="Grupo:").grid(row=4, column=2, padx=10, pady=5, #sticky="e")
        #self.comboGrupo = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH)  
        #self.comboGrupo.grid(row=4, column=3, sticky="w")
        #grupoValues = []
        #for grupo in getListaGrupos():
        #    grupoValues.append(grupo[1])
        #self.comboGrupo['values'] = grupoValues
        #self.comboGrupo.config(state="disabled")

        tk.Label(self.dataFrame, text="Fecha de Nac:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.calendario = DateEntry(self.dataFrame, selectmode='day', date_pattern='yyyy-MM-dd', width=ENTRY_WIDTH)
        self.calendario.grid(row=4, column=3, sticky="w")
        self.calendario.config(state="disabled")

        # Botones

        self.btnGuardar = tk.Button(self.buttonFrame, text="Guardar", width=BUTTON_WIDTH, command=self.guardarAlumno)
        self.btnGuardar.grid(row=11, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnGuardar.config(state="disabled")

        self.btnCancelar = tk.Button(self.buttonFrame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancelarAccion)
        self.btnCancelar.grid(row=11, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnCancelar.config(state="disabled")

        self.btnEditar = tk.Button(self.buttonFrame, text="Editar", width=BUTTON_WIDTH, command=self.editarAlumno)
        self.btnEditar.grid(row=11, column=3, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEditar.config(state="disabled")

    def buscarAlumno(self):
        id = self.txIdUsuario.get()
        result = buscarIdAlumno(id)

        if result:
            self.cleanAlumno()
            self.actAlumno()

            self.txIdAlumno.insert(0, result[0])
            self.txNombre.insert(0, result[6])
            self.txAPaterno.insert(0, result[7])
            self.txAMaterno.insert(0, result[8])
            self.txCorreo.insert(0, result[9])

            self.comboCarrera.config(state="normal")
            if result[1] == None:
                self.comboCarrera.insert(0, "")
            else:
                self.comboCarrera.insert(0, result[1])
            self.comboCarrera.config(state="readonly")

            #self.comboGrupo.config(state="normal")
            #if result[2] == None:
                #self.comboGrupo.insert(0, "")
            #else:
                #self.comboGrupo.insert(0, result[2])
            #self.comboGrupo.config(state="readonly")

            if result[4] == None:
                self.calendario.insert(0, "")
            else:
                self.calendario.insert(0, result[4])
            self.deactAlumno()

            if self.perfil != "Administrador":
                if self.correo == self.txCorreo.get() and self.perfil == "Alumno":
                    self.btnGuardar.config(state="disabled")
                    self.btnCancelar.config(state="disabled")
                    self.btnEditar.config(state="normal")
                else: 
                    self.btnGuardar.config(state="disabled")
                    self.btnCancelar.config(state="disabled")
                    self.btnEditar.config(state="disabled")
                
            if self.perfil == "Administrador":
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="disabled")
                self.btnEditar.config(state="normal")
        else:
            messagebox.showwarning("Error", "No existe alumno con ese ID")

    def editarAlumno(self):
        self.actAlumno()
        self.txIdAlumno.config(state="disabled")
        self.txNombre.config(state="disabled")
        self.txAPaterno.config(state="disabled")
        self.txAMaterno.config(state="disabled")
        self.txCorreo.config(state="disabled")
        
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")

    def guardarAlumno(self):
        id_alumno = self.txIdAlumno.get()
        id_usuario = getIdUsuarioDeAlumno(id_alumno)
        nombre_carrera = self.comboCarrera.get()
        #id_grupo = self.comboGrupo.get()
        fecha_nacimiento = self.calendario.get_date()

        editarAlumno(id_alumno, nombre_carrera, id_usuario, fecha_nacimiento)
        messagebox.showinfo("Éxito", "Alumno guardado correctamente")
        self.deactAlumno()

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="normal")

    def cancelarAccion(self):
        self.cleanAlumno()
        
        self.txIdAlumno.config(state="normal")
        self.txIdAlumno.delete(0, END)
        self.txIdAlumno.config(state="disabled")
        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnEditar.config(state="disabled")

    def eliminarAlumno(self):   
        yesno = messagebox.askyesno("Confirmación","¿Quieres eliminar a este alumno?")
        if yesno:
            id_alumno = self.txIdAlumno.get()
            id_usuario = getIdUsuarioDeAlumno(id_alumno)
            desactivarUsuario(id_usuario)
            messagebox.showinfo("Éxito", "Alumno dado de baja correctamente")
            self.cancelarAccion()
        
    def cleanAlumno(self):
        self.actAlumno()
        self.txIdUsuario.delete(0, END)
        self.txIdAlumno.delete(0, END)
        self.txNombre.delete(0, END)
        self.txAPaterno.delete(0, END)
        self.txAMaterno.delete(0, END)
        self.txCorreo.delete(0, END)
        self.comboCarrera.set('')
        #self.comboGrupo.set('')
        self.calendario.delete(0, END)
        self.deactAlumno()

    def actAlumno(self):
        self.txIdAlumno.config(state="normal")
        self.txNombre.config(state="normal")
        self.txAPaterno.config(state="normal")
        self.txAMaterno.config(state="normal")
        self.txCorreo.config(state="normal")
        self.comboCarrera.config(state="readonly")
        #self.comboGrupo.config(state="readonly")
        self.calendario.config(state="normal")

    def deactAlumno(self):
        self.txIdAlumno.config(state="disabled")
        self.txNombre.config(state="disabled")
        self.txAPaterno.config(state="disabled")
        self.txAMaterno.config(state="disabled")
        self.txCorreo.config(state="disabled")
        self.comboCarrera.config(state="disabled")
        #self.comboGrupo.config(state="disabled")
        self.calendario.config(state="disabled")


# -----------------------------------------------------------
# ---------------------APP DE MAESTROS------------------------
# -----------------------------------------------------------
class AppMaestros(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=1, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=2, column=0, sticky="s")

        tk.Label(self.titleFrame, text="MAESTROS", font=("Arial", 20)).grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

        tk.Label(self.dataFrame, text="Buscar por ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txIdBuscar = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txIdBuscar.grid(row=1, column=1, sticky="w")
        self.btnBuscarUsuario = tk.Button(self.dataFrame, text="Buscar", command=self.buscarMaestro, width=BUTTON_WIDTH)
        self.btnBuscarUsuario.grid(row=1, column=2, padx=10, pady=5)

        # Etiquetas y entradas para mostrar información del Maestro
        tk.Label(self.dataFrame, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txIdMaestro = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txIdMaestro.grid(row=2, column=1, sticky="w")
        self.txIdMaestro.config(state="disabled")

        tk.Label(self.dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNombre = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txNombre.grid(row=3, column=1, sticky="w")
        self.txNombre.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.txAPaterno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txAPaterno.grid(row=4, column=1, sticky="w")
        self.txAPaterno.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.txAMaterno = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txAMaterno.grid(row=5, column=1, sticky="w")
        self.txAMaterno.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Correo:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
        self.txCorreo = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txCorreo.grid(row=2, column=3, sticky="w")
        self.txCorreo.config(state="disabled")

        tk.Label(self.dataFrame, text="Estudios:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.comboEstudios = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH)  
        self.comboEstudios.grid(row=3, column=3, sticky="w")
        estudiosValues = ["Licenciatura", "Normal Superior", "Maestría", "Doctorado", "Especialización"]
        self.comboEstudios['values'] = estudiosValues
        self.comboEstudios.config(state="disabled")


        # Botones
        self.btnGuardar = tk.Button(self.buttonFrame, text="Guardar", width=BUTTON_WIDTH, command=self.guardarMaestro)
        self.btnGuardar.grid(row=11, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnGuardar.config(state="disabled")

        self.btnCancelar = tk.Button(self.buttonFrame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancelarAccion)
        self.btnCancelar.grid(row=11, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnCancelar.config(state="disabled")

        self.btnEditar = tk.Button(self.buttonFrame, text="Editar", width=BUTTON_WIDTH, command=self.editarMaestro)
        self.btnEditar.grid(row=11, column=3, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEditar.config(state="disabled")

    def buscarMaestro(self):
        id = self.txIdBuscar.get()
        result = buscarIdMaestro(id)

        if result:
            self.cleanMaestro()
            self.actMaestro()
            self.txIdMaestro.insert(0, result[0])
            self.txNombre.insert(0, result[5])
            self.txAPaterno.insert(0, result[6])
            self.txAMaterno.insert(0, result[7])
            self.txCorreo.insert(0, result[8])

            self.comboEstudios.config(state="normal")
            if result[3] == None:
                self.comboEstudios.insert(0, "")
            else:
                self.comboEstudios.insert(0, result[3])
            self.comboEstudios.config(state="readonly")

            self.deactMaestro()
            
            if self.perfil != "Administrador":
                if self.correo == self.txCorreo.get() and self.perfil == "Maestro":
                    self.btnGuardar.config(state="disabled")
                    self.btnCancelar.config(state="disabled")
                    self.btnEditar.config(state="normal")
                else: 
                    self.btnGuardar.config(state="disabled")
                    self.btnCancelar.config(state="disabled")
                    self.btnEditar.config(state="disabled")
                
            if self.perfil == "Administrador":
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="disabled")
                self.btnEditar.config(state="normal")
        else:
            messagebox.showwarning("Error", "No existe Maestro con ese ID")

    def editarMaestro(self):
        self.actMaestro()
        self.txIdMaestro.config(state="disabled")
        self.txNombre.config(state="disabled")
        self.txAPaterno.config(state="disabled")
        self.txAMaterno.config(state="disabled")
        self.txCorreo.config(state="disabled")
        
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")

    def guardarMaestro(self):
        id_maestro = self.txIdMaestro.get()
        id_usuario = getIdUsuarioDeMaestro(id_maestro)
        estudios = self.comboEstudios.get()

        editarMaestro(id_maestro, id_usuario, estudios)
        messagebox.showinfo("Éxito", "Maestro guardado correctamente")
        self.deactMaestro()

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="normal")

    def cancelarAccion(self):
        self.cleanMaestro()
        
        self.txIdBuscar.config(state="normal")
        self.txIdBuscar.delete(0, END)
        self.txIdBuscar.config(state="disabled")
        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnEditar.config(state="disabled")

    def eliminarMaestro(self):   
        yesno = messagebox.askyesno("Confirmación","¿Quieres eliminar a este Maestro?")
        if yesno:
            id_Maestro = self.txIdMaestro.get()
            id_usuario = getIdUsuarioDeMaestro(id_Maestro)
            desactivarUsuario(id_usuario)
            messagebox.showinfo("Éxito", "Maestro dado de baja correctamente")
            self.cancelarAccion()
        
    def cleanMaestro(self):
        self.actMaestro()
        self.txIdBuscar.delete(0, END)
        self.txIdMaestro.delete(0, END)
        self.txIdMaestro.delete(0, END)
        self.txNombre.delete(0, END)
        self.txAPaterno.delete(0, END)
        self.txAMaterno.delete(0, END)
        self.txCorreo.delete(0, END)
        self.comboEstudios.set('')
        self.deactMaestro()

    def actMaestro(self):
        self.txIdMaestro.config(state="normal")
        self.txNombre.config(state="normal")
        self.txAPaterno.config(state="normal")
        self.txAMaterno.config(state="normal")
        self.txCorreo.config(state="normal")
        self.comboEstudios.config(state="readonly")

    def deactMaestro(self):
        self.txIdMaestro.config(state="disabled")
        self.txNombre.config(state="disabled")
        self.txAPaterno.config(state="disabled")
        self.txAMaterno.config(state="disabled")
        self.txCorreo.config(state="disabled")
        self.comboEstudios.config(state="disabled")


# -----------------------------------------------------------
# ---------------------APP DE CARRERA------------------------
# -----------------------------------------------------------
class AppCarrera(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=1, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=2, column=0, sticky="s")

        tk.Label(self.titleFrame, text="CARRERA", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

        # Casilla buscar carrera
        carrerasLista = []
        for carrera in getListaCarreras():
            carrerasLista.append(', '.join(carrera))
        tk.Label(self.dataFrame, text="Buscar Carrera:").grid(row=1, column=0, sticky="e")
        self.comboBuscarCarrera = ttk.Combobox(self.dataFrame, width=35, values=carrerasLista)
        self.comboBuscarCarrera.grid(row=1, column=1, columnspan=2, sticky="w")
        # Boton Buscar
        self.btnBuscarCarrera = tk.Button(self.dataFrame, text="Buscar", command=self.buscarCarrera, width=BUTTON_WIDTH)
        self.btnBuscarCarrera.grid(row=1, column=3)

        tk.Label(self.dataFrame, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txIdCarrera = tk.Entry(self.dataFrame, width=10)
        self.txIdCarrera.grid(row=2, column=1, sticky="w")
        self.txIdCarrera.config(state="disabled")

        tk.Label(self.dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNombreCarrera = tk.Entry(self.dataFrame, width=ENTRY_WIDTH*2)
        self.txNombreCarrera.grid(row=3, column=1, columnspan=3, sticky="w")
        self.txNombreCarrera.config(state="disabled")

        tk.Label(self.dataFrame, text="Semestre:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
        # Combobox para mostrar los semestres como opciones
        self.cbSemestre = ttk.Combobox(self.dataFrame, width=10, state="disabled", values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.cbSemestre.grid(row=2, column=3, pady=5, sticky="w")

        # Nuevo carrera
        self.btnNuevo = tk.Button(self.buttonFrame, text="Nuevo", width=BUTTON_WIDTH, command=self.nuevaCarrera)
        self.btnNuevo.grid(row=11, column=0, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnNuevo.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnNuevo.config(state="normal")

        # Guardar
        self.btnGuardar = tk.Button(self.buttonFrame, text="Crear", width=BUTTON_WIDTH, command=self.guardarCarrera)
        self.btnGuardar.grid(row=11, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnGuardar.config(state="disabled")

        # Cancelar
        self.btnCancelar = tk.Button(self.buttonFrame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancelarCarrera)
        self.btnCancelar.grid(row=11, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnCancelar.config(state="disabled")

        # Editar
        self.btnEditar = tk.Button(self.buttonFrame, text="Editar", width=BUTTON_WIDTH, command=self.editarCarrera)
        self.btnEditar.grid(row=11, column=3, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEditar.config(state="disabled")

        # Eliminar
        self.btnEliminar = tk.Button(self.buttonFrame, text="Eliminar", width=BUTTON_WIDTH, command=self.eliminarCarrera)
        self.btnEliminar.grid(row=11, column=4, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEliminar.config(state="disabled")


    def buscarCarrera(self):
        nombre_carrera = self.comboBuscarCarrera.get()
        carrera = buscarNombreCarrera(nombre_carrera)
        # [0]=id_carrera, [1]=nombre, [2]=semestre
        if carrera:
            self.cleanCarrera()
            self.actCarrera()

            self.txIdCarrera.insert(0, carrera[0])
            self.txNombreCarrera.insert(0, carrera[1])

            self.cbSemestre.config(state="normal")
            self.cbSemestre.insert(0, carrera[2])
            self.cbSemestre.config(state="readonly")
            
            self.deactCarrera()

            if self.perfil == "Administrador":
                self.btnNuevo.config(state="normal")
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="disabled")
                self.btnEditar.config(state="normal")
                self.btnEliminar.config(state="normal")
        else:
            messagebox.showwarning("Carrera no encontrada", "No se encontró ninguna carrera con el nombre proporcionado.")


    def nuevaCarrera(self):
        self.cleanCarrera()
        self.actCarrera()

        self.txIdCarrera.insert(0, getUltimoIdCarreras() + 1)

        self.txIdCarrera.config(state="disabled")
        self.cbSemestre.config(state="readonly")

        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")
        
        self.btnGuardar.config(text="Crear")

    def guardarCarrera(self):
        nombre = self.txNombreCarrera.get()
        semestre = self.cbSemestre.get()
        if nombre and semestre:
            if self.btnGuardar.cget("text") == "Crear":
                nuevaCarrera(nombre, semestre)
                messagebox.showinfo("Carrera creada", "La carrera ha sido creada exitosamente.")
                self.btnGuardar.config(text="Guardar")
            elif self.btnGuardar.cget("text") == "Guardar":
                id_carrera = self.txIdCarrera.get()
                editarCarrera(id_carrera, nombre, semestre)
                messagebox.showinfo("Carrera actualizada", "La carrera ha sido actualizada exitosamente.")

            self.deactCarrera()

            if self.perfil == "Administrador":
                self.btnNuevo.config(state="normal")
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="normal")
                self.btnEditar.config(state="disabled")
                self.btnEliminar.config(state="disabled")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete los campos")
            

    def cancelarCarrera(self):
        self.cleanCarrera()
        self.deactCarrera()

        self.btnNuevo.config(state="normal")
        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")

    def editarCarrera(self):
        self.actCarrera()
        self.txIdCarrera.config(state="disabled")

        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")

    def eliminarCarrera(self):
        id_carrera = self.txIdCarrera.get()
        yesno = messagebox.askyesno("Warning","¿Desea eliminar esta carrera?")
        if yesno:
            eliminarCarrera(id_carrera)
            messagebox.showinfo("Carrera eliminada", f"La carrera con ID {id_carrera} ha sido eliminada.")
            self.cancelarCarrera()
            
    def cleanCarrera(self):
        self.actCarrera()
        self.comboBuscarCarrera.set('')
        self.txIdCarrera.delete(0, END)
        self.txNombreCarrera.delete(0, END)
        self.cbSemestre.set('')
        self.deactCarrera()

    def actCarrera(self):
        self.txIdCarrera.config(state="normal")
        self.txNombreCarrera.config(state="normal")
        self.cbSemestre.config(state="readonly")

    def deactCarrera(self):
        self.txIdCarrera.config(state="disabled")
        self.txNombreCarrera.config(state="disabled")
        self.cbSemestre.config(state="disabled")

        
# -----------------------------------------------------------
# ---------------------APP DE MATERIA------------------------
# -----------------------------------------------------------
class AppMaterias(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame1 = tk.Frame(self)
        self.dataFrame1.grid(row=1, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=2, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=3, column=0, sticky="s")
        self.separatorFrame = tk.Frame(self)
        self.separatorFrame.grid(row=4, column=0, columnspan=2, sticky="s")
        self.dataFrame2 = tk.Frame(self)
        self.dataFrame2.grid(row=5, column=0, sticky="n")
        self.frame_form = tk.Frame(self)
        self.frame_form.grid(row=6, column=0,sticky="s")

        self.lbl_titulo = tk.Label(self.titleFrame, text="Gestión de Materias", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="n")


        tk.Label(self.dataFrame1, text="Buscar ID Materia:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txBuscarMateria = tk.Entry(self.dataFrame1, width=ENTRY_WIDTH)
        self.txBuscarMateria.grid(row=1, column=1, sticky="w")
        self.btnBuscarMateria = tk.Button(self.dataFrame1, text="Buscar", command=self.buscarMateria, width=BUTTON_WIDTH)
        self.btnBuscarMateria.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self.dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNombreMateria = tk.Entry(self.dataFrame, width=30)
        self.txNombreMateria.grid(row=3, column=1, sticky="w")
        self.txNombreMateria.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Maestro:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        profeValues = []
        for maestro in getListaUsuariosMaestros():
            profeValues.append(maestro[1]+" "+ maestro[2]+" "+ maestro[3])
        self.comboNombreMaestro = ttk.Combobox(self.dataFrame, width=30, values=profeValues)
        self.comboNombreMaestro.grid(row=4, column=1, sticky="w")
        self.comboNombreMaestro.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Aula:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        listaAulas = []
        for aula in getListaAulas():
            listaAulas.append(aula[1]+"-"+aula[2])
        self.comboAula = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH, values=listaAulas)
        self.comboAula.grid(row=5, column=1, sticky="w")
        self.comboAula.config(state="disabled")

        tk.Label(self.dataFrame, text="Semestre:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.comboSemestre = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.comboSemestre.grid(row=6, column=1, sticky="w")
        self.comboSemestre.config(state="disabled")

        tk.Label(self.dataFrame, text="Hora entrada:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.txHoraEnt = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txHoraEnt.grid(row=3, column=3, sticky="w")
        self.txHoraEnt.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Hora salida:").grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.txHoraSal = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txHoraSal.grid(row=4, column=3, sticky="w")
        self.txHoraSal.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Día:").grid(row=5, column=2, padx=10, pady=5, sticky="e")
        self.comboDia = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH, values=['Lunes','Martes','Miércoles','Jueves','Viernes'])
        self.comboDia.grid(row=5, column=3, sticky="w")
        self.comboDia.config(state="disabled")
        
        tk.Label(self.dataFrame, text="Créditos:").grid(row=6, column=2, padx=10, pady=5, sticky="e")
        self.txCreditos = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txCreditos.grid(row=6, column=3, sticky="w")
        self.txCreditos.config(state="disabled")        

        tk.Label(self.dataFrame, text="Carrera:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
        carreraValues = []
        for carrera in getListaCarreras():
            carreraValues.append(', '.join(carrera))
        self.comboCarrera = ttk.Combobox(self.dataFrame, width=30, values=carreraValues)
        self.comboCarrera.grid(row=7, column=1, sticky="w")
        self.comboCarrera.config(state="disabled")


        # Botones
        
        self.btnNuevo = tk.Button(self.buttonFrame, text="Nuevo", width=BUTTON_WIDTH, command=self.nuevaMateria)
        self.btnNuevo.grid(row=11, column=0, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnNuevo.config(state="disabled")

        self.btnGuardar = tk.Button(self.buttonFrame, text="Guardar", width=BUTTON_WIDTH, command=self.guardarMateria)
        self.btnGuardar.grid(row=11, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnGuardar.config(state="disabled")

        self.btnCancelar = tk.Button(self.buttonFrame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancelarMateria)
        self.btnCancelar.grid(row=11, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnCancelar.config(state="disabled")

        self.btnEditar = tk.Button(self.buttonFrame, text="Editar", width=BUTTON_WIDTH, command=self.editarMateria)
        self.btnEditar.grid(row=11, column=3, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEditar.config(state="disabled")

        self.btnEliminar = tk.Button(self.buttonFrame, text="Eliminar", width=BUTTON_WIDTH, command=self.deleteMateria)
        self.btnEliminar.grid(row=11, column=4, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEliminar.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnNuevo.config(state="normal")
            self.btnGuardar.config(state="disabled")
            self.btnCancelar.config(state="disabled")
            self.btnEditar.config(state="disabled")
            self.btnEliminar.config(state="disabled")


        ttk.Separator(self.dataFrame2, orient="horizontal").grid(row=0, column=0, columnspan=4, sticky="ew", pady=15)

        carrerasLista = []
        for carrera in getListaCarreras():
            carrerasLista.append(', '.join(carrera))
        tk.Label(self.dataFrame2, text="Buscar Materias de Carrera:").grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.comboBuscarDeCarrera = ttk.Combobox(self.dataFrame2, width=30, values=carrerasLista)
        self.comboBuscarDeCarrera.grid(row=1, column=1, sticky="ew")
        self.btnBuscarDeCarrera = tk.Button(self.dataFrame2, text="Buscar", command=self.buscarDeCarrera, width=BUTTON_WIDTH)
        self.btnBuscarDeCarrera.grid(row=1, column=2, padx=10, pady=5)

        # Tabla para mostrar las materias
        self.tree = ttk.Treeview(self.frame_form, columns=('','ID','Nombre','Maestro','Aula','Día','Hora Entrada','Hora Salida','Semestre','Carrera','Creditos'))
        self.tree.heading('#0', text='')
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Maestro')
        self.tree.heading('#4', text='Aula')
        self.tree.heading('#5', text='Día')
        self.tree.heading('#6', text='Entrada')
        self.tree.heading('#7', text='Salida')
        self.tree.heading('#8', text='Semestre')
        self.tree.heading('#9', text='Carrera')
        self.tree.heading('#10', text='Creditos')
        self.tree.column('#0', width=0)
        self.tree.column('#1', width=15)
        self.tree.column('#2', width=200)
        self.tree.column('#3', width=160)
        self.tree.column('#4', width=75)
        self.tree.column('#5', width=60)
        self.tree.column('#6', width=50)
        self.tree.column('#7', width=50)
        self.tree.column('#8', width=60)
        self.tree.column('#9', width=175)
        self.tree.column('#10', width=70)
        self.tree.grid(row=5, column=0)

        self.cargar_materias()
        
        self.btnBuscarMateria.config(state="normal")
        self.btnBuscarDeCarrera.config(state="normal")


    def cargar_materias(self):
        self.limpiarTabla()
        # Obtener la lista de materias desde la base de datos
        materias = getListaMaterias()
        # n = atributos ([0]=id_materia, [1]=nombre, [2]=horario_entrada, [3]=horario_salida, [4]=dia, [5]=maestro, [6]=aula, [7]=creditos, [8]=semestre, [9]=carrera)
        # Insertar las materias en la tabla
        for materia in materias:
            self.tree.insert("", END, values=[materia[0], materia[1], materia[5], materia[6], materia[4], materia[2], materia[3], materia[8], materia[9], materia[7]])
        
    def limpiarTabla(self):
        # Limpiar la tabla antes de cargar los datos
        for record in self.tree.get_children():
            self.tree.delete(record)


    def buscarMateria(self):
        id = self.txBuscarMateria.get()
        result = buscarIdMateria(id)
        # [0]=id_materia, [1]=nombre, [2]=horario_entrada, [3]=horario_salida, [4]=dia, [5]=maestro, [6]=aula, [7]=creditos, [8]=semestre, [9]=carrera
        
        if result:
            self.cleanMateria()
            self.actMateria()
            self.txBuscarMateria.insert(0, id)
            self.txBuscarMateria.config(state="disabled")
            
            self.txNombreMateria.insert(0, result[1])
            self.comboNombreMaestro.insert(0, result[5])
            self.txHoraEnt.insert(0, result[2])
            self.txHoraSal.insert(0, result[3])
            self.txCreditos.insert(0, result[7])

            self.comboAula.config(state="normal")
            self.comboAula.insert(0, result[6])
            self.comboAula.config(state="readonly")

            self.comboSemestre.config(state="normal")
            self.comboSemestre.insert(0, result[8])
            self.comboSemestre.config(state="readonly")

            self.comboCarrera.config(state="normal")
            self.comboCarrera.insert(0, result[9])
            self.comboCarrera.config(state="readonly")

            self.comboDia.config(state="normal")
            self.comboDia.insert(0, result[4])
            self.comboDia.config(state="readonly")

            self.deactMateria()
            
            if self.perfil == "Administrador":
                self.btnNuevo.config(state="normal")
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="normal")
                self.btnEditar.config(state="normal")
                self.btnEliminar.config(state="normal")
        else:
            messagebox.showwarning("Error", "No existe materia con ese ID")


    def nuevaMateria(self):
        self.cancelarMateria()
        self.cleanMateria()
        self.txBuscarMateria.delete(0, END)
        self.actMateria()
        
        proximo_id = getUltimoIdMaterias()+1

        self.txBuscarMateria.insert(0, proximo_id)
        self.txBuscarMateria.config(state="disabled")
        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")
        self.btnGuardar.config(text="Crear")


    def editarMateria(self):
        self.actMateria()
        self.txBuscarMateria.config(state="disabled")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminar.config(state="normal")
        self.btnGuardar.config(state="normal")
        self.btnGuardar.config(text="Guardar")

    def guardarMateria(self):
        nombre = self.txNombreMateria.get() 
        horario_entrada = self.txHoraEnt.get()
        horario_salida = self.txHoraSal.get()
        dia = self.comboDia.get()
        maestro = self.comboNombreMaestro.get()
        aula = self.comboAula.get()
        creditos = self.txCreditos.get()
        semestre = self.comboSemestre.get()
        carrera = self.comboCarrera.get()

        if nombre and horario_entrada and horario_salida and dia and maestro and aula and creditos and semestre and carrera:
            if self.btnGuardar.cget("text") == "Crear":
                nuevaMateria(nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera)
                messagebox.showinfo("Materia agregada", "La materia ha sido creada exitosamente.")
            elif self.btnGuardar.cget("text") == "Guardar":
                id_materia = self.txBuscarMateria.get()
                editarMateria(id_materia, nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera)
                messagebox.showinfo("Materia actualizada", "La materia se ha editado exitosamente.")

            self.btnNuevo.config(state="normal")
            self.btnGuardar.config(state="disabled")
            self.btnCancelar.config(state="disabled")
            self.btnEditar.config(state="disabled")
            if self.perfil == "Administrador":
                self.btnEliminar.config(state="disabled")
            self.cancelarMateria()
        else:
            messagebox.showwarning("Error", "Favor de llenar todos los campos")
            return

    def cancelarMateria(self):
        self.cleanMateria()
        self.deactMateria()
        self.txBuscarMateria.config(state="normal")
        self.txBuscarMateria.delete(0, END)
        self.txBuscarMateria.config(state="disabled")

        self.btnNuevo.config(state="normal")
        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnEditar.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminar.config(state="disabled")
        self.btnNuevo.config(state="normal")
        self.btnGuardar.config(text="Crear")

        self.txBuscarMateria.config(state="normal")

    def deleteMateria(self):
        id_materia = self.txBuscarMateria.get()
        yesno = messagebox.askyesno("Warning","¿Desea eliminar esta materia?")
        if yesno:
            eliminarMateria(id_materia)
            messagebox.showinfo("Materia eliminada", f"La materia con ID {id_materia} ha sido eliminada.")
            self.cancelarMateria()

    def buscarDeCarrera(self):
        carrera = self.comboBuscarDeCarrera.get()

        self.limpiarTabla()
        # Obtener la lista de materias desde la base de datos
        materias = getMateriasDeCarrera(carrera)
        # n = atributos ([0]=id_materia, [1]=nombre, [2]=horario_entrada, [3]=horario_salida, [4]=dia, [5]=maestro, [6]=aula, [7]=creditos, [8]=semestre, [9]=carrera)
        # Insertar las materias en la tabla
        for materia in materias:
            self.tree.insert("", END, values=[materia[0], materia[1], materia[5], materia[6], materia[4], materia[2], materia[3], materia[8], materia[9], materia[7]])


    def cleanMateria(self):
        self.actMateria()
        self.txBuscarMateria.delete(0, END)
        self.txNombreMateria.delete(0, END)
        self.comboNombreMaestro.delete(0, END)
        self.txHoraEnt.delete(0, END)
        self.txHoraSal.delete(0, END)
        self.txCreditos.delete(0, END)
        self.comboAula.set('')
        self.comboSemestre.set('')
        self.comboCarrera.set('')
        self.comboDia.set('')
        self.deactMateria()

    def actMateria(self):
        self.txNombreMateria.config(state="normal")
        self.comboNombreMaestro.config(state="normal")
        self.txHoraEnt.config(state="normal")
        self.txHoraSal.config(state="normal")
        self.txCreditos.config(state="normal")
        self.comboAula.config(state="readonly")
        self.comboSemestre.config(state="readonly")
        self.comboCarrera.config(state="readonly")
        self.comboDia.config(state="readonly")

    def deactMateria(self):
        self.txNombreMateria.config(state="disabled")
        self.comboNombreMaestro.config(state="disabled")
        self.txHoraEnt.config(state="disabled")
        self.txHoraSal.config(state="disabled")
        self.txCreditos.config(state="disabled")
        self.comboAula.config(state="disabled")
        self.comboSemestre.config(state="disabled")
        self.comboCarrera.config(state="disabled")
        self.comboDia.config(state="disabled")


# -----------------------------------------------------------
# ---------------------APP DE AULAS--------------------------
# -----------------------------------------------------------
class AppAulas(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=1, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=2, column=0, sticky="s")

        tk.Label(self.titleFrame, text="AULAS", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

        # Casilla buscar aula
        tk.Label(self.dataFrame, text="Nombre del Aula:").grid(row=1, column=0, sticky="e")
        aulaValues = []
        for aula in getListaAulas():
            aulaValues.append(aula[3])
        self.comboBuscarAula = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH, values=aulaValues)
        self.comboBuscarAula.grid(row=1, column=1, sticky="w")
        # Boton Buscar
        self.btnBuscarAula = tk.Button(self.dataFrame, text="Buscar", command=self.buscarAula, width=BUTTON_WIDTH)
        self.btnBuscarAula.grid(row=1, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD)

        tk.Label(self.dataFrame, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.txIdAula = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txIdAula.grid(row=2, column=1, sticky="w")
        self.txIdAula.config(state="disabled")

        tk.Label(self.dataFrame, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNombreAula = tk.Entry(self.dataFrame, width=ENTRY_WIDTH)
        self.txNombreAula.grid(row=3, column=1, sticky="w")
        self.txNombreAula.config(state="disabled")

        tk.Label(self.dataFrame, text="Edificio:").grid(row=3, column=2, padx=10, pady=5, sticky="e")
        # Combobox para mostrar las aulas como opciones
        self.cbEdificio = ttk.Combobox(self.dataFrame, width=ENTRY_WIDTH, values= ["DEDU", "DBETA", "DEDX", "DEDV", "DUCT1", "DUCT2"], state="disabled")
        self.cbEdificio.grid(row=3, column=3, pady=5, sticky="w")

        # Botones

        # Nuevo aula
        self.btnNuevo = tk.Button(self.buttonFrame, text="Nuevo", width=BUTTON_WIDTH, command=self.nuevaAula)
        self.btnNuevo.grid(row=11, column=0, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnNuevo.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnNuevo.config(state="normal")

        # Guardar
        self.btnGuardar = tk.Button(self.buttonFrame, text="Guardar", width=BUTTON_WIDTH, command=self.guardarAula)
        self.btnGuardar.grid(row=11, column=1, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnGuardar.config(state="disabled")

        # Cancelar
        self.btnCancelar = tk.Button(self.buttonFrame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancelarAula)
        self.btnCancelar.grid(row=11, column=2, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnCancelar.config(state="disabled")

        # Editar
        self.btnEditar = tk.Button(self.buttonFrame, text="Editar", width=BUTTON_WIDTH, command=self.editarAula)
        self.btnEditar.grid(row=11, column=3, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEditar.config(state="disabled")

        # Eliminar
        # Desactivar botón de eliminación si el perfil no es "Administrador"
        self.btnEliminar = tk.Button(self.buttonFrame, text="Eliminar", width=BUTTON_WIDTH, command=self.eliminarAula)
        self.btnEliminar.grid(row=11, column=4, padx=BUTTON_PAD, pady=BUTTON_PAD, sticky="es")
        self.btnEliminar.config(state="disabled")
                

    def buscarAula(self):
        nombre_aula = self.comboBuscarAula.get()
        aula = buscarNombreCompletoAula(nombre_aula)

        if aula:
            self.cleanAula()
            self.actAula()

            self.txIdAula.insert(0, aula[0])
            self.txNombreAula.insert(0, aula[1])

            self.cbEdificio.config(state="normal")
            if aula[2] == None:
                self.cbEdificio.insert(0, "")
            else: 
                self.cbEdificio.insert(0, aula[2])
            self.cbEdificio.config(state="readonly")

            self.deactAula()
                
            if self.perfil == "Administrador":
                self.btnNuevo.config(state="normal")
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="disabled")
                self.btnEditar.config(state="normal")
                self.btnEliminar.config(state="normal")

        else:
            messagebox.showwarning("Aula no encontrada", "No se encontró ningún aula con el nombre proporcionado.")

    def nuevaAula(self):
        self.cleanAula()
        self.comboBuscarAula.set('')
        self.actAula()

        self.txIdAula.insert(0, getUltimoIdAulas() + 1)
        self.txIdAula.config(state="disabled")
        self.cbEdificio.config(state="readonly")

        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")
        
        self.btnGuardar.config(text="Crear")

    def guardarAula(self):
        nombre = self.txNombreAula.get()
        edificio = self.cbEdificio.get()
        if nombre and edificio:
            if self.btnGuardar.cget("text") == "Crear":
                nuevaAula(nombre, edificio)
                messagebox.showinfo("Aula creada", "El aula ha sido creada exitosamente.")
                self.btnGuardar.config(text="Guardar")
            elif self.btnGuardar.cget("text") == "Guardar":
                id_aula = self.txIdAula.get()
                editarAula(id_aula, nombre, edificio)
                messagebox.showinfo("Aula actualizada", "El aula ha sido actualizada exitosamente.")

            self.deactAula()
                
            if self.perfil == "Administrador":
                self.btnNuevo.config(state="normal")
                self.btnGuardar.config(state="disabled")
                self.btnCancelar.config(state="normal")
                self.btnEditar.config(state="disabled")
                self.btnEliminar.config(state="disabled")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete los campos")

    def cancelarAula(self):
        self.cleanAula()

        self.btnNuevo.config(state="normal")
        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")

    def editarAula(self):
        self.actAula()
        self.txIdAula.config(state="disabled")

        self.btnNuevo.config(state="disabled")
        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnEditar.config(state="disabled")
        self.btnEliminar.config(state="disabled")

    def eliminarAula(self):
        id_aula = self.txIdAula.get()
        confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar el aula con ID {id_aula}?")
        if confirmacion:
            eliminarAula(id_aula)
            messagebox.showinfo("Aula eliminada", f"El aula con ID {id_aula} ha sido eliminada.")
            self.cancelarAula()

    def cleanAula(self):
        self.actAula()
        self.comboBuscarAula.set('')
        self.txIdAula.delete(0, END)
        self.txNombreAula.delete(0, END)
        self.cbEdificio.set('')
        self.deactAula()

    def actAula(self):
        self.txIdAula.config(state="normal")
        self.txNombreAula.config(state="normal")
        self.cbEdificio.config(state="readonly")

    def deactAula(self):
        self.txIdAula.config(state="disabled")
        self.txNombreAula.config(state="disabled")
        self.cbEdificio.config(state="disabled")

        
# -----------------------------------------------------------
# ---------------------APP DE GRUPOS-------------------------
# -----------------------------------------------------------
        
# -----------------------------------------------------------
# --------------------APP DE HORARIOS------------------------
# -----------------------------------------------------------
        
# -----------------------------------------------------------
# -------------------APP DE PLANEACIÓN-----------------------
# -----------------------------------------------------------
from planeacion3 import *



if __name__ == "__main__":
    home = AppHome("ejemplo@gmail.com", "Administrador")
    home.mainloop()
