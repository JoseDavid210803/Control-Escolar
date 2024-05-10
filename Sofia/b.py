from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from mysql.connector import connect, Error
import re
from tkinter import END, ttk
import tkinter as tk
from tkinter import messagebox, Toplevel
from tkcalendar import Calendar, DateEntry 
from datetime import datetime

botonEliminar = None
botonEditar = None

class DBControl:
    def __init__(self):
        self.host = "localhost"
        self.usuario = "root"
        self.password = ""
        self.baseDatos = "control"
        self.conn = None
        self.cursor1 = None
        self.open()

    def open(self):
        self.conn = connect(host=self.host,
                            user=self.usuario,
                            password=self.password,
                            database=self.baseDatos)
        self.cursor1 = self.conn.cursor()

    def close(self):
        self.conn.close()

    def verificarLogin(self, correo, contrasena):
        self.cursor1.execute("SELECT * FROM usuarios WHERE BINARY correo = %s AND BINARY contrasena = %s", (correo, contrasena))
        user_data = self.cursor1.fetchone()
        if user_data:
            if user_data[7] == 'Inactivo':
                print("Usuario Inactivo!")
                return None
            return user_data
        else:
            print("Login fail!")
            return None
    def buscarUsuario(self, id):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarUsuario(self, usuario):
        sql = "INSERT INTO usuarios (id, nombre, a_paterno, a_materno, correo, contrasena, perfil, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (usuario.get_usuario_id(),
                usuario.get_nombre(),
                usuario.get_apellido_paterno(),
                usuario.get_apellido_materno(),
                usuario.get_correo(),
                usuario.get_contrasena(),
                usuario.get_perfil(),
                usuario.get_status())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Usuario guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el usuario: {e}")
    def eliminarUsuario(self, id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el usuario: {err}")
    def actualizarUsuario(self, usuario):
        sql = "UPDATE usuarios SET nombre=%s, a_paterno=%s, a_materno=%s, correo=%s, contrasena=%s, perfil=%s, status=%s WHERE id=%s"
        datos = (usuario.get_nombre(),
                usuario.get_apellido_paterno(),
                usuario.get_apellido_materno(),
                usuario.get_correo(),
                usuario.get_contrasena(),
                usuario.get_perfil(),
                usuario.get_status(),
                usuario.get_usuario_id())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar el usuario: {err}")
    
    def buscarAlumno(self, id):
        sql = "SELECT * FROM alumnos WHERE id_alumno = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarAlumno(self, alumno):
        sql = "INSERT INTO alumnos (id_alumno, id_usuario, fecha_nacimiento, nombre_carrera, grupo) VALUES (%s, %s, %s, %s, %s)"
        datos = (alumno.get_IdAlumno(),
                alumno.get_idUsuario(),
                alumno.get_nacimiento(),
                alumno.get_carreraAlumno(),
                alumno.get_grupoAlumno())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Alumno guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el alumno: {e}")
    def eliminarAlumno(self, id):
        sql = "DELETE FROM alumnos WHERE id_alumno = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el alumno: {err}")
    def actualizarAlumno(self, alumno):
        sql = "UPDATE alumnos SET id_usuario=%s, fecha_nacimiento=%s, nombre_carrera=%s, grupo=%s WHERE id_alumno=%s"
        datos = (alumno.get_idUsuario(),
            alumno.get_nacimiento(),
            alumno.get_carreraAlumno(),
            alumno.get_grupoAlumno(),
            alumno.get_IdAlumno())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Alumno actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar el usuario: {err}")
    def obtenerPerfilUsuario(self, id_usuario):
        sql = "SELECT perfil FROM usuarios WHERE id = %s"
        try:
            self.cursor1.execute(sql, (id_usuario,))
            perfil = self.cursor1.fetchone()
            if perfil:
                return perfil[0]  # Retorna el perfil del usuario
            else:
                return None  # Retorna None si no se encuentra el usuario
        except Error as err:
            print(f"No se pudo obtener el perfil del usuario: {err}")
            return None  # Retorna None si hay algún error
    def buscarAlumnoPorIdUsuario(self, id_usuario):
        sql = "SELECT * FROM alumnos WHERE id_usuario = %s"
        self.cursor1.execute(sql, (id_usuario,))
        alumno = self.cursor1.fetchone()
        return alumno
    
    
    def buscarMaestro(self, id):
        sql = "SELECT * FROM maestros WHERE id_maestro = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarMaestro(self, maestro):
        sql = "INSERT INTO maestros (id_maestro, id_usuario, id_materias, grado_estudios) VALUES (%s, %s, %s, %s)"
        datos = (maestro.get_idMaestro(),
                maestro.get_idUsuario(),
                maestro.get_idMaterias(),
                maestro.get_gradoEstudios())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Maestro guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el maestro: {e}")
    def eliminarMaestro(self, id):
        sql = "DELETE FROM maestros WHERE id_maestro = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Maestro eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el maestro: {err}")
    def actualizarMaestro(self, maestro):
        sql = "UPDATE maestros SET id_usuario=%s, id_materias=%s, grado_estudios=%s WHERE id_maestro=%s"
        datos = (maestro.get_idUsuario(),
            maestro.get_idMaterias(),
            maestro.get_gradoEstudios(),
            maestro.get_idMaestro())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Maestro actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar el maestro: {err}")
    
    def buscarMaestroPorIdUsuario(self, id_usuario):
        sql = "SELECT * FROM maestros WHERE id_usuario = %s"
        self.cursor1.execute(sql, (id_usuario,))
        maestro = self.cursor1.fetchone()
        return maestro
    
    def getListaMaterias(self):
        mostrarMaterias = "SELECT nombre FROM materias"
        self.cursor1.execute(mostrarMaterias)
        listaMaterias = self.cursor1.fetchall()  
        return listaMaterias        
    
    def getListaCarreras(self):
        mostrar_carreras = "SELECT nombre FROM carrera"
        self.cursor1.execute(mostrar_carreras)
        lista_carreras = self.cursor1.fetchall()  
        return lista_carreras
    
    def getListaGrupos(self):
        mostrarGrupos = "SELECT nombre_grupo FROM grupos"
        self.cursor1.execute(mostrarGrupos)
        listaGrupos = self.cursor1.fetchall()  
        return listaGrupos     
    
    def getListaEstudios(self):
        mostrarEstudios = "SELECT grado_estudios FROM maestros"
        self.cursor1.execute(mostrarEstudios)
        listaEstudios = self.cursor1.fetchall()  
        return listaEstudios 
    
    def buscarAula(self, id):
        sql = "SELECT * FROM aula WHERE id_aula = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarAula(self, aula):
        sql = "INSERT INTO aula (id_aula, nombre, edificio) VALUES (%s, %s, %s)"
        datos = (aula.get_idAula(),
                aula.get_nombreAula(),
                aula.get_edificioAula())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Aula guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el aula: {e}")
    def eliminarAula(self, id):
        sql = "DELETE FROM aula WHERE id_aula = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Aula eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el aula: {err}")
    def actualizarAula(self, aula):
        sql = "UPDATE aula SET nombre=%s, edificio=%s  WHERE id_aula=%s"
        datos = (aula.get_nombreAula(),
            aula.get_edificioAula(),
            aula.get_idAula())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Aula actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar la aula: {err}")
    def buscarCarrera(self, id):
        sql = "SELECT * FROM carrera WHERE id_carrera = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarCarrera(self, carrera):
        sql = "INSERT INTO carrera (id_carrera, nombre, semestre) VALUES (%s, %s, %s)"
        datos = (carrera.get_idCarrera(),
                carrera.get_nombreCarrera(),
                carrera.get_semestre())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Carrera guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el carrera: {e}")
    def eliminarCarrera(self, id):
        sql = "DELETE FROM carrera WHERE id_carrera = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Carrera eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el carrera: {err}")
    def actualizarCarrera(self, carrera):
        sql = "UPDATE carrera SET nombre=%s, semestre=%s  WHERE id_carrera=%s"
        datos = (carrera.get_nombreCarrera(),
                carrera.get_semestre(),
                carrera.get_idCarrera())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Carrera actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar la carrera: {err}")
    
    def buscarHorario(self, id):
        sql = "SELECT * FROM horarios WHERE id_horarios = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarHorario(self, horario):
        sql = "INSERT INTO horarios (id_horarios, turno, hora) VALUES (%s, %s, %s)"
        datos = (horario.get_idHorario(),
                horario.get_turnoHorario(),
                horario.get_horaHorario())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Horario guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el horario: {e}")
    def eliminarHorario(self, id):
        sql = "DELETE FROM horarios WHERE id_horarios = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Horario eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar el horario: {err}")
    def actualizarHorario(self, horario):
        sql = "UPDATE horarios SET turno=%s, hora=%s  WHERE id_horarios=%s"
        datos = (horario.get_turnoHorario(),
                horario.get_horaHorario(),
                horario.get_idHorario())
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Horario actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar la horario: {err}")
            
    def buscarMateria(self, id):
        sql = "SELECT * FROM materias WHERE id_materia = %s"
        self.cursor1.execute(sql, (id,))
        user = self.cursor1.fetchone()
        return user
    def guardarMateria(self, materia):
        sql = "INSERT INTO materias (id_materia, nombre, horario_entrada, horario_salida, maestro, aula, creditos, semestre, carrera) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (materia.get_idMateria(),
                    materia.get_nombre(),
                    materia.get_horarioEntrada(),
                    materia.get_horarioSalida(),
                    materia.get_maestroMateria(),
                    materia.get_aulaMateria(),
                    materia.get_creditosMateria(),
                    materia.get_semestreMateria(),
                    materia.get_carreraMateria(),
                    )
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Materia guardado correctamente.")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo guardar la materia: {e}")
    def eliminarMateria(self, id):
        sql = "DELETE FROM materias WHERE id_materia = %s"
        try:
            self.cursor1.execute(sql, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Materia eliminado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo eliminar la materia: {err}")
    def actualizarMateria(self, materia):
        sql = "UPDATE materias SET nombre=%s, horario_entrada=%s, horario_salida=%s, maestro=%s, aula=%s, creditos=%s, semestre=%s, carrera=%s   WHERE id_materia=%s"
        datos = (materia.get_nombre(),
                    materia.get_horarioEntrada(),
                    materia.get_horarioSalida(),
                    materia.get_maestroMateria(),
                    materia.get_aulaMateria(),
                    materia.get_creditosMateria(),
                    materia.get_semestreMateria(),
                    materia.get_carreraMateria(),
                    materia.get_idMateria()
                    )
        try:
            self.cursor1.execute(sql, datos)
            self.conn.commit()
            messagebox.showinfo("Éxito", "Materia actualizado correctamente.")
        except Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar la materia: {err}")
                      
class Usuarios:
    def __init__(self):
        self.usuarioId = None
        self.nombre = None
        self.apellidoPaterno = None
        self.apellidoMaterno = None
        self.correo = None
        self.contrasena = None
        self.perfil = None
        self.status = None
        

    def get_usuario_id(self):   return self.usuarioId
    def set_usuario_id(self, usuarioId):    self.usuarioId = usuarioId

    def get_nombre(self):   return self.nombre
    def set_nombre(self, nombre):   self.nombre = nombre

    def get_apellido_paterno(self): return self.apellidoPaterno
    def set_apellido_paterno(self, apellidoPaterno):    self.apellidoPaterno = apellidoPaterno

    def get_apellido_materno(self): return self.apellidoMaterno
    def set_apellido_materno(self, apellidoMaterno):    self.apellidoMaterno = apellidoMaterno

    def get_correo(self):   return self.correo
    def set_correo(self, correo):   self.correo = correo

    def get_contrasena(self):   return self.contrasena
    def set_contrasena(self, contrasena):   self.contrasena = contrasena

    def get_perfil(self):   return self.perfil
    def set_perfil(self, perfil):   self.perfil = perfil
    
    def get_status(self):   return self.status
    def set_status(self, status):   self.status = status
class Alumnos:
    def __init__(self):
        self.idAlumno = None
        self.idUsuario = None
        self.nacimiento = None
        self.carreraAlumno = None
        self.grupoAlumno = None
        

    def get_IdAlumno(self):   return self.idAlumno
    def set_IdAlumno(self, idAlumno):    self.idAlumno = idAlumno

    def get_idUsuario(self):   return self.idUsuario
    def set_idUsuario(self, idUsuario):   self.idUsuario = idUsuario

    def get_nacimiento(self): return self.nacimiento
    def set_nacimiento(self, nacimiento):    self.nacimiento = nacimiento

    def get_carreraAlumno(self): return self.carreraAlumno
    def set_carreraAlumno(self, carreraAlumno):    self.carreraAlumno = carreraAlumno

    def get_grupoAlumno(self):   return self.grupoAlumno
    def set_grupoAlumno(self, grupoAlumno):   self.grupoAlumno = grupoAlumno
class Maestros:
    def __init__(self):
        self.idMaestro = None
        self.idUsuario = None
        self.idMaterias = None
        self.gradoEstudios = None
        

    def get_idMaestro(self):   return self.idMaestro
    def set_idMaestro(self, idMaestro):    self.idMaestro = idMaestro

    def get_idUsuario(self):   return self.idUsuario
    def set_idUsuario(self, idUsuario):   self.idUsuario = idUsuario

    def get_idMaterias(self): return self.idMaterias
    def set_idMaterias(self, idMaterias):    self.idMaterias = idMaterias

    def get_gradoEstudios(self):   return self.gradoEstudios
    def set_gradoEstudios(self, gradoEstudios):   self.gradoEstudios = gradoEstudios
class Aula:
    def __init__(self):
        self.idAula = None
        self.nombreAula = None
        self.edificioAula = None
        

    def get_idAula(self):   return self.idAula
    def set_idAula(self, idAula):    self.idAula = idAula

    def get_nombreAula(self):   return self.nombreAula
    def set_nombreAula(self, nombreAula):   self.nombreAula = nombreAula

    def get_edificioAula(self): return self.edificioAula
    def set_edificioAula(self, edificioAula):    self.edificioAula = edificioAula
class Carrera:
    def __init__(self):
        self.idCarrera = None
        self.nombreCarrera = None
        self.semestre = None
        

    def get_idCarrera(self):   return self.idCarrera
    def set_idCarrera(self, idCarrera):    self.idCarrera = idCarrera

    def get_nombreCarrera(self):   return self.nombreCarrera
    def set_nombreCarrera(self, nombreCarrera):   self.nombreCarrera = nombreCarrera

    def get_semestre(self): return self.semestre
    def set_semestre(self, semestre):    self.semestre = semestre
class Horario:
    def __init__(self):
        self.idHorario = None
        self.turnoHorario = None
        self.horaHorario = None
        

    def get_idHorario(self):   return self.idHorario
    def set_idHorario(self, idHorario):    self.idHorario = idHorario

    def get_turnoHorario(self):   return self.turnoHorario
    def set_turnoHorario(self, turnoHorario):   self.turnoHorario = turnoHorario

    def get_horaHorario(self): return self.horaHorario
    def set_horaHorario(self, horaHorario):    self.horaHorario = horaHorario
class Materia:
    def __init__(self):
        self.idMateria = None
        self.nombre = None
        self.horarioEntrada = None
        self.horarioSalida = None
        self.maestroMateria = None
        self.aulaMateria = None
        self.creditosMateria = None
        self.semestreMateria = None
        self.carreraMateria = None
        
    def get_idMateria(self):   return self.idMateria
    def set_idMateria(self, idMateria):    self.idMateria = idMateria

    def get_nombre(self):   return self.nombre
    def set_nombre(self, nombre):   self.nombre = nombre

    def get_horarioEntrada(self): return self.horarioEntrada
    def set_horarioEntrada(self, horarioEntrada):    self.horarioEntrada = horarioEntrada
    
    def get_horarioSalida(self): return self.horarioSalida
    def set_horarioSalida(self, horarioSalida):    self.horarioSalida = horarioSalida
    
    def get_maestroMateria(self): return self.maestroMateria
    def set_maestroMateria(self, maestroMateria):    self.maestroMateria = maestroMateria
    
    def get_aulaMateria(self): return self.aulaMateria
    def set_aulaMateria(self, aulaMateria):    self.aulaMateria = aulaMateria
    
    def get_creditosMateria(self): return self.creditosMateria
    def set_creditosMateria(self, creditosMateria):    self.creditosMateria = creditosMateria
    
    def get_semestreMateria(self): return self.semestreMateria
    def set_semestreMateria(self, semestreMateria):    self.semestreMateria = semestreMateria
    
    def get_carreraMateria(self): return self.carreraMateria
    def set_carreraMateria(self, carreraMateria):    self.carreraMateria = carreraMateria


def limpiarVentana(): #Limpiar pantalla
    for widget in root.winfo_children():
        widget.destroy()
def desactivarBoton(boton): #Desactivar botón
    boton.config(state="disabled")
def activarBoton(boton): #Activar botón
    boton.config(state="normal")

#Validaciones
def correoValido(correo):
    return re.match(r"[^@]+@[^@]+\.[^@]+", correo)
def contrasenaSegura(contrasena):
    return len(contrasena) >= 8 and \
            any(c.isupper() for c in contrasena) and \
            any(c.islower() for c in contrasena) and \
            any(c.isdigit() for c in contrasena)
def validarLetras(dato):
    patron = re.compile(r'[^a-zA-Z]')
    coincidencias = patron.search(dato)
    
    if not coincidencias:   return True
    else:   return False


#Carrera
def limpiarCamposCarrera():
    BuscarCarrera_entry.delete(0, tk.END)
    IdCarrera_entry.delete(0, tk.END)
    nombreCarrera_entry.delete(0, tk.END)
    semestreCarrera_entry.delete(0, tk.END)
def desactivarCamposCarrera():
    if 'BuscarCarrera_entry' in globals():
        BuscarCarrera_entry.config(state='disabled')
    if 'IdCarrera_entry' in globals():
        IdCarrera_entry.config(state='disabled')
    if 'nombreCarrera_entry' in globals():
        nombreCarrera_entry.config(state='disabled')
    if 'semestreCarrera_entry' in globals():
        semestreCarrera_entry.config(state='disabled')
def activarCamposCarrera():
    if 'BuscarCarrera_entry' in globals():
        BuscarCarrera_entry.config(state='normal')
    if 'IdCarrera_entry' in globals():
        IdCarrera_entry.config(state='normal')
    if 'nombreCarrera_entry' in globals():
        nombreCarrera_entry.config(state='normal')
    if 'semestreCarrera_entry' in globals():
        semestreCarrera_entry.config(state='normal')
def obtenerIdCarrera():
    sql = "SELECT MAX(id_carrera) FROM carrera"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def buscarCarrera(BuscarCarrera_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposCarrera()
    if BuscarCarrera_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    carreraId = int(BuscarCarrera_entry.get())
    carrera = db.buscarCarrera(carreraId)
    if carrera:
        activarCamposCarrera()
        if IdCarrera_entry:
            IdCarrera_entry.delete(0, END)
            IdCarrera_entry.insert(0, carrera[0])
            IdCarrera_entry.config(state='disabled')
        if nombreCarrera_entry:
            nombreCarrera_entry.delete(0, END)
            nombreCarrera_entry.insert(0, carrera[1])
        if semestreCarrera_entry:
            semestreCarrera_entry.delete(0, END)
            semestreCarrera_entry.insert(0, carrera[2])
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Carrera no encontrado.")      
def nuevoCarrera():
    activarCamposCarrera()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerIdCarrera()
    if IdCarrera_entry:
        IdCarrera_entry.config(state='normal')
        IdCarrera_entry.delete(0, END)
        IdCarrera_entry.insert(0, autoId)
        IdCarrera_entry.config(state='disabled')
def guardarCarrera():
    # Verificar si hay algún campo vacío
    if (not IdCarrera_entry.get() or
        not nombreCarrera_entry.get() or
        not semestreCarrera_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    carrera_id = int(IdCarrera_entry.get())

    carrera = Carrera()
    carrera.set_idCarrera(carrera_id)
    carrera.set_nombreCarrera(nombreCarrera_entry.get())
    carrera.set_semestre(semestreCarrera_entry.get())  
    db.guardarCarrera(carrera)

    activarCamposCarrera()
    limpiarCamposCarrera()
    desactivarCamposCarrera()
def editarCarrera():
    if (not IdCarrera_entry.get() or
        not nombreCarrera_entry.get() or
        not semestreCarrera_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    carrera_id = int(IdCarrera_entry.get())

    carrera = Carrera()
    carrera.set_idCarrera(carrera_id)
    carrera.set_nombreCarrera(nombreCarrera_entry.get())
    carrera.set_semestre(semestreCarrera_entry.get())  

    db.actualizarCarrera(carrera)

    activarCamposCarrera()
    limpiarCamposCarrera()
    desactivarBoton(botonCancelar)
    desactivarBoton(botonGuardar)
    desactivarBoton(botonEliminar)
def cancelarCarrera():
    activarCamposCarrera()
    limpiarCamposCarrera()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposCarrera()
def eliminarCarrera():
    idCarrera = int(IdCarrera_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarCarrera(idCarrera)
        activarCamposCarrera()
        limpiarCamposCarrera()
        desactivarCamposCarrera() 
def carrera(perfil_usuario):
    global BuscarCarrera_entry, IdCarrera_entry, nombreCarrera_entry, semestreCarrera_entry
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo

    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="CARRERA", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID Carrera:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarCarrera_entry = tk.Entry(usuariosRoot, width=20)
    BuscarCarrera_entry.grid(row=1, column=1)
    btnBuscarCarrera = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarCarrera(BuscarCarrera_entry), width=10)
    btnBuscarCarrera.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID Carrera:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    IdCarrera_entry = tk.Entry(usuariosRoot)
    IdCarrera_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    nombreCarrera_entry = tk.Entry(usuariosRoot)
    nombreCarrera_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Semestre:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    semestreCarrera_entry = tk.Entry(usuariosRoot)
    semestreCarrera_entry.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="w")
    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoCarrera)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarCarrera)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarCarrera, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarCarrera)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarCarrera)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    desactivarCamposCarrera()

#Horario
def limpiarCamposHorario():
    BuscarHorario_entry.delete(0, tk.END)
    IdHorario_entry.delete(0, tk.END)
    turno_var.set("")
    horaHorario_entry.delete(0, tk.END)
def desactivarCamposHorario():
    if 'BuscarHorario_entry' in globals():
        BuscarHorario_entry.config(state='disabled')
    if 'IdHorario_entry' in globals():
        IdHorario_entry.config(state='disabled')
    if 'turno_option' in globals():
        turno_option.config(state='disabled')
    if 'horaHorario_entry' in globals():
        horaHorario_entry.config(state='disabled')
def activarCamposHorario():
    if 'BuscarHorario_entry' in globals():
        BuscarHorario_entry.config(state='normal')
    if 'IdHorario_entry' in globals():
        IdHorario_entry.config(state='normal')
    if 'turno_option' in globals():
        turno_option.config(state='normal')
    if 'horaHorario_entry' in globals():
        horaHorario_entry.config(state='normal')
def obtenerIdHorario():
    sql = "SELECT MAX(id_horarios) FROM horarios"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def buscarHorario(BuscarHorario_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposHorario()
    if BuscarHorario_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    horarioId = int(BuscarHorario_entry.get())
    horario = db.buscarHorario(horarioId)
    if horario:
        activarCamposHorario()
        if IdHorario_entry:
            IdHorario_entry.delete(0, END)
            IdHorario_entry.insert(0, horario[0])
            IdHorario_entry.config(state='disabled')
        if turno_var:
            turno = horario[1] if horario[1] is not None and horario[1] != '' else ''
            turno_var.set(turno)
        if horaHorario_entry:
            horaHorario_entry.delete(0, END)
            horaHorario_entry.insert(0, horario[2])
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Horario no encontrado.")      
def nuevoHorario():
    activarCamposHorario()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerIdHorario()
    if IdHorario_entry:
        IdHorario_entry.config(state='normal')
        IdHorario_entry.delete(0, END)
        IdHorario_entry.insert(0, autoId)
        IdHorario_entry.config(state='disabled')
def guardarHorario():
    # Verificar si hay algún campo vacío
    if (not IdHorario_entry.get() or
        not turno_var.get() or
        not horaHorario_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    horario_id = int(IdHorario_entry.get())

    horario = Horario()
    horario.set_idHorario(horario_id)
    horario.set_turnoHorario(turno_var.get())
    horario.set_horaHorario(horaHorario_entry.get())  
    db.guardarHorario(horario)

    activarCamposHorario()
    limpiarCamposHorario()
    desactivarCamposHorario()
def editarHorario():
    if (not IdHorario_entry.get() or
        not turno_var.get() or
        not horaHorario_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    horario_id = int(IdHorario_entry.get())

    existing_horario = db.buscarHorario(horario_id)
    if existing_horario:
        # Si el horario existe, actualizamos sus atributos
        horario = Horario()
        horario.set_idHorario(horario_id)
        horario.set_turnoHorario(turno_var.get())
        horario.set_horaHorario(horaHorario_entry.get())  

        # Luego, actualizamos el horario en la base de datos
        db.actualizarHorario(horario)

        activarCamposHorario()
        limpiarCamposHorario()
        desactivarBoton(botonCancelar)
        desactivarBoton(botonGuardar)
        desactivarBoton(botonEliminar)
    else:
        # Si el horario no existe, mostramos un mensaje de error
        messagebox.showerror("Error", "El ID del horario no existe en la base de datos.")
def cancelarHorario():
    activarCamposHorario()
    limpiarCamposHorario()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposHorario()
def eliminarHorario():
    idHorario = int(IdHorario_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarHorario(idHorario)
        activarCamposHorario()
        limpiarCamposHorario()
        desactivarCamposCarrera() 
def horario(perfil_usuario):
    global BuscarHorario_entry, IdHorario_entry, turno_var, turno_option, horaHorario_entry
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo

    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="HORARIO", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID Horario:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarHorario_entry = tk.Entry(usuariosRoot, width=20)
    BuscarHorario_entry.grid(row=1, column=1)
    btnBuscarHorario = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarHorario(BuscarHorario_entry), width=10)
    btnBuscarHorario.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID Horario:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    IdHorario_entry = tk.Entry(usuariosRoot)
    IdHorario_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Turno:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    turno_var = tk.StringVar(usuariosRoot)
    turno_var.set("")
    turno_option = tk.OptionMenu(usuariosRoot, turno_var, "Matutino", "Vespertino")
    turno_option.config(width=13)
    turno_option.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Hora:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    horaHorario_entry = tk.Entry(usuariosRoot)
    horaHorario_entry.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="w")
    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoHorario)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarHorario)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarHorario, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarHorario)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarHorario)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    desactivarCamposHorario()


#Materias
def limpiarCamposMateria():
    BuscarMateria_entry.delete(0, tk.END)
    IdMateria_entry.delete(0, tk.END)
    nombreMateria_entry.delete(0, tk.END)
    horarioEntrada_entry.delete(0, tk.END)
    horarioSalida_entry.delete(0, tk.END)
    maestroMateria_entry.delete(0, tk.END)
    aulaMateria_entry.delete(0, tk.END)
    creditosMateria_entry.delete(0, tk.END)
    semestreMateria_entry.delete(0, tk.END)
    carreraMateria_entry.delete(0, tk.END)
def desactivarCamposMateria():
    if 'BuscarMateria_entry' in globals():
        BuscarMateria_entry.config(state='disabled')
    if 'IdMateria_entry' in globals():
        IdMateria_entry.config(state='disabled')
    if 'nombreMateria_entry' in globals():
        nombreMateria_entry.config(state='disabled')
    if 'horarioEntrada_entry' in globals():
        horarioEntrada_entry.config(state='disabled')
    if 'horarioSalida_entry' in globals():
        horarioSalida_entry.config(state='disabled')
    if 'maestroMateria_entry' in globals():
        maestroMateria_entry.config(state='disabled')
    if 'aulaMateria_entry' in globals():
        aulaMateria_entry.config(state='disabled')
    if 'creditosMateria_entry' in globals():
        creditosMateria_entry.config(state='disabled')
    if 'semestreMateria_entry' in globals():
        semestreMateria_entry.config(state='disabled')
    if 'carreraMateria_entry' in globals():
        carreraMateria_entry.config(state='disabled')
def activarCamposMateria():
    if 'BuscarMateria_entry' in globals():
        BuscarMateria_entry.config(state='normal')
    if 'IdMateria_entry' in globals():
        IdMateria_entry.config(state='normal')
    if 'nombreMateria_entry' in globals():
        nombreMateria_entry.config(state='normal')
    if 'horarioEntrada_entry' in globals():
        horarioEntrada_entry.config(state='normal')
    if 'horarioSalida_entry' in globals():
        horarioSalida_entry.config(state='normal')
    if 'maestroMateria_entry' in globals():
        maestroMateria_entry.config(state='normal')
    if 'aulaMateria_entry' in globals():
        aulaMateria_entry.config(state='normal')
    if 'creditosMateria_entry' in globals():
        creditosMateria_entry.config(state='normal')
    if 'semestreMateria_entry' in globals():
        semestreMateria_entry.config(state='normal')
    if 'carreraMateria_entry' in globals():
        carreraMateria_entry.config(state='normal')
def obtenerIdMateria():
    sql = "SELECT MAX(id_materia) FROM materias"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def buscarMateria(BuscarMateria_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposMateria()
    if BuscarMateria_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    materiaId = int(BuscarMateria_entry.get())
    materia = db.buscarMateria(materiaId)
    if materia:
        activarCamposHorario()
        if IdMateria_entry:
            IdMateria_entry.delete(0, END)
            IdMateria_entry.insert(0, horario[0])
            IdMateria_entry.config(state='disabled')
        if nombreMateria_entry:
            nombreMateria_entry.delete(0, END)
            nombreMateria_entry.insert(0, horario[2])
        if horarioEntrada_entry:
            horarioEntrada_entry.delete(0, END)
            horarioEntrada_entry.insert(0, horario[3])
        if horarioSalida_entry:
            horarioSalida_entry.delete(0, END)
            horarioSalida_entry.insert(0, horario[4])
        if maestroMateria_entry:
            maestroMateria_entry.delete(0, END)
            maestroMateria_entry.insert(0, horario[5])
        if aulaMateria_entry:
            aulaMateria_entry.delete(0, END)
            aulaMateria_entry.insert(0, horario[6])
        if creditosMateria_entry:
            creditosMateria_entry.delete(0, END)
            creditosMateria_entry.insert(0, horario[7])
        if semestreMateria_entry:
            semestreMateria_entry.delete(0, END)
            semestreMateria_entry.insert(0, horario[8])
        if carreraMateria_entry:
            carreraMateria_entry.delete(0, END)
            carreraMateria_entry.insert(0, horario[9])
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Materia no encontrada.")      
def nuevoMateria():
    activarCamposMateria()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerIdMateria()
    if IdMateria_entry:
        IdMateria_entry.config(state='normal')
        IdMateria_entry.delete(0, END)
        IdMateria_entry.insert(0, autoId)
        IdMateria_entry.config(state='disabled')
def guardarMateria():
    # Verificar si hay algún campo vacío
    if (not IdMateria_entry.get() or
        not nombreMateria_entry.get() or
        not horarioEntrada_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    horario_id = int(IdHorario_entry.get())

    horario = Horario()
    horario.set_idHorario(horario_id)
    horario.set_turnoHorario(turno_var.get())
    horario.set_horaHorario(horaHorario_entry.get())  
    db.guardarHorario(horario)

    activarCamposHorario()
    limpiarCamposHorario()
    desactivarCamposHorario()
def editarMateria():
    if (not IdHorario_entry.get() or
        not turno_var.get() or
        not horaHorario_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    horario_id = int(IdHorario_entry.get())

    existing_horario = db.buscarHorario(horario_id)
    if existing_horario:
        # Si el horario existe, actualizamos sus atributos
        horario = Horario()
        horario.set_idHorario(horario_id)
        horario.set_turnoHorario(turno_var.get())
        horario.set_horaHorario(horaHorario_entry.get())  

        # Luego, actualizamos el horario en la base de datos
        db.actualizarHorario(horario)

        activarCamposHorario()
        limpiarCamposHorario()
        desactivarBoton(botonCancelar)
        desactivarBoton(botonGuardar)
        desactivarBoton(botonEliminar)
    else:
        # Si el horario no existe, mostramos un mensaje de error
        messagebox.showerror("Error", "El ID del horario no existe en la base de datos.")
def cancelarMateria():
    activarCamposHorario()
    limpiarCamposHorario()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposHorario()
def eliminarMateria():
    idMateria = int(IdMateria_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarMateria(idMateria)
        activarCamposMateria()
        limpiarCamposMateria()
        desactivarCamposMateria() 
def materia(perfil_usuario):
    global BuscarMateria_entry, IdMateria_entry, nombreMateria_entry, horarioEntrada_entry, horarioSalida_entry, maestroMateria_entry, aulaMateria_entry, creditosMateria_entry, semestreMateria_entry, carreraMateria_entry
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo

    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="MATERIA", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID Materia:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarMateria_entry = tk.Entry(usuariosRoot, width=20)
    BuscarMateria_entry.grid(row=1, column=1)
    btnBuscarMateria = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarMateria(BuscarMateria_entry), width=10)
    btnBuscarMateria.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID Materia:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    IdMateria_entry = tk.Entry(usuariosRoot)
    IdMateria_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    nombreMateria_entry = tk.Entry(usuariosRoot)
    nombreMateria_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Horario entrada:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    horarioEntrada_entry = tk.Entry(usuariosRoot)
    horarioEntrada_entry.grid(row=4, column=1, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Horario salida:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    horarioSalida_entry = tk.Entry(usuariosRoot)
    horarioSalida_entry.grid(row=5, column=1, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Maestro:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    maestroMateria_entry = tk.Entry(usuariosRoot)
    maestroMateria_entry.grid(row=6, column=1, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Aula:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    aulaMateria_entry = tk.Entry(usuariosRoot)
    aulaMateria_entry.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Créditos:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
    creditosMateria_entry = tk.Entry(usuariosRoot)
    creditosMateria_entry.grid(row=3, column=3, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Semestre:").grid(row=4, column=2, padx=10, pady=5, sticky="w")
    semestreMateria_entry = tk.Entry(usuariosRoot)
    semestreMateria_entry.grid(row=4, column=3, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Carrera:").grid(row=5, column=2, padx=10, pady=5, sticky="w")
    carreraMateria_entry = tk.Entry(usuariosRoot)
    carreraMateria_entry.grid(row=5, column=3, padx=(0, 5), pady=5, sticky="w")
    
    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoMateria)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarMateria)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarMateria, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarMateria)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarMateria)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    desactivarCamposMateria()

#Aula
def limpiarCamposAula():
    BuscarAula_entry.delete(0, tk.END)
    IdAula_entry.delete(0, tk.END)
    nombreAula_entry.delete(0, tk.END)
    edificioAula_entry.delete(0, tk.END)
def desactivarCamposAula():
    if 'BuscarAula_entry' in globals():
        BuscarAula_entry.config(state='disabled')
    if 'IdAula_entry' in globals():
        IdAula_entry.config(state='disabled')
    if 'nombreAula_entry' in globals():
        nombreAula_entry.config(state='disabled')
    if 'edificioAula_entry' in globals():
        edificioAula_entry.config(state='disabled')
def activarCamposAula():
    if 'BuscarAula_entry' in globals():
        BuscarAula_entry.config(state='normal')
    if 'IdAula_entry' in globals():
        IdAula_entry.config(state='normal')
    if 'nombreAula_entry' in globals():
        nombreAula_entry.config(state='normal')
    if 'edificioAula_entry' in globals():
        edificioAula_entry.config(state='normal')
def obtenerIdAula():
    sql = "SELECT MAX(id_aula) FROM aula"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def buscarAula(BuscarAula_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposAula()
    if BuscarAula_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    aulaId = int(BuscarAula_entry.get())
    aula = db.buscarAula(aulaId)
    if aula:
        activarCamposAula()
        if IdAula_entry:
            IdAula_entry.delete(0, END)
            IdAula_entry.insert(0, aula[0])
            IdAula_entry.config(state='disabled')
        if nombreAula_entry:
            nombreAula_entry.delete(0, END)
            nombreAula_entry.insert(0, aula[1])
        if edificioAula_entry:
            edificioAula_entry.delete(0, END)
            edificioAula_entry.insert(0, aula[2])
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Aula no encontrado.")      
def nuevoAula():
    activarCamposAula()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerIdAula()
    if IdAula_entry:
        IdAula_entry.config(state='normal')
        IdAula_entry.delete(0, END)
        IdAula_entry.insert(0, autoId)
        IdAula_entry.config(state='disabled')
def guardarAula():
    # Verificar si hay algún campo vacío
    if (not IdAula_entry.get() or
        not nombreAula_entry.get() or
        not edificioAula_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    aula_id = int(IdAula_entry.get())

    aula = Aula()
    aula.set_idAula(aula_id)
    aula.set_nombreAula(nombreAula_entry.get())
    aula.set_edificioAula(edificioAula_entry.get())  # Aquí se usa gradoEstudios

    db.guardarAula(aula)

    activarCamposAula()
    limpiarCamposAula()
    desactivarCamposAula()
def editarAula():
    # Verificar si hay algún campo vacío
    if (not IdAula_entry.get() or
        not nombreAula_entry.get() or
        not edificioAula_entry.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    aula_id = int(IdAula_entry.get())

    aula = Aula()
    aula.set_idAula(aula_id)
    aula.set_nombreAula(nombreAula_entry.get())
    aula.set_edificioAula(edificioAula_entry.get())

    db.actualizarAula(aula)

    activarCamposAula()
    limpiarCamposAula()
    desactivarBoton(botonCancelar)
    desactivarBoton(botonGuardar)
    desactivarBoton(botonEliminar)
def cancelarAula():
    activarCamposAula()
    limpiarCamposAula()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposAula()
def eliminarAula():
    idAula = int(IdAula_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarAula(idAula)
        activarCamposAula()
        limpiarCamposAula()
        desactivarCamposAula() 
def aula(perfil_usuario):
    global BuscarAula_entry, IdAula_entry, nombreAula_entry, edificioAula_entry
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo

    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="AULAS", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID Aula:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarAula_entry = tk.Entry(usuariosRoot, width=20)
    BuscarAula_entry.grid(row=1, column=1)
    btnBuscarAula = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarAula(BuscarAula_entry), width=10)
    btnBuscarAula.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID Aula:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    IdAula_entry = tk.Entry(usuariosRoot)
    IdAula_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    nombreAula_entry = tk.Entry(usuariosRoot)
    nombreAula_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Edificio:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    edificioAula_entry = tk.Entry(usuariosRoot)
    edificioAula_entry.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="w")
    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoAula)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarAula)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarAula, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarAula)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarAula)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    desactivarCamposAula()

#Maestros
def limpiarCamposMaestros():
    BuscarMaestro_entry.delete(0, tk.END)
    IdMaestro_entry.delete(0, tk.END)
    IdUsuario_entry.delete(0, tk.END)
    nombreMateria.set("")
    gradoEstudios.set("")
def desactivarCamposMaestros():
    if 'BuscarMaestro_entry' in globals():
        BuscarMaestro_entry.config(state='disabled')
    if 'IdMaestro_entry' in globals():
        IdMaestro_entry.config(state='disabled')
    if 'IdUsuario_entry' in globals():
        IdUsuario_entry.config(state='disabled')
    if 'nombreMateria' in globals():
        nombreMateria.config(state='disabled')
    if 'gradoEstudios' in globals():
        gradoEstudios.config(state='disabled')
def activarCamposMaestros():
    if 'BuscarMaestro_entry' in globals():
        BuscarMaestro_entry.config(state='normal')
    if 'IdMaestro_entry' in globals():
        IdMaestro_entry.config(state='normal')
    if 'IdUsuario_entry' in globals():
        IdUsuario_entry.config(state='normal')
    if 'nombreMateria' in globals():
        nombreMateria.config(state='normal')
    if 'gradoEstudios' in globals():
        gradoEstudios.config(state='normal')
def obtenerIdMaestro():
    sql = "SELECT MAX(id_maestro) FROM maestros"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def buscarMaestro(BuscarMaestro_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposMaestros()
    if BuscarMaestro_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    maestroId = int(BuscarMaestro_entry.get())
    maestro = db.buscarMaestro(maestroId)
    if maestro:
        activarCamposMaestros()
        if IdMaestro_entry:
            IdMaestro_entry.delete(0, END)
            IdMaestro_entry.insert(0, maestro[0])
            IdMaestro_entry.config(state='disabled')
        if IdUsuario_entry:
            IdUsuario_entry.delete(0, END)
            IdUsuario_entry.insert(0, maestro[1])
        if nombreMateria:
            nombreMateria.delete(0, END)
            nombreMateria.insert(0, maestro[2])
        if gradoEstudios:
            gradoEstudios.delete(0, END)
            gradoEstudios.insert(0, maestro[3])
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Maestro no encontrado.")      
def nuevoMaestro():
    activarCamposMaestros()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerIdMaestro()
    if IdMaestro_entry:
        IdMaestro_entry.config(state='normal')
        IdMaestro_entry.delete(0, END)
        IdMaestro_entry.insert(0, autoId)
        IdMaestro_entry.config(state='disabled')
def guardarMaestro():
    # Verificar si hay algún campo vacío
    if (not IdMaestro_entry.get() or
        not IdUsuario_entry.get() or
        not nombreMateria.get() or
        not gradoEstudios.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return

    id_maestro = IdMaestro_entry.get()
    if db.buscarMaestroPorIdUsuario(id_maestro):
        messagebox.showerror("Error", "El ID de usuario ya está asociado a un alumno.")
        return

    perfil_usuario = db.obtenerPerfilUsuario(IdUsuario_entry.get())
    print("Perfil del usuario:", perfil_usuario)
    if perfil_usuario and 'Maestro' not in perfil_usuario:
        messagebox.showerror("Error", "El ID de usuario ingresado no tiene el perfil de alumno.")
        return

    maestro_id = int(IdMaestro_entry.get())

    maestro = Maestros()
    maestro.set_idMaestro(maestro_id)
    maestro.set_idUsuario(IdUsuario_entry.get())
    maestro.set_idMaterias(nombreMateria.get())
    maestro.set_gradoEstudios(gradoEstudios.get())  # Aquí se usa gradoEstudios

    db.guardarMaestro(maestro)

    activarCamposMaestros()
    limpiarCamposMaestros()
    desactivarCamposMaestros()
def editarMaestro():
    # Verificar si hay algún campo vacío
    if (not IdMaestro_entry.get() or
        not IdUsuario_entry.get() or
        not nombreMateria.get() or
        not gradoEstudios.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return
    
    id_maestro = IdMaestro_entry.get()
    if db.buscarMaestroPorIdUsuario(id_maestro):
        messagebox.showerror("Error", "El ID de usuario ya está asociado a un alumno.")
        return
    
    perfil_usuario = db.obtenerPerfilUsuario(IdUsuario_entry.get())
    print("Perfil del usuario:", perfil_usuario)
    if perfil_usuario and 'Maestro' not in perfil_usuario:
        messagebox.showerror("Error", "El ID de usuario ingresado no tiene el perfil de alumno.")
        return

    
    maestro_id = int(IdMaestro_entry.get())

    maestro = Maestros()
    maestro.set_idMaestro(maestro_id)
    maestro.set_idUsuario(IdUsuario_entry.get())
    maestro.set_idMaterias(nombreMateria.get())
    maestro.set_gradoEstudios(gradoEstudios.get())

    db.actualizarMaestro(maestro)

    activarCamposMaestros()
    limpiarCamposMaestros()
    desactivarBoton(botonCancelar)
    desactivarBoton(botonGuardar)
    desactivarBoton(botonEliminar)
def cancelarMaestro():
    activarCamposMaestros()
    limpiarCamposMaestros()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposMaestros()
def eliminarMaestro():
    idMaestro = int(IdMaestro_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarMaestro(idMaestro)
        activarCamposMaestros()
        limpiarCamposAlumnos()
        desactivarCamposMaestros() 
def maestros(perfil_usuario):
    global BuscarMaestro_entry, IdMaestro_entry, IdUsuario_entry, gradoEstudios, nombreMateria
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo

    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="MAESTROS", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID Maestro:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarMaestro_entry = tk.Entry(usuariosRoot, width=20)
    BuscarMaestro_entry.grid(row=1, column=1)
    btnBuscarMaestro = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarMaestro(BuscarMaestro_entry), width=10)
    btnBuscarMaestro.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID Maestro:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    IdMaestro_entry = tk.Entry(usuariosRoot)
    IdMaestro_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="ID Usuario:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    IdUsuario_entry = tk.Entry(usuariosRoot)
    IdUsuario_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Materias:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    nombreMateria = ttk.Combobox(usuariosRoot, width=17)  
    listaMaterias = db.getListaMaterias()
    nombresMaterias = [materia[0] for materia in listaMaterias]
    nombreMateria['values'] = nombresMaterias
    nombreMateria.grid(row=2, column=3)
    nombreMateria.config(state="disabled")
    
    tk.Label(usuariosRoot, text="Grado estudios:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
    grados_estudios = ["Primaria", "Secundaria", "Preparatoria", "Universidad"]  # Lista de valores para el grado de estudios
    gradoEstudios = ttk.Combobox(usuariosRoot, width=17, values=grados_estudios)  # Configuración del Combobox con los valores
    gradoEstudios.grid(row=3, column=3)
    gradoEstudios.config(state="disabled")

    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoMaestro)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarMaestro)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarMaestro, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarMaestro)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarMaestro)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    desactivarCamposMaestros()

#Alumnos
def generar_pdf():
    try:
        # Conexión a la base de datos
        conn = connect(host="localhost", user="root", password="", database="control")
        cursor = conn.cursor()

        # Consulta para obtener todos los datos de la tabla alumnos
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        # Crear un nuevo PDF
        c = canvas.Canvas("alumnos.pdf", pagesize=letter)
        y = 750  # Posición inicial en el eje y

        # Escribir los datos de los alumnos en el PDF
        for alumno in alumnos:
            c.drawString(100, y, f"ID Alumno: {alumno[0]}")
            c.drawString(100, y - 20, f"ID Usuario: {alumno[1]}")
            c.drawString(100, y - 40, f"Fecha de nacimiento: {alumno[2]}")
            c.drawString(100, y - 60, f"Carrera: {alumno[3]}")
            c.drawString(100, y - 80, f"Grupo: {alumno[4]}")
            y -= 100  # Actualizar la posición en el eje y para el próximo alumno

        # Guardar el PDF
        c.save()

        print("PDF generado correctamente.")

    except Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
def limpiarCamposAlumnos():
    IdAlumno_entry.delete(0, tk.END)
    IdUsuario_entry.delete(0, tk.END)
    nacimientoAlumno.set_date(datetime.now())
    carreraAlumno.set("")
    grupoAlumno.set("")
def desactivarCamposAlumnos():
    if 'IdAlumno_entry' in globals():
        IdAlumno_entry.config(state='disabled')
    if 'IdUsuario_entry' in globals():
        IdUsuario_entry.config(state='disabled')
    if 'nacimientoAlumno' in globals():
        nacimientoAlumno.config(state='disabled')
    if 'carreraAlumno' in globals():
        carreraAlumno.config(state='disabled')
    if 'grupoAlumno' in globals():
        grupoAlumno.config(state='disabled')
def activarCamposAlumnos():
    if 'IdAlumno_entry' in globals():
        IdAlumno_entry.config(state='normal')
    if 'IdUsuario_entry' in globals():
        IdUsuario_entry.config(state='normal')
    if 'nacimientoAlumno' in globals():
        nacimientoAlumno.config(state='normal')
    if 'carreraAlumno' in globals():
        carreraAlumno.config(state='normal')
    if 'grupoAlumno' in globals():
        grupoAlumno.config(state='normal')
def obtenerIdAlumno():
    sql = "SELECT MAX(id_alumno) FROM alumnos"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def buscarAlumno(BuscarAlumno_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposAlumnos()
    if BuscarAlumno_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    alumnoId = int(BuscarAlumno_entry.get())
    alumno = db.buscarAlumno(alumnoId)
    if alumno:
        activarCamposAlumnos()
        if IdAlumno_entry:
            IdAlumno_entry.delete(0, END)
            IdAlumno_entry.insert(0, alumno[0])
            IdAlumno_entry.config(state='disabled')
        if IdUsuario_entry:
            IdUsuario_entry.delete(0, END)
            IdUsuario_entry.insert(0, alumno[1])
        if nacimientoAlumno:
            nacimientoAlumno.delete(0, END)
            nacimientoAlumno.insert(0, alumno[2])
        if carreraAlumno:
            carreraAlumno.delete(0, END)
            carreraAlumno.insert(0, alumno[3])
        if grupoAlumno:
            grupoAlumno.delete(0, END)
            grupoAlumno.insert(0, alumno[4])
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Usuario no encontrado.")      
def nuevoAlumno():
    activarCamposAlumnos()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerIdAlumno()
    if IdAlumno_entry:
        IdAlumno_entry.config(state='normal')
        IdAlumno_entry.delete(0, END)
        IdAlumno_entry.insert(0, autoId)
        IdAlumno_entry.config(state='disabled')
def guardarAlumno():
    # Verificar si hay algún campo vacío
    if (not IdAlumno_entry.get() or
        not IdUsuario_entry.get() or
        not nacimientoAlumno.get() or
        not carreraAlumno.get() or
        not grupoAlumno.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return
    
    id_usuario = IdUsuario_entry.get()
    if db.buscarAlumnoPorIdUsuario(id_usuario):
        messagebox.showerror("Error", "El ID de usuario ya está asociado a un alumno.")
        return
    
    perfil_usuario = db.obtenerPerfilUsuario(IdUsuario_entry.get())
    print("Perfil del usuario:", perfil_usuario)
    if perfil_usuario and 'Alumno' not in perfil_usuario:
        messagebox.showerror("Error", "El ID de usuario ingresado no tiene el perfil de alumno.")
        return

    
    alumno_id = int(IdAlumno_entry.get())

    alumno = Alumnos()
    alumno.set_IdAlumno(alumno_id)
    alumno.set_idUsuario(IdUsuario_entry.get())
    alumno.set_nacimiento(nacimientoAlumno.get())
    alumno.set_carreraAlumno(carreraAlumno.get())
    alumno.set_grupoAlumno(grupoAlumno.get())

    db.guardarAlumno(alumno)

    activarCamposAlumnos()
    limpiarCamposAlumnos()
    desactivarCamposAlumnos()
    limpiarCamposAlumnos()
def editarAlumno():
    # Verificar si hay algún campo vacío
    if (not IdAlumno_entry.get() or
        not IdUsuario_entry.get() or
        not nacimientoAlumno.get() or
        not carreraAlumno.get() or
        not grupoAlumno.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return
    
    perfil_usuario = db.obtenerPerfilUsuario(IdUsuario_entry.get())
    print("Perfil del usuario:", perfil_usuario)
    if perfil_usuario and 'Alumno' not in perfil_usuario:
        messagebox.showerror("Error", "El ID de usuario ingresado no tiene el perfil de alumno.")
        return

    alumno_id = int(IdAlumno_entry.get())

    alumno = Alumnos()
    alumno.set_IdAlumno(alumno_id)
    alumno.set_idUsuario(IdUsuario_entry.get())
    alumno.set_nacimiento(nacimientoAlumno.get())
    alumno.set_carreraAlumno(carreraAlumno.get())
    alumno.set_grupoAlumno(grupoAlumno.get())

    db.actualizarAlumno(alumno)

    activarCamposAlumnos()
    limpiarCamposAlumnos()
    desactivarBoton(botonCancelar)
    desactivarBoton(botonGuardar)
    desactivarBoton(botonEliminar)
def cancelarAlumno():
    activarCamposAlumnos()
    limpiarCamposAlumnos()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposAlumnos()
def eliminarAlumno():
    idAlumno = int(IdAlumno_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarAlumno(idAlumno)
        activarCamposAlumnos()
        limpiarCamposAlumnos()
        desactivarCamposAlumnos() 
def alumnos(perfil_usuario):
    global BuscarAlumno_entry, IdAlumno_entry, IdUsuario_entry, nacimientoAlumno, carreraAlumno, grupoAlumno
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo

    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="ALUMNOS", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID ALlumno:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarAlumno_entry = tk.Entry(usuariosRoot, width=20)
    BuscarAlumno_entry.grid(row=1, column=1)
    btnBuscarAlumno = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarAlumno(BuscarAlumno_entry), width=10)
    btnBuscarAlumno.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID Alumno:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    IdAlumno_entry = tk.Entry(usuariosRoot)
    IdAlumno_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="ID Usuario:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    IdUsuario_entry = tk.Entry(usuariosRoot)
    IdUsuario_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Fecha de nacimiento:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    nacimientoAlumno = DateEntry(usuariosRoot, width=17)
    nacimientoAlumno.grid(row=4, column=1)
    nacimientoAlumno.config(state="disabled")

    tk.Label(usuariosRoot, text="Carrera:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    carreraAlumno = ttk.Combobox(usuariosRoot, width=17)  
    lista_carreras = db.getListaCarreras()
    nombres_carreras = [carrera[0] for carrera in lista_carreras]
    carreraAlumno['values'] = nombres_carreras
    carreraAlumno.grid(row=2, column=3)
    carreraAlumno.config(state="disabled")
    
    tk.Label(usuariosRoot, text="Grupo:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
    grupoAlumno = ttk.Combobox(usuariosRoot, width=17)  
    listaGrupos = db.getListaGrupos()
    nombresGrupos = [grupos[0] for grupos in listaGrupos]
    grupoAlumno['values'] = nombresGrupos
    grupoAlumno.grid(row=3, column=3)
    grupoAlumno.config(state="disabled")

    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoAlumno)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarAlumno)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarAlumno, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarAlumno)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarAlumno)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonPDF = tk.Button(usuariosRoot, text="Generar PDF", command=generar_pdf)
    botonPDF.grid(row=7, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    desactivarCamposAlumnos()

#Registro de Usuarios
def limpiarCamposUsuarios():
    usuarioID_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    ApellidoPaterno_entry.delete(0, tk.END)
    ApellidoMaterno_entry.delete(0, tk.END)
    Correo_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    perfil_var.set("")
    status_var.set("")
def desactivarCamposUsuarios():
    if 'usuarioID_entry' in globals():
        usuarioID_entry.config(state='disabled')
    if 'nombre_entry' in globals():
        nombre_entry.config(state='disabled')
    if 'ApellidoPaterno_entry' in globals():
        ApellidoPaterno_entry.config(state='disabled')
    if 'ApellidoMaterno_entry' in globals():
        ApellidoMaterno_entry.config(state='disabled')
    if 'Correo_entry' in globals():
        Correo_entry.config(state='disabled')
    if 'password_entry' in globals():
        password_entry.config(state='disabled')
    if 'perfil_option' in globals():
        perfil_option.config(state='disabled')
    if 'status_option' in globals():
        status_option.config(state='disabled')
def activarCamposUsuarios():
    if 'usuarioID_entry' in globals():
        usuarioID_entry.config(state='normal')
    if 'nombre_entry' in globals():
        nombre_entry.config(state='normal')
    if 'ApellidoPaterno_entry' in globals():
        ApellidoPaterno_entry.config(state='normal')
    if 'ApellidoMaterno_entry' in globals():
        ApellidoMaterno_entry.config(state='normal')
    if 'Correo_entry' in globals():
        Correo_entry.config(state='normal')
    if 'password_entry' in globals():
        password_entry.config(state='normal')
    if 'perfil_option' in globals():
        perfil_option.config(state='normal')
    if 'status_option' in globals():
        status_option.config(state='normal')
def obtenerId():
    sql = "SELECT MAX(id) FROM usuarios"
    db.cursor1.execute(sql)
    resultado = db.cursor1.fetchone()[0]
    if resultado is None:
        return 1
    else:
        return resultado + 1
def nuevoUsuario():
    activarCamposUsuarios()
    activarBoton(botonGuardar)
    activarBoton(botonCancelar)

    autoId = obtenerId()
    if usuarioID_entry:
        usuarioID_entry.config(state='normal')
        usuarioID_entry.delete(0, END)
        usuarioID_entry.insert(0, autoId)
        usuarioID_entry.config(state='disabled')
def guardarUsuario():
    # Verificar si hay algún campo vacío
    if (not usuarioID_entry.get() or
        not nombre_entry.get() or
        not ApellidoPaterno_entry.get() or
        not ApellidoMaterno_entry.get() or
        not Correo_entry.get() or
        not password_entry.get() or
        not perfil_var.get() or
        not status_var.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return
    
    if not contrasenaSegura(password_entry.get()):
        messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula y un número.")
        return
    
    if not correoValido(Correo_entry.get()):
        messagebox.showerror("Error", "El correo electrónico no es válido.")
        return
    if not validarLetras(nombre_entry.get()) and not validarLetras(ApellidoPaterno_entry.get()) and not validarLetras(ApellidoMaterno_entry.get()):
        messagebox.showerror("Error", "El dato ingresado no es válido.")
        return

    
    usuario_id = int(usuarioID_entry.get())

    usuario = Usuarios()
    usuario.set_usuario_id(usuario_id)
    usuario.set_nombre(nombre_entry.get())
    usuario.set_apellido_paterno(ApellidoPaterno_entry.get())
    usuario.set_apellido_materno(ApellidoMaterno_entry.get())
    usuario.set_correo(Correo_entry.get())
    usuario.set_contrasena(password_entry.get())
    usuario.set_perfil(perfil_var.get())
    usuario.set_status(status_var.get())

    db.guardarUsuario(usuario)

    activarCamposUsuarios()
    limpiarCamposUsuarios()
    desactivarCamposUsuarios()
    limpiarCamposUsuarios()
def cancelarUsuario():
    activarCamposUsuarios()
    limpiarCamposUsuarios()
    desactivarBoton(botonGuardar)
    desactivarBoton(botonCancelar)
    desactivarCamposUsuarios()
def editarUsuario():
    if (not usuarioID_entry.get() or
        not nombre_entry.get() or
        not ApellidoPaterno_entry.get() or
        not ApellidoMaterno_entry.get() or
        not Correo_entry.get() or
        not password_entry.get() or
        not perfil_var.get() or
        not status_var.get()
        ):
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de guardar.")
        return
    
    if not contrasenaSegura(password_entry.get()):
        messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula y un número.")
        return
    
    if not correoValido(Correo_entry.get()):
        messagebox.showerror("Error", "El correo electrónico no es válido.")
        return
    if not validarLetras(nombre_entry.get()) and not validarLetras(ApellidoPaterno_entry.get()) and not validarLetras(ApellidoMaterno_entry.get()):
        messagebox.showerror("Error", "El dato ingresado no es válido.")
        return

    usuario_id = int(usuarioID_entry.get())

    usuario = Usuarios()
    usuario.set_usuario_id(usuario_id)
    usuario.set_nombre(nombre_entry.get())
    usuario.set_apellido_paterno(ApellidoPaterno_entry.get())
    usuario.set_apellido_materno(ApellidoMaterno_entry.get())
    usuario.set_correo(Correo_entry.get())
    usuario.set_contrasena(password_entry.get())
    usuario.set_perfil(perfil_var.get())
    usuario.set_status(status_var.get())

    db.actualizarUsuario(usuario)

    activarCamposUsuarios()
    limpiarCamposUsuarios()
    desactivarBoton(botonCancelar)
    desactivarBoton(botonGuardar)
    desactivarBoton(botonEliminar)
def eliminarUsuario():
    usuario_id = int(usuarioID_entry.get())
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        db.eliminarUsuario(usuario_id)
        activarCamposUsuarios()
        limpiarCamposUsuarios()
        desactivarCamposUsuarios() 
def registro():
    global usuarioID_entry, nombre_entry, usuario_entry, password_entry, perfil_option, status_option, perfil_var, status_var, botonGuardar, botonCancelar, ApellidoPaterno_entry, ApellidoMaterno_entry, Correo_entry
    
    registrar_window = Toplevel(root)
    registrar_window.title("Registrar Usuario")
    registrar_window.geometry("600x350")
    registrar_window.resizable(0, 0)

    tk.Label(registrar_window, text="REGISTRO DE USUARIOS", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(registrar_window, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    usuarioID_entry = tk.Entry(registrar_window)
    usuarioID_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(registrar_window, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    nombre_entry = tk.Entry(registrar_window)
    nombre_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(registrar_window, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    ApellidoPaterno_entry = tk.Entry(registrar_window)
    ApellidoPaterno_entry.grid(row=4, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(registrar_window, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    ApellidoMaterno_entry = tk.Entry(registrar_window)
    ApellidoMaterno_entry.grid(row=5, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(registrar_window, text="Correo:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    Correo_entry = tk.Entry(registrar_window)
    Correo_entry.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="w")

    tk.Label(registrar_window, text="Contraseña:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
    password_entry = tk.Entry(registrar_window, show="*")
    password_entry.grid(row=3, column=3, padx=(0, 5), pady=5, sticky="w")

    tk.Label(registrar_window, text="Perfil:").grid(row=4, column=2, padx=10, pady=5, sticky="w")
    perfil_var = tk.StringVar(registrar_window)
    perfil_var.set("")
    perfil_option = tk.OptionMenu(registrar_window, perfil_var, "Administrador", "Maestro", "Alumno")
    perfil_option.config(width=13)
    perfil_option.grid(row=4, column=3, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(registrar_window, text="Status:").grid(row=5, column=2, padx=10, pady=5, sticky="w")
    status_var = tk.StringVar(registrar_window)
    status_var.set("")
    status_option = tk.OptionMenu(registrar_window, status_var, "Activo", "Inactivo")
    status_option.config(width=13)
    status_option.grid(row=5, column=3, padx=(0, 5), pady=5, sticky="w")

    padx_between_buttons = 5

    botonNuevo = tk.Button(registrar_window, text="Nuevo", command=nuevoUsuario)
    botonNuevo.grid(row=7, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(registrar_window, text="Guardar", command=guardarUsuario)
    botonGuardar.grid(row=7, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(registrar_window, text="Cancelar", command=cancelarUsuario)
    botonCancelar.grid(row=7, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")

    desactivarCamposUsuarios()

#Usuarios
def buscarUsuario(BuscarUsuario_entry):
    global botonCancelar, botonEditar, botonEliminar
    desactivarCamposUsuarios()
    if BuscarUsuario_entry is None:
        messagebox.showerror("Error", "El campo ID no está inicializado.")
        return
    
    usuarioId = int(BuscarUsuario_entry.get())
    usuario = db.buscarUsuario(usuarioId)
    if usuario:
        activarCamposUsuarios()
        if usuarioID_entry:
            usuarioID_entry.delete(0, END)
            usuarioID_entry.insert(0, usuario[0])
            usuarioID_entry.config(state='disabled')
        if nombre_entry:
            nombre_entry.delete(0, END)
            nombre_entry.insert(0, usuario[1])
        if ApellidoPaterno_entry:
            ApellidoPaterno_entry.delete(0, END)
            ApellidoPaterno_entry.insert(0, usuario[2])
        if ApellidoMaterno_entry:
            ApellidoMaterno_entry.delete(0, END)
            ApellidoMaterno_entry.insert(0, usuario[3])
        if Correo_entry:
            Correo_entry.delete(0, END)
            Correo_entry.insert(0, usuario[4])
        if password_entry:
            password_entry.delete(0, END)
            password_entry.insert(0, usuario[5])
        if perfil_var:
            perfil = usuario[6] if usuario[6] is not None and usuario[6] != '' else ''
            perfil_var.set(perfil)
        if status_var:
            status = usuario[7] if usuario[7] is not None and usuario[7] != '' else ''
            status_var.set(status)
        
        activarBoton(botonEliminar)
        activarBoton(botonEditar)
        activarBoton(botonCancelar)
    else:
        messagebox.showerror("Error", "Usuario no encontrado.")      
def usuarios(perfil_usuario):
    global usuarioID_entry, nombre_entry, ApellidoPaterno_entry, ApellidoMaterno_entry, Correo_entry, password_entry, perfil_option, status_option, perfil_var, status_var
    global botonGuardar, botonCancelar, botonEliminar, botonEditar, botonNuevo
    
    limpiarVentana()
    menu(perfil_usuario)  # Se pasa el perfil del usuario como argumento
    usuariosRoot = root

    tk.Label(usuariosRoot, text="USUARIOS", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="n")

    tk.Label(usuariosRoot, text="ID Usuario:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    BuscarUsuario_entry = tk.Entry(usuariosRoot, width=20)
    BuscarUsuario_entry.grid(row=1, column=1)
    btnBuscarUsuario = tk.Button(usuariosRoot, text="Buscar", command=lambda: buscarUsuario(BuscarUsuario_entry), width=10)
    btnBuscarUsuario.grid(row=1, column=2, padx=10, pady=10)
        
    tk.Label(usuariosRoot, text="ID:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    usuarioID_entry = tk.Entry(usuariosRoot)
    usuarioID_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Nombre:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    nombre_entry = tk.Entry(usuariosRoot)
    nombre_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Apellido Paterno:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    ApellidoPaterno_entry = tk.Entry(usuariosRoot)
    ApellidoPaterno_entry.grid(row=4, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Apellido Materno:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    ApellidoMaterno_entry = tk.Entry(usuariosRoot)
    ApellidoMaterno_entry.grid(row=5, column=1, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Correo:").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    Correo_entry = tk.Entry(usuariosRoot)
    Correo_entry.grid(row=2, column=3, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Contraseña:").grid(row=3, column=2, padx=10, pady=5, sticky="w")
    password_entry = tk.Entry(usuariosRoot, show="*")
    password_entry.grid(row=3, column=3, padx=(0, 5), pady=5, sticky="w")

    tk.Label(usuariosRoot, text="Perfil:").grid(row=4, column=2, padx=10, pady=5, sticky="w")
    perfil_var = tk.StringVar(usuariosRoot)
    perfil_var.set("")
    perfil_option = tk.OptionMenu(usuariosRoot, perfil_var, "Administrador", "Maestro", "Alumno")
    perfil_option.config(width=13)
    perfil_option.grid(row=4, column=3, padx=(0, 5), pady=5, sticky="w")
    
    tk.Label(usuariosRoot, text="Status:").grid(row=5, column=2, padx=10, pady=5, sticky="w")
    status_var = tk.StringVar(usuariosRoot)
    status_var.set("")
    status_option = tk.OptionMenu(usuariosRoot, status_var, "Activo", "Inactivo")
    status_option.config(width=13)
    status_option.grid(row=5, column=3, padx=(0, 5), pady=5, sticky="w")

    padx_between_buttons = 5

    botonNuevo = tk.Button(usuariosRoot, text="Nuevo", command=nuevoUsuario)
    botonNuevo.grid(row=6, column=0, padx=(2, padx_between_buttons), pady=5, sticky="ew")
    botonGuardar = tk.Button(usuariosRoot, text="Guardar", command=guardarUsuario)
    botonGuardar.grid(row=6, column=1, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEditar = tk.Button(usuariosRoot, text="Editar", command=editarUsuario, state="disabled")
    botonEditar.grid(row=6, column=2, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonCancelar = tk.Button(usuariosRoot, text="Cancelar", command=cancelarUsuario)
    botonCancelar.grid(row=6, column=3, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")
    botonEliminar = tk.Button(usuariosRoot, text="Eliminar", command=eliminarUsuario)
    botonEliminar.grid(row=6, column=4, padx=(padx_between_buttons, padx_between_buttons), pady=5, sticky="ew")

    desactivarCamposUsuarios()

#Inicio del sistema
def inicio(perfil_usuario):
    limpiarVentana()
    inicioVentana = root
    inicioVentana.geometry("600x350")
    inicioVentana.resizable(0, 0)

    tk.Label(inicioVentana, text="CONTROL ESCOLAR", font=("Arial", 20), padx=15, pady=20).grid(row=0, column=0, columnspan=2, pady=(20, 0))

    menu(perfil_usuario)  # Asegúrate de llamar a menu() después de crear la ventana y etiqueta de título
def menu(perfil_usuario): #Menú 
    menu_principal = tk.Menu(root)
    root.config(menu=menu_principal)

    menuOpciones = tk.Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label="Menú", menu=menuOpciones)
    menuOpciones.add_command(label="Inicio", command=lambda: inicio(perfil_usuario))  # Pasar el perfil del usuario al iniciar
    menuOpciones.add_separator()
    menuOpciones.add_command(label="Usuarios", command=lambda: usuarios(perfil_usuario))
    menuOpciones.add_command(label="Alumnos", command=lambda: alumnos(perfil_usuario))
    menuOpciones.add_command(label="Aulas", command=lambda: aula(perfil_usuario))
    menuOpciones.add_command(label="Maestros", command=lambda: maestros(perfil_usuario))
    menuOpciones.add_command(label="Materia", command=lambda: materia(perfil_usuario))
    menuOpciones.add_command(label="Grupos")
    menuOpciones.add_command(label="Planeación")
    menuOpciones.add_command(label="Horarios", command=lambda: horario(perfil_usuario))
    menuOpciones.add_command(label="Carrera", command=lambda: carrera(perfil_usuario))
    
    menuOpciones.add_separator()
    menuOpciones.add_command(label="Salir", command=root.quit)

#Inicio / Login
def login():
    correo = correoUsuario_entry.get()
    contrasena = password_entry.get()

    user_data = db.verificarLogin(correo, contrasena)

    if not user_data:
        messagebox.showerror("Error", "Usuario no encontrado.")
    else:
        perfil_usuario = user_data[6]  # Obtener el perfil del usuario desde la base de datos
        inicio(perfil_usuario)  # Pasar el perfil del usuario al iniciar sesión

# Crear la instancia de DBControl
db = DBControl()

# Crear la ventana principal
root = tk.Tk()
root.title("Control Escolar")

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Definir las dimensiones de la ventana y calcular la posición x centrada
window_width = 540
window_height = 290
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 3  # Centrado verticalmente pero ajustable

# Configurar la geometría de la ventana
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(0, 0)

# Crear los widgets de la interfaz gráfica
tk.Label(root, text="CONTROL ESCOLAR", font=("Arial", 32, "bold"), padx=50, pady=20).grid(row=0, column=0, columnspan=2, pady=(20, 0))

tk.Label(root, text="Correo:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
correoUsuario_entry = tk.Entry(root, bd=2, width=30)
correoUsuario_entry.grid(row=2, column=1, padx=(5,10), pady=10, sticky="w")

tk.Label(root, text="Contraseña:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(root, show="*", bd=2, width=30)
password_entry.grid(row=3, column=1, padx=(5,10), pady=10, sticky="w")

botonIngresar = tk.Button(root, text="Ingresar", command=login, cursor="hand2")
botonIngresar.grid(row=4, column=0, columnspan=2, padx=200, pady=10, sticky="ew")

textRegistrarse = tk.Label(root, text="¿No estás registrado? Regístrate aquí", fg="blue", cursor="hand2")
textRegistrarse.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
textRegistrarse.bind("<Button-1>", lambda e: registro())

# Iniciar el bucle principal del programa
root.mainloop()