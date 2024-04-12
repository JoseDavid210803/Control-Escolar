import tkinter as tk
from tkinter import messagebox, Menu

class APP(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        self.title("Control Escolar")
        self.geometry("540x290")

        self.label_prueba = tk.Label(self, text=f"Bienvenido, {usuario}")
        self.label_prueba.pack(pady=50)

if __name__ == "__main__":
    app = APP()
    #app.mainloop()