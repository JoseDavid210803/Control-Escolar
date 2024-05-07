import tkinter as tk
from tkinter import END, messagebox, ttk
from functions.carrera_func import CarrerasFunc


class AppCarrera(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.carrera = CarrerasFunc()
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.width = 550
        self.height = 550

        tk.Label(self, text="CARRERA", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

        # Casilla buscar carrera
        tk.Label(self, text="ID carrera:").grid(row=1, column=0)
        self.txBuscarCarrera = tk.Entry(self, width=20)
        self.txBuscarCarrera.grid(row=1, column=1)
        # Boton Buscar
        self.btnBuscarCarrera = tk.Button(self, text="Buscar", command=self.buscarCarrera, width=10)
        self.btnBuscarCarrera.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self, text="ID:").grid(row=2, column=0, padx=40, pady=5, sticky="w")
        self.txIdCarrera = tk.Entry(self, width=20)
        self.txIdCarrera.grid(row=2, column=1)
        self.txIdCarrera.config(state="disabled")

        tk.Label(self, text="Nombre:").grid(row=3, column=0, padx=40, pady=5, sticky="w")
        self.txNombreCarrera = tk.Entry(self, width=20)
        self.txNombreCarrera.grid(row=3, column=1)
        self.txNombreCarrera.config(state="disabled")

        tk.Label(self, text="Semestre:").grid(row=4, column=0, padx=40, pady=5, sticky="w")
        # Combobox para mostrar los semestres como opciones
        self.cbSemestre = ttk.Combobox(self, width=20, state="readonly")
        self.cbSemestre.grid(row=4, column=1, pady=5)
        self.cbSemestre.bind("<<ComboboxSelected>>", self.actualizarDatosCarrera)


        # Ancho uniforme para todos los botones
        button_width = 10

        # Distancia entre botones en la misma fila
        padx_between_buttons = 5

        # Nuevo carrera
        self.btnNuevoCarrera = tk.Button(self, text="Nuevo", width=button_width, command=self.nuevaCarrera)
        self.btnNuevoCarrera.grid(row=11, column=0, padx=(40, padx_between_buttons), pady=10, sticky="ew")

        # Guardar
        self.btnGuardarCarrera = tk.Button(self, text="Crear", width=button_width, command=self.guardarCarrera)
        self.btnGuardarCarrera.grid(row=11, column=1, padx=padx_between_buttons, pady=10, sticky="ew")

        # Cancelar
        self.btnCancelarCarrera = tk.Button(self, text="Cancelar", width=button_width, command=self.cancelarCarrera)
        self.btnCancelarCarrera.grid(row=11, column=2, padx=padx_between_buttons, pady=10, sticky="ew")

        # Editar
        self.btnEditarCarrera = tk.Button(self, text="Editar", width=button_width, command=self.editarCarrera)
        self.btnEditarCarrera.grid(row=11, column=3, padx=padx_between_buttons, pady=10, sticky="ew")

        # Eliminar
        self.btnEliminarCarrera = tk.Button(self, text="Eliminar", width=button_width, command=self.eliminarCarrera)
        self.btnEliminarCarrera.grid(row=11, column=4, padx=padx_between_buttons, pady=10, sticky="ew")

        # Desactivar botón de eliminación si el perfil no es "Administrador"
        if self.perfil != "Administrador":
            self.btnEliminarCarrera.config(state="disabled")

        # Cargar la lista de carreras al combobox de semestres
        self.cargarCarrerasEnCombobox()

    def cargarCarrerasEnCombobox(self):
        lista_carrera = self.carrera.getListaCarreras()
        nombres_carrera = [carrera[1] for carrera in lista_carrera]
        self.cbSemestre["values"] = nombres_carrera

    def actualizarDatosCarrera(self, event):
        nombre_carrera = self.cbSemestre.get()
        carrera = self.carrera.buscarCarreraPorNombre(nombre_carrera)
        if carrera:
            self.txIdCarrera.config(state="normal")
            self.txNombreCarrera.config(state="normal")

            self.txIdCarrera.delete(0, END)
            self.txNombreCarrera.delete(0, END)

            self.txIdCarrera.insert(0, carrera[0])
            self.txNombreCarrera.insert(0, carrera[1])

            self.txIdCarrera.config(state="disabled")
            self.txNombreCarrera.config(state="disabled")

    def buscarCarrera(self):
        nombre_carrera = self.cbSemestre.get()
        carrera = self.carrera.buscarCarreraPorNombre(nombre_carrera)
        if carrera:
            self.txIdCarrera.config(state="normal")
            self.txNombreCarrera.config(state="normal")

            self.txIdCarrera.delete(0, END)
            self.txNombreCarrera.delete(0, END)

            self.txIdCarrera.insert(0, carrera[0])
            self.txNombreCarrera.insert(0, carrera[1])

            self.txIdCarrera.config(state="disabled")
            self.txNombreCarrera.config(state="disabled")
        else:
            messagebox.showwarning("Carrera no encontrada", "No se encontró ninguna carrera con el nombre proporcionado.")

    def nuevaCarrera(self):
        self.txIdCarrera.config(state="normal")
        self.txNombreCarrera.config(state="normal")

        self.txIdCarrera.delete(0, END)
        self.txNombreCarrera.delete(0, END)

        self.txIdCarrera.insert(0, self.carrera.getUltimoId() + 1)

        self.txIdCarrera.config(state="disabled")
        self.btnNuevoCarrera.config(state="disabled")
        self.cbSemestre.config(state="disabled")
        self.btnGuardarCarrera.config(state="normal")
        self.btnCancelarCarrera.config(state="normal")

    def guardarCarrera(self):
        nombre = self.txNombreCarrera.get()
        if nombre:
            if self.btnGuardarCarrera.cget("text") == "Crear":
                self.carrera.nuevaCarrera(nombre)
                messagebox.showinfo("Carrera creada", "La carrera ha sido creada exitosamente.")
            elif self.btnGuardarCarrera.cget("text") == "Guardar":
                id_carrera = self.txIdCarrera.get()
                self.carrera.editarCarrera(id_carrera, nombre)
                messagebox.showinfo("Carrera actualizada", "La carrera ha sido actualizada exitosamente.")

            self.btnNuevoCarrera.config(state="normal")
            self.cbSemestre.config(state="normal")
            self.btnGuardarCarrera.config(state="disabled")
            self.btnCancelarCarrera.config(state="disabled")
            self.btnEditarCarrera.config(state="disabled")
            if self.perfil == "Administrador":
                self.btnEliminarCarrera.config(state="disabled")
        else:
            messagebox.showwarning("Campo vacío", "Por favor complete el nombre de la carrera.")

    def cancelarCarrera(self):
        self.txIdCarrera.config(state="normal")
        self.txNombreCarrera.config(state="normal")

        self.txIdCarrera.delete(0, END)
        self.txNombreCarrera.delete(0, END)

        self.txIdCarrera.config(state="disabled")
        self.btnNuevoCarrera.config(state="normal")
        self.cbSemestre.config(state="normal")
        self.btnGuardarCarrera.config(state="disabled")
        self.btnCancelarCarrera.config(state="disabled")
        self.btnEditarCarrera.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarCarrera.config(state="disabled")

    def editarCarrera(self):
        self.txNombreCarrera.config(state="normal")

        self.btnNuevoCarrera.config(state="disabled")
        self.cbSemestre.config(state="disabled")
        self.btnGuardarCarrera.config(state="normal")
        self.btnCancelarCarrera.config(state="normal")
        self.btnEditarCarrera.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarCarrera.config(state="disabled")

    def eliminarCarrera(self):
        id_carrera = self.txIdCarrera.get()
        confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar la carrera con ID {id_carrera}?")
        if confirmacion:
            self.carrera.eliminarCarrera(id_carrera)
            messagebox.showinfo("Carrera eliminada", f"La carrera con ID {id_carrera} ha sido eliminada.")
            self.cancelarCarrera()


if __name__ == "__main__":
    root = tk.Tk()
    carrera = AppCarrera(root, "correo@example.com", "Administrador")
    carrera.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()