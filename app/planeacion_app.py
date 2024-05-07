import tkinter as tk
from tkinter import END, messagebox, ttk


class AppPlaneacion(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

    def create_widgets(self):
        self.width = 550
        self.height = 550

        tk.Label(self, text="PLANEACIÓN", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="w")



if __name__ == "__main__":
    root = tk.Tk()
    planeacion = AppPlaneacion(root, "correo@example.com", "Administrador")
    planeacion.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()