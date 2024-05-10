import tkinter as tk
from tkinter import ttk, END, messagebox
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from funciones import *
import os

class AppPlaneacion(tk.Frame):
    def __init__(self, master, correo, perfil):
        super().__init__(master)
        self.master = master
        self.correo = correo
        self.perfil = perfil
        self.create_widgets()

        if self.perfil == "Alumno":
            carrera = getCarreraPorCorreo(self.correo)[1]
            self.crearGrafico(carrera)

        self.nombre = buscarCorreoUsuario(self.correo)


    def create_widgets(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.grid(row=0, column=0, sticky="n")
        self.dataFrame = tk.Frame(self)
        self.dataFrame.grid(row=1, column=0, sticky="n")
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=2, column=0, sticky="s")
        self.frame_form = tk.Frame(self)
        self.frame_form.grid(row=3, column=0, sticky="s")

        tk.Label(self.titleFrame, text="PLANEACIÓN", font=("Arial", 20)).grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

        carreraValues = []
        for carrera in getListaCarreras():
            carreraValues.append(', '.join(carrera))
        self.comboCarrera = ttk.Combobox(self.buttonFrame, width=30, values=carreraValues)
        self.comboCarrera.grid(row=1, column=1, sticky="w")
        
        self.btnBuscarMateria = tk.Button(self.buttonFrame, text="Cambiar Carrera", command=lambda: self.crearGrafico(self.comboCarrera.get()), width=15)
        self.btnBuscarMateria.grid(row=1, column=2, padx=10, pady=5)

        self.exportarPDFButton = tk.Button(self.buttonFrame, text="Exportar a PDF", command=self.exportar_a_pdf, width=15)
        self.exportarPDFButton.grid(row=1, column=3, padx=10, pady=5)


    def crearGrafico(self, carrera):
        # Aquí es donde definimos el gráfico y lo agregamos a dataFrame
        # Conexión a la base de datos
        cadena_conexion = 'mysql+mysqlconnector://root:@localhost/control'
        engine = create_engine(cadena_conexion)
        
        consulta = f"""
        SELECT id_materia, nombre, horario_entrada, horario_salida, maestro, aula, creditos, semestre, carrera, dia
        FROM materias
        WHERE dia IN ('lunes', 'martes', 'miércoles', 'jueves', 'viernes')
        AND TIME(horario_entrada) BETWEEN '07:00' AND '14:00'
        AND carrera = '{carrera}'
        """
        df = pd.read_sql(consulta, engine)

        # Crea el gráfico con matplotlib
        self.fig, ax = plt.subplots(figsize=(8, 4))

        # Configura el gráfico con seaborn
        for index, row in df.iterrows():
            dia = row['dia']
            entrada = row['horario_entrada'].total_seconds() / 3600
            salida = row['horario_salida'].total_seconds() / 3600
        
            ax.plot([entrada, salida], [dia, dia], label=row['nombre'], color='C' + str(index % 10), marker='o', linestyle='-')
        
        # Configurar los ejes y el título
        plt.title(f'Horario de {carrera}')
        plt.xlabel('Hora del día')
        plt.ylabel('Día de la semana')
        
        # Configurar el rango de los ejes
        plt.xlim(7, 14)  # Mostrar solo las horas de 7 a 14
        plt.ylim(-1, 5)  # Mostrar solo los días de lunes a viernes (0: lunes, 1: martes, 2: miércoles, 3: jueves, 4: viernes)
        
        # Personalizar las etiquetas del eje Y para mostrar los días de la semana
        plt.yticks([0, 1, 2, 3, 4], ['lunes', 'martes', 'miércoles', 'jueves', 'viernes'])
        
        # Mostrar leyenda
        plt.legend()

        # Crea el canvas para el gráfico de matplotlib
        canvas = FigureCanvasTkAgg(self.fig, master=self.dataFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


    def exportar_a_pdf(self):
        # Obtiene el directorio de trabajo actual
        directorio_actual = os.getcwd()
        # Especifica la ruta de la carpeta 'pdfs' dentro del directorio actual
        carpeta_pdfs = os.path.join(directorio_actual, 'pdfs')

        # Asegúrate de que la carpeta 'pdfs' exista. Si no existe, créala.
        if not os.path.exists(carpeta_pdfs):
            os.makedirs(carpeta_pdfs)

        # Define la ruta completa del archivo PDF que deseas guardar
        ruta_archivo_pdf = os.path.join(carpeta_pdfs, f'grafico{self.nombre[1]}_{self.nombre[2]}_{self.comboCarrera.get()}.pdf')

        # Abrir un archivo PDF usando PdfPages
        with PdfPages(ruta_archivo_pdf) as pdf:
            # Guardar la figura actual en el archivo PDF
            pdf.savefig(self.fig)
        
        # Mostrar un mensaje de confirmación
        messagebox.showinfo("Exportar a PDF", f"El gráfico se ha exportado a {ruta_archivo_pdf}")
