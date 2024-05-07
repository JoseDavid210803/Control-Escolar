import tkinter as tk
from tkinter import ttk, messagebox
from functions.materias_func import MateriasFunc

class MateriasApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Gestión de Materias")
        self.master.geometry("800x600")

        self.materias_func = MateriasFunc()

        self.create_widgets()

    def create_widgets(self):
        self.lbl_titulo = tk.Label(self.master, text="Gestión de Materias", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=10)

        self.frame_form = tk.Frame(self.master)
        self.frame_form.pack(pady=20)

        # Labels y Entries para ingresar los datos de la materia
        self.lbl_horario = tk.Label(self.frame_form, text="ID Horario:")
        self.lbl_horario.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_horario = tk.Entry(self.frame_form, width=30)
        self.entry_horario.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_maestro = tk.Label(self.frame_form, text="ID Maestro:")
        self.lbl_maestro.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_maestro = tk.Entry(self.frame_form, width=30)
        self.entry_maestro.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_asignatura = tk.Label(self.frame_form, text="Asignatura:")
        self.lbl_asignatura.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_asignatura = tk.Entry(self.frame_form, width=30)
        self.entry_asignatura.grid(row=2, column=1, padx=10, pady=5)

        self.lbl_creditos = tk.Label(self.frame_form, text="Créditos:")
        self.lbl_creditos.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_creditos = tk.Entry(self.frame_form, width=30)
        self.entry_creditos.grid(row=3, column=1, padx=10, pady=5)

        self.lbl_semestre = tk.Label(self.frame_form, text="Semestre:")
        self.lbl_semestre.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_semestre = tk.Entry(self.frame_form, width=30)
        self.entry_semestre.grid(row=4, column=1, padx=10, pady=5)

        self.lbl_carrera = tk.Label(self.frame_form, text="Carrera:")
        self.lbl_carrera.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_carrera = tk.Entry(self.frame_form, width=30)
        self.entry_carrera.grid(row=5, column=1, padx=10, pady=5)

        # Botones de acciones
        self.btn_guardar = tk.Button(self.frame_form, text="Guardar", command=self.guardar_materia)
        self.btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_limpiar = tk.Button(self.frame_form, text="Limpiar", command=self.limpiar_campos)
        self.btn_limpiar.grid(row=7, column=0, columnspan=2)

        # Tabla para mostrar las materias
        self.tree = ttk.Treeview(self.master, columns=("ID", "Horario", "Maestro", "Asignatura", "Créditos", "Semestre", "Carrera"))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Horario')
        self.tree.heading('#2', text='Maestro')
        self.tree.heading('#3', text='Asignatura')
        self.tree.heading('#4', text='Créditos')
        self.tree.heading('#5', text='Semestre')
        self.tree.heading('#6', text='Carrera')
        self.tree.pack(padx=10, pady=20)

        self.cargar_materias()

    def cargar_materias(self):
        # Limpiar la tabla antes de cargar los datos
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Obtener la lista de materias desde la base de datos
        materias = self.materias_func.getListaMaterias()

        # Insertar las materias en la tabla
        for materia in materias:
            self.tree.insert("", tk.END, values=materia)

    def guardar_materia(self):
        # Obtener los datos de la materia desde los campos de entrada
        id_horario = self.entry_horario.get()
        id_maestro = self.entry_maestro.get()
        asignatura = self.entry_asignatura.get()
        creditos = self.entry_creditos.get()
        semestre = self.entry_semestre.get()
        carrera = self.entry_carrera.get()

        # Verificar si todos los campos están completos
        if id_horario and id_maestro and asignatura and creditos and semestre and carrera:
            # Guardar la nueva materia en la base de datos
            self.materias_func.nuevaMateria(id_horario, id_maestro, asignatura, creditos, semestre, carrera)
            messagebox.showinfo("Éxito", "Materia guardada exitosamente.")
            self.limpiar_campos()
            self.cargar_materias()
        else:
            messagebox.showwarning("Error", "Por favor complete todos los campos.")

    def limpiar_campos(self):
        # Limpiar todos los campos de entrada
        self.entry_horario.delete(0, tk.END)
        self.entry_maestro.delete(0, tk.END)
        self.entry_asignatura.delete(0, tk.END)
        self.entry_creditos.delete(0, tk.END)
        self.entry_semestre.delete(0, tk.END)
        self.entry_carrera.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MateriasApp(root)
    app.pack()
    root.mainloop()
