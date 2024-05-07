import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar  # Importa el calendario
from functions.usuarios_func import UsuariosFunc
from functions.alumnos_func import AlumnosFunc

class AlumnosApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.usuario = UsuariosFunc()
        self.alumno = AlumnosFunc()
        self.create_widgets()

    def create_widgets(self):
        self.width = 800
        self.height = 600

        tk.Label(self, text="ALUMNOS", font=("Arial", 20)).grid(row=0, column=0, columnspan=3, pady=10, sticky="w")

        tk.Label(self, text="Buscar por ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txIdUsuario = tk.Entry(self, width=20)
        self.txIdUsuario.grid(row=1, column=1)
        self.btnBuscarUsuario = tk.Button(self, text="Buscar", command=self.buscarUsuario)
        self.btnBuscarUsuario.grid(row=1, column=2, padx=10, pady=5)

        # Etiquetas y entradas para mostrar información del alumno
        tk.Label(self, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txIdAlumno = tk.Entry(self, width=20)
        self.txIdAlumno.grid(row=2, column=1)

        tk.Label(self, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txNombre = tk.Entry(self, width=20)
        self.txNombre.grid(row=3, column=1)

        tk.Label(self, text="Carrera:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.comboCarrera = ttk.Combobox(self, width=25)  
        self.comboCarrera.grid(row=4, column=1)
        self.comboCarrera['values'] = ["Carrera A", "Carrera B", "Carrera C"]

        tk.Label(self, text="Grupo:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.comboGrupo = ttk.Combobox(self, width=25)  
        self.comboGrupo.grid(row=5, column=1)
        self.comboGrupo['values'] = ["Grupo 1", "Grupo 2", "Grupo 3"]

        tk.Label(self, text="Fecha de Nacimiento:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.calendario = Calendar(self)
        self.calendario.grid(row=6, column=1)

        # Botones
        self.btnGuardar = tk.Button(self, text="Guardar", command=self.guardarAlumno)
        self.btnGuardar.grid(row=7, column=0, padx=10, pady=5)

        self.btnEditar = tk.Button(self, text="Editar", command=self.editarAlumno)
        self.btnEditar.grid(row=7, column=1, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text="Cancelar", command=self.cancelarAccion)
        self.btnCancelar.grid(row=7, column=2, padx=10, pady=5)

        self.btnEliminar = tk.Button(self, text="Eliminar", command=self.eliminarAlumno)
        self.btnEliminar.grid(row=7, column=3, padx=10, pady=5)

    def buscarUsuario(self):
        id = self.txIdUsuario.get()
        result = self.usuario.buscarIdUsuario(id)

        if result:
            self.mostrarUsuario(result)
        else:
            messagebox.showwarning("Error", "No existe alumno con ese ID")

    def mostrarUsuario(self, usuario):
        self.txIdAlumno.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)

        self.txIdAlumno.insert(0, usuario[0])
        self.txNombre.insert(0, usuario[1])

    def guardarAlumno(self):
        id_carrera = self.comboCarrera.get()
        id_grupo = self.comboGrupo.get()
        id_usuario = self.txIdUsuario.get()  # Por definir de dónde viene este dato
        fecha_nacimiento = self.calendario.get_date()

        self.alumno.nuevoAlumno(id_carrera, id_grupo, id_usuario, fecha_nacimiento)
        messagebox.showinfo("Éxito", "Alumno guardado correctamente")

    def editarAlumno(self):
        id_alumno = self.txIdAlumno.get()
        id_carrera = self.comboCarrera.get()
        id_grupo = self.comboGrupo.get()
        id_usuario = self.txIdUsuario.get()  # Por definir de dónde viene este dato
        fecha_nacimiento = self.calendario.get_date()

        self.alumno.editarAlumno(id_alumno, id_carrera, id_grupo, id_usuario, fecha_nacimiento)
        messagebox.showinfo("Éxito", "Alumno editado correctamente")

    def cancelarAccion(self):
        # Limpiar los campos y reiniciar
        self.txIdUsuario.delete(0, tk.END)
        self.txIdAlumno.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.comboCarrera.set('')
        self.comboGrupo.set('')
        self.calendario.selection_clear()

    def eliminarAlumno(self):
        id_alumno = self.txIdAlumno.get()
        self.alumno.eliminarAlumno(id_alumno)
        messagebox.showinfo("Éxito", "Alumno eliminado correctamente")

if __name__ == "__main__":
    root = tk.Tk()
    alumnos_app = AlumnosApp(root)
    alumnos_app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()