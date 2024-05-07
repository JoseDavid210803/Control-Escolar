import tkinter as tk
from tkinter import END, messagebox, ttk
from functions.aula_func import AulasFunc


class AppAulas(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.aulas = AulasFunc()
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.width = 550
        self.height = 550

        tk.Label(self, text="AULAS", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

        # Casilla buscar aula
        tk.Label(self, text="ID Aula:").grid(row=1, column=0)
        self.txBuscarAula = tk.Entry(self, width=20)
        self.txBuscarAula.grid(row=1, column=1)
        # Boton Buscar
        self.btnBuscarAula = tk.Button(self, text="Buscar", command=self.buscarAula, width=10)
        self.btnBuscarAula.grid(row=1, column=2, padx=10, pady=5)

        tk.Label(self, text="ID:").grid(row=2, column=0, padx=40, pady=5, sticky="w")
        self.txIdAula = tk.Entry(self, width=20)
        self.txIdAula.grid(row=2, column=1)
        self.txIdAula.config(state="disabled")

        tk.Label(self, text="Nombre:").grid(row=3, column=0, padx=40, pady=5, sticky="w")
        self.txNombreAula = tk.Entry(self, width=20)
        self.txNombreAula.grid(row=3, column=1)
        self.txNombreAula.config(state="disabled")

        tk.Label(self, text="Aulas:").grid(row=4, column=0, padx=40, pady=5, sticky="w")
        # Combobox para mostrar las aulas como opciones
        self.cbEdificio = ttk.Combobox(self, width=20, state="readonly")
        self.cbEdificio.grid(row=4, column=1, pady=5)
        self.cbEdificio.bind("<<ComboboxSelected>>", self.actualizarDatosAula)


        # Ancho uniforme para todos los botones
        button_width = 10

        # Distancia entre botones en la misma fila
        padx_between_buttons = 5

        # Nuevo aula
        self.btnNuevoAula = tk.Button(self, text="Nuevo", width=button_width, command=self.nuevaAula)
        self.btnNuevoAula.grid(row=11, column=0, padx=(40, padx_between_buttons), pady=10, sticky="ew")

        # Guardar
        self.btnGuardarAula = tk.Button(self, text="Crear", width=button_width, command=self.guardarAula)
        self.btnGuardarAula.grid(row=11, column=1, padx=padx_between_buttons, pady=10, sticky="ew")

        # Cancelar
        self.btnCancelarAula = tk.Button(self, text="Cancelar", width=button_width, command=self.cancelarAula)
        self.btnCancelarAula.grid(row=11, column=2, padx=padx_between_buttons, pady=10, sticky="ew")

        # Editar
        self.btnEditarAula = tk.Button(self, text="Editar", width=button_width, command=self.editarAula)
        self.btnEditarAula.grid(row=11, column=3, padx=padx_between_buttons, pady=10, sticky="ew")

        # Eliminar
        self.btnEliminarAula = tk.Button(self, text="Eliminar", width=button_width, command=self.eliminarAula)
        self.btnEliminarAula.grid(row=11, column=4, padx=padx_between_buttons, pady=10, sticky="ew")

        # Desactivar botón de eliminación si el perfil no es "Administrador"
        if self.perfil != "Administrador":
            self.btnEliminarAula.config(state="disabled")

        # Cargar la lista de aulas al combobox de edificios
        self.cargarAulasEnCombobox()

    def cargarAulasEnCombobox(self):
        lista_aulas = self.aulas.getListaAulas()
        nombres_aulas = [aula[1] for aula in lista_aulas]
        self.cbEdificio["values"] = nombres_aulas

    def actualizarDatosAula(self, event):
        nombre_aula = self.cbEdificio.get()
        aula = self.aulas.buscarAulaPorNombre(nombre_aula)
        if aula:
            self.txIdAula.config(state="normal")
            self.txNombreAula.config(state="normal")

            self.txIdAula.delete(0, END)
            self.txNombreAula.delete(0, END)

            self.txIdAula.insert(0, aula[0])
            self.txNombreAula.insert(0, aula[1])

            self.txIdAula.config(state="disabled")
            self.txNombreAula.config(state="disabled")

    def buscarAula(self):
        nombre_aula = self.cbEdificio.get()
        aula = self.aulas.buscarAulaPorNombre(nombre_aula)
        if aula:
            self.txIdAula.config(state="normal")
            self.txNombreAula.config(state="normal")

            self.txIdAula.delete(0, END)
            self.txNombreAula.delete(0, END)

            self.txIdAula.insert(0, aula[0])
            self.txNombreAula.insert(0, aula[1])

            self.txIdAula.config(state="disabled")
            self.txNombreAula.config(state="disabled")
        else:
            messagebox.showwarning("Aula no encontrada", "No se encontró ningún aula con el nombre proporcionado.")

    def nuevaAula(self):
        self.txIdAula.config(state="normal")
        self.txNombreAula.config(state="normal")

        self.txIdAula.delete(0, END)
        self.txNombreAula.delete(0, END)

        self.txIdAula.insert(0, self.aulas.getUltimoId() + 1)

        self.txIdAula.config(state="disabled")
        self.btnNuevoAula.config(state="disabled")
        self.cbEdificio.config(state="disabled")
        self.btnGuardarAula.config(state="normal")
        self.btnCancelarAula.config(state="normal")

    def guardarAula(self):
        nombre = self.txNombreAula.get()
        if nombre:
            if self.btnGuardarAula.cget("text") == "Crear":
                self.aulas.nuevaAula(nombre)
                messagebox.showinfo("Aula creada", "El aula ha sido creada exitosamente.")
            elif self.btnGuardarAula.cget("text") == "Guardar":
                id_aula = self.txIdAula.get()
                self.aulas.editarAula(id_aula, nombre)
                messagebox.showinfo("Aula actualizada", "El aula ha sido actualizada exitosamente.")

            self.btnNuevoAula.config(state="normal")
            self.cbEdificio.config(state="normal")
            self.btnGuardarAula.config(state="disabled")
            self.btnCancelarAula.config(state="disabled")
            self.btnEditarAula.config(state="disabled")
            if self.perfil == "Administrador":
                self.btnEliminarAula.config(state="disabled")
        else:
            messagebox.showwarning("Campo vacío", "Por favor complete el nombre del aula.")

    def cancelarAula(self):
        self.txIdAula.config(state="normal")
        self.txNombreAula.config(state="normal")

        self.txIdAula.delete(0, END)
        self.txNombreAula.delete(0, END)

        self.txIdAula.config(state="disabled")
        self.btnNuevoAula.config(state="normal")
        self.cbEdificio.config(state="normal")
        self.btnGuardarAula.config(state="disabled")
        self.btnCancelarAula.config(state="disabled")
        self.btnEditarAula.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarAula.config(state="disabled")

    def editarAula(self):
        self.txNombreAula.config(state="normal")

        self.btnNuevoAula.config(state="disabled")
        self.cbEdificio.config(state="disabled")
        self.btnGuardarAula.config(state="normal")
        self.btnCancelarAula.config(state="normal")
        self.btnEditarAula.config(state="disabled")
        if self.perfil == "Administrador":
            self.btnEliminarAula.config(state="disabled")

    def eliminarAula(self):
        id_aula = self.txIdAula.get()
        confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar el aula con ID {id_aula}?")
        if confirmacion:
            self.aulas.eliminarAula(id_aula)
            messagebox.showinfo("Aula eliminada", f"El aula con ID {id_aula} ha sido eliminada.")
            self.cancelarAula()


if __name__ == "__main__":
    root = tk.Tk()
    aulas = AppAulas(root, "correo@example.com", "Administrador")
    aulas.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()
