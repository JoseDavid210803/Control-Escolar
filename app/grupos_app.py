import tkinter as tk
from tkinter import END, messagebox, ttk
from functions.grupos_func import GruposFunc

class AppGrupos(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.grupos = GruposFunc()
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.width = 550
        self.height = 550

        tk.Label(self, text="GRUPOS", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

        # Casilla buscar grupo
        tk.Label(self, text="ID Grupo:").grid(row=1, column=0)
        self.txBuscarGrupo = tk.Entry(self, width=20)
        self.txBuscarGrupo.grid(row=1, column=1)
        # Boton Buscar
        self.btnBuscarGrupo = tk.Button(self, text="Buscar", command=self.buscarIdGrupo, width=10)
        self.btnBuscarGrupo.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self, text="ID Grupo:").grid(row=2, column=0, padx=40, pady=5, sticky="w")
        self.txIdGrupo = tk.Entry(self, width=20)
        self.txIdGrupo.grid(row=2, column=1)
        self.txIdGrupo.config(state="disabled")

        tk.Label(self, text="ID Carrera:").grid(row=3, column=0, padx=40, pady=5, sticky="w")
        self.txIdCarrera = tk.Entry(self, width=20)
        self.txIdCarrera.grid(row=3, column=1)
        self.txIdCarrera.config(state="disabled")
        
        tk.Label(self, text="ID Materia:").grid(row=4, column=0, padx=40, pady=5, sticky="w")
        self.txIdMateria = tk.Entry(self, width=20)
        self.txIdMateria.grid(row=4, column=1)
        self.txIdMateria.config(state="disabled")
        
        tk.Label(self, text="ID Alumnos:").grid(row=5, column=0, padx=40, pady=5, sticky="w")
        self.txIdAlumnos = tk.Entry(self, width=20)
        self.txIdAlumnos.grid(row=5, column=1)
        self.txIdAlumnos.config(state="disabled")
        
        tk.Label(self, text="Salón:").grid(row=2, column=2, padx=40, pady=5, sticky="w")
        self.txSalon = tk.Entry(self, width=20)
        self.txSalon.grid(row=2, column=3)
        self.txSalon.config(state="disabled")
        
        tk.Label(self, text="Semestre:").grid(row=3, column=2, padx=40, pady=5, sticky="w")
        self.txSemestre = tk.Entry(self, width=20)
        self.txSemestre.grid(row=3, column=3)
        self.txSemestre.config(state="disabled")
        
        tk.Label(self, text="Max. Alumnos:").grid(row=4, column=2, padx=40, pady=5, sticky="w")
        self.txMaxAlumnos = tk.Entry(self, width=20)
        self.txMaxAlumnos.grid(row=4, column=3)
        self.txMaxAlumnos.config(state="disabled")

        # Combobox para mostrar grupos
        tk.Label(self, text="Grupos:").grid(row=5, column=2, padx=40, pady=5, sticky="w")
        self.cbGrupos = ttk.Combobox(self, width=18)
        self.cbGrupos.grid(row=5, column=3, columnspan=2, padx=10, pady=5)

        # Ancho uniforme para todos los botones
        button_width = 8

        # Distancia entre botones en la misma fila
        padx_between_buttons = 10

        # Guardar
        self.btnGuardarGrupo = tk.Button(self, text="Crear", width=button_width, command=self.nuevoGrupo)
        self.btnGuardarGrupo.grid(row=11, column=0, padx=padx_between_buttons, pady=10, sticky="ew")

        # Cancelar
        self.btnCancelarGrupo = tk.Button(self, text="Cancelar", width=button_width, command=self.cancelarGrupo)
        self.btnCancelarGrupo.grid(row=11, column=1, padx=padx_between_buttons, pady=10, sticky="ew")

        # Editar
        self.btnEditarGrupo = tk.Button(self, text="Editar", width=button_width, command=self.editarGrupo)
        self.btnEditarGrupo.grid(row=11, column=2, padx=padx_between_buttons, pady=10, sticky="ew")

        # Eliminar
        self.btnEliminarGrupo = tk.Button(self, text="Eliminar", width=button_width, command=self.eliminarGrupo)
        self.btnEliminarGrupo.grid(row=11, column=3, padx=padx_between_buttons, pady=10, sticky="ew")

        # Desactivar botón de eliminación si el perfil no es "Administrador"
        if self.perfil != "Administrador":
            self.btnEliminarGrupo.config(state="disabled")

        # Cargar la lista de grupos al combobox de edificios
        self.cargarGruposEnCombobox()

    def cargarGruposEnCombobox(self):
        lista_grupos = self.grupos.getListaGrupos()
        nombres_grupos = [grupo[1] for grupo in lista_grupos]
        self.cbGrupos["values"] = nombres_grupos

    def buscarIdGrupo(self):
        id_grupo = self.txBuscarGrupo.get()
        grupo = self.grupos.buscarIdGrupo(id_grupo)
        if grupo:
            self.txIdGrupo.config(state="normal")
            self.txIdCarrera.config(state="normal")
            self.txIdMateria.config(state="normal")
            self.txIdAlumnos.config(state="normal")
            self.txSalon.config(state="normal")
            self.txSemestre.config(state="normal")
            self.txMaxAlumnos.config(state="normal")

            self.txIdGrupo.delete(0, END)
            self.txIdCarrera.delete(0, END)
            self.txIdMateria.delete(0, END)
            self.txIdAlumnos.delete(0, END)
            self.txSalon.delete(0, END)
            self.txSemestre.delete(0, END)
            self.txMaxAlumnos.delete(0, END)

            self.txIdGrupo.insert(0, grupo[0])
            self.txIdCarrera.insert(0, grupo[1])
            self.txIdMateria.insert(0, grupo[2])
            self.txIdAlumnos.insert(0, grupo[3])
            self.txSalon.insert(0, grupo[4])
            self.txSemestre.insert(0, grupo[5])
            self.txMaxAlumnos.insert(0, grupo[6])

            self.txIdGrupo.config(state="disabled")
            self.txIdCarrera.config(state="disabled")
            self.txIdMateria.config(state="disabled")
            self.txIdAlumnos.config(state="disabled")
            self.txSalon.config(state="disabled")
            self.txSemestre.config(state="disabled")
            self.txMaxAlumnos.config(state="disabled")
        else:
            messagebox.showwarning("Grupo no encontrado", "No se encontró ningún grupo con el ID proporcionado.")

    def nuevoGrupo(self):
        id_carrera = self.txIdCarrera.get()
        id_materia = self.txIdMateria.get()
        id_alumnos = self.txIdAlumnos.get()
        salon = self.txSalon.get()
        semestre = self.txSemestre.get()
        max_alumn = self.txMaxAlumnos.get()

        if id_carrera and id_materia and id_alumnos and salon and semestre and max_alumn:
            self.grupos.nuevoGrupo(id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn)
            messagebox.showinfo("Grupo creado", "El grupo ha sido creado exitosamente.")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")

    def cancelarGrupo(self):
        self.txIdCarrera.delete(0, END)
        self.txIdMateria.delete(0, END)
        self.txIdAlumnos.delete(0, END)
        self.txSalon.delete(0, END)
        self.txSemestre.delete(0, END)
        self.txMaxAlumnos.delete(0, END)

    def editarGrupo(self):
        id_grupo = self.txIdGrupo.get()
        id_carrera = self.txIdCarrera.get()
        id_materia = self.txIdMateria.get()
        id_alumnos = self.txIdAlumnos.get()
        salon = self.txSalon.get()
        semestre = self.txSemestre.get()
        max_alumn = self.txMaxAlumnos.get()

        if id_grupo and id_carrera and id_materia and id_alumnos and salon and semestre and max_alumn:
            self.grupos.editarGrupo(id_grupo, id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn)
            messagebox.showinfo("Grupo editado", "El grupo ha sido editado exitosamente.")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")

    def eliminarGrupo(self):
        id_grupo = self.txIdGrupo.get()
        if id_grupo:
            confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar el grupo con ID {id_grupo}?")
            if confirmacion:
                self.grupos.eliminarGrupo(id_grupo)
                messagebox.showinfo("Grupo eliminado", f"El grupo con ID {id_grupo} ha sido eliminado.")
                self.cancelarGrupo()
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingrese el ID del grupo que desea eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    grupos = AppGrupos(root, "correo@example.com", "Administrador")
    grupos.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()
