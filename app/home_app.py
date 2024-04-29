import tkinter as tk
from tkinter import Menu, messagebox


class AppHome(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        self.title("Control Escolar")
        self.geometry("540x290")
        self.resizable(0, 0)
        self.iconbitmap(r"C:\Users\sofia\Desktop\Control Escolar\img\01.ico")

        self.label_prueba = tk.Label(self, text=f"Bienvenido, {usuario}")
        self.label_prueba.pack(pady=50)
        self.menu()
        

    def salir(self):
        self.destroy()

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Esta es una aplicación de Control Escolar.")

    def limpiaVentana(self):
        for widget in self.winfo_children():
            widget.destroy()
            
    def menu(self):
        # Crear el menú
        self.menu_principal = Menu(self)
        self.config(menu=self.menu_principal)

        # Crear elementos del menú
        self.menu_archivo = Menu(self.menu_principal, tearoff=0)
        self.menu_archivo.add_command(label="Usuarios", command=lambda: self.UsuariosVentana("","Activo"))
        self.menu_archivo.add_command(label="Guardar")
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Archivo", menu=self.menu_archivo)
            
    def UsuariosVentana(self, correo, perfil):
        self.limpiaVentana()
        from app.usuarios_app import AppUsers
        usuarios = AppUsers(correo, perfil)
        usuarios.mainloop()
        
if __name__ == "__main__":
    home = AppHome("usuario")
    home.mainloop()
