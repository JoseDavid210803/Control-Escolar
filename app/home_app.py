import tkinter as tk
from tkinter import Menu, messagebox


class AppHome(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        self.title("Control Escolar")
        self.geometry("650x350")
        self.resizable(0, 0)
        self.iconbitmap(r"C:\Users\sofia\Desktop\Control Escolar\img\01.ico")
        self.menu()
        

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
        self.lbltitulo = tk.Label(self, text="CONTROL ESCOLAR", font=("Arial", 32, "bold"))
        self.lbltitulo.place(x=50, y=15)
            
    def menu(self):
        # Crear el menú
        self.limpiaVentana()
        self.menu_principal = Menu(self)
        self.config(menu=self.menu_principal)

        # Crear elementos del menú
        self.menu_archivo = Menu(self.menu_principal, tearoff=0)
        self.menu_archivo.add_command(label="Inicio", command=self.inicio)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Usuarios", command=lambda: self.UsuariosVentana("","Activo"))
        self.menu_archivo.add_command(label="Alumnos", command=lambda: self.AlumnosVentana())
        self.menu_archivo.add_command(label="Aulas", command=lambda: self.AulasVentana())
        self.menu_archivo.add_command(label="Maestros", command=lambda: self.MaestrosVentana())
        self.menu_archivo.add_command(label="Materia", command=lambda: self.MateriaVentana())
        self.menu_archivo.add_command(label="Grupos", command=lambda: self.GruposVentana())
        self.menu_archivo.add_command(label="Planeación", command=lambda: self.PlaneacionVentana())
        self.menu_archivo.add_command(label="Horarios", command=lambda: self.HorariosVentana())
        self.menu_archivo.add_command(label="Carrera", command=lambda: self.CarreraVentana())
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_principal.add_cascade(label="Menú", menu=self.menu_archivo)
            
    def UsuariosVentana(self, correo, perfil):
        from app.usuarios_app import AppUsers
        self.limpiaVentana()
        self.menu()
        usuarios = AppUsers(self, correo, perfil)
        usuarios.grid(row=0, column=0, padx=10, pady=10)
    
    def AlumnosVentana(self):
        from app.alumnos_app import AlumnosApp
        self.limpiaVentana()
        self.menu()
        alumnos = AlumnosApp(self)
        alumnos.grid(row=0, column=0, padx=10, pady=10)
        
    def AulasVentana(self):
        self.limpiaVentana()
        self.menu()  
        from app.aulas_app import AppAulas
        aulas = AppAulas(self, "", "")
        aulas.grid(row=0, column=0, padx=10, pady=10)

    def MaestrosVentana(self):
        self.limpiaVentana()
        self.menu()
    
    def MateriaVentana(self):
        self.limpiaVentana()
        self.menu()
        from app.materias_app import MateriasApp
        materia = MateriasApp(self)
        materia.grid(row=0, column=0, padx=10, pady=10)
    
    def GruposVentana(self):
        self.limpiaVentana()
        self.menu() 
        from app.grupos_app import AppGrupos
        grupos = AppGrupos(self, "", "")
        grupos.grid(row=0, column=0, padx=10, pady=10)
        
    def PlaneacionVentana(self):
        self.limpiaVentana()
        self.menu()
        from app.planeacion_app import AppPlaneacion
        planeacion = AppPlaneacion(self, "", "")
        planeacion.grid(row=0, column=0, padx=10, pady=10)
          
    def HorariosVentana(self):
        self.limpiaVentana()
        self.menu() 

    def CarreraVentana(self):
        self.limpiaVentana()
        self.menu() 
        from app.carrera_app import AppCarrera
        carrera = AppCarrera(self, "", "")
        carrera.grid(row=0, column=0, padx=10, pady=10)
        
if __name__ == "__main__":
    home = AppHome("usuario")
    home.mainloop()
