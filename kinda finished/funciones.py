# Para iniciar, se necesita tener instalados:
# python -m pip install tkcalendar
# python -m pip install mysql-connector-python
# python.exe -m pip install --upgrade pip

# import funciones para mysql
from mysql.connector import connect, Error
# import funciones de validacion para contraseña
import re
# import tkinter y derivados
import tkinter as tk
from tkinter import messagebox
import tkcalendar


# Conexión a la base de datos "control" en MySQL --------------------------------------------------------------------
def conectarDB():
    host    = "localhost"
    user    = "root"
    password= ""
    database= "control"
    try:
        connection = connect(host=host, user=user, password=password, database=database)
            
        # Cursor para manipular funciones 
        cursor = connection.cursor()     
    # Verificación de conexión
    except Error as e:
        messagebox.showerror("Error", f"Error en conectar la BD: {e}")
    
    return connection, cursor

connection, cursor = conectarDB()
# Función para login -------------------------------------------------------------------------------------------------
# Verificar que el correo y la contraseña pertenezcan al mismo registro
def verificar_login(correo, contrasena):
    # Binary es para que sea sensible a mayus y minus
    cursor.execute("SELECT * FROM usuarios WHERE BINARY correo = %s AND BINARY contrasena = %s", (correo, contrasena))  
    # Regresar tupla de datos
    user_data = cursor.fetchone() 

    if user_data: 
        if user_data[7] == 'Inactivo':
            messagebox.showwarning("Error","Usuario Inactivo!")
            return None
        # Regresa todos los valores de un usuario en la forma
        # [0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status 	
        return user_data
    else: 
        messagebox.showwarning("Error","Login fail!")
        return None

# Funciones usuarios -------------------------------------------------------------------------------------------------
# Creación de usuario, se usará como "Guardar" en el programa
def nuevoUsuario(nombre, a_paterno, a_materno, correo, contrasena, perfil):
    # Revisar que no se registren dos usuarios con el mismo correo
    if not verifica_correo(correo):
        if validarContrasena(contrasena):
            insert_user = ("""
            INSERT INTO 
                usuarios (nombre, a_paterno, a_materno, correo, contrasena, perfil) 
            VALUES 
                (%s, %s, %s, %s, %s, %s)
            """)
            values = (nombre, a_paterno, a_materno, correo, contrasena, perfil)
            cursor.execute(insert_user, values)
            # Genera un id nuevo según su perfil
            if perfil == "Alumno":
                nuevoAlumno("","", getUltimoIdUsuarios(), "")
            if perfil == "Maestro":
                nuevoMaestro(getUltimoIdUsuarios(), "", "")
            # Guarda los cambios en la base de datos
            connection.commit()
    else:
        messagebox.showwarning("Error","El correo ya está registrado!")

# Editar usuario
def editarUsuario(id, nombre, a_paterno, a_materno, correo, contrasena, perfil):
    # Edita todos los atributos del usuario que tenga el id "id"
    editar_usuario = ("""
        UPDATE
            usuarios
        SET
            nombre = %s,
            a_paterno = %s,
            a_materno = %s,
            correo = %s,
            contrasena = %s,
            perfil = %s
        WHERE
            id = %s
    """)
    values = (nombre, a_paterno, a_materno, correo, contrasena, perfil, id)
    cursor.execute(editar_usuario, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Eliminar usuario PERMANENTEMENTE
# (es de apoyo pero en el código no se necesitará, espero)
def eliminarUsuario(id):
    eliminar_usuario = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(eliminar_usuario, id)
    # Guarda los cambios en la base de datos
    connection.commit()

# "Elimina" al usuario (lo deja inactivo) dejando sus datos
def desactivarUsuario(id):
    desactivar_usuario = ("UPDATE usuarios SET status = Inactivo' WHERE id = %s")
    values = (id,)
    cursor.execute(desactivar_usuario, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Busca un usuario por su id
def buscarIdUsuario(id):
    try:
        buscar_usuario = (f"SELECT * FROM usuarios WHERE id = {id}")
        cursor.execute(buscar_usuario)
        found_user = cursor.fetchone()
        # Método para que perfil y status no aparezcan como {''}, sino como ''
        found_list = list(found_user)
        perfil_str = ', '.join(found_user[6])
        status_str = ', '.join(found_user[7])
        found_list.pop(-1)
        found_list.pop(-1)
        found_list.append(perfil_str)
        found_list.append(status_str)
        found_tuple = tuple(found_list)
        # Se regresa el usuario encontrado de forma
        # [0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status 
        return found_tuple
    except:
        return None
    
    
# Busca un usuario por su correo
def buscarCorreoUsuario(correo):
    try:
        buscar_usuario = (f"SELECT * FROM usuarios WHERE correo = '{correo}'")
        cursor.execute(buscar_usuario)
        found_user = cursor.fetchone()
        # Método para que perfil y status no aparezcan como {''}, sino como ''
        found_list = list(found_user)
        perfil_str = ', '.join(found_user[6])
        status_str = ', '.join(found_user[7])
        found_list.pop(-1)
        found_list.pop(-1)
        found_list.append(perfil_str)
        found_list.append(status_str)
        found_tuple = tuple(found_list)
        # Se regresa el usuario encontrado de forma
        # [0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status 
        return found_tuple
    except:
        return None

# Mostrar lista de usuarios
def getListaUsuarios():
    show_user = "SELECT * FROM usuarios"
    cursor.execute(show_user)
    list_users = cursor.fetchall()
    # Se regresa como matriz de usuarios [m][n] donde 
        # m = usuarios registrados
        # n = atributos ([0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status )
    return list_users

# Verificar si existe el correo
def verifica_correo(correo):
    # Busca correos parecidos al ingresado por si ya está repetido
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
    return cursor.fetchone() is not None

# Último id ingresado (Para la hora de agregar un nuevo)
def getUltimoIdUsuarios():
    cursor.execute("SELECT MAX(id) FROM usuarios")
    result = cursor.fetchall()[0]
    
    if result[0] is not None:
        return result[0]
    else:
        return 0  
    
# Parámetros de validación para la contraseña
def validarContrasena(contrasena):
    # Verificar si la contraseña tiene al menos 8 caracteres
    if len(contrasena) < 8:
        messagebox.showwarning("Error","Contraseña debe de ser mayor a 8 dígitos!")
        return False   
    # Verificar si la contraseña tiene al menos una mayúscula
    if not re.search(r"[A-Z]", contrasena):
        messagebox.showwarning("Error","Contraseña Debe de tener como mínimo una mayúscula!")
        return False    
    # Verificar si la contraseña tiene al menos un carácter especial
    if not re.search(r"[!@#$%^&*()\-_=+{};:,]", contrasena):
        messagebox.showwarning("Error","Contraseña debe de tener un carácter especial!")
        return False   
    # Verificar si la contraseña tiene al menos un número
    if not re.search(r"\d", contrasena):
        messagebox.showwarning("Error","Contraseña debe de contener mínimo un número!")
        return False   
    return True

# Lista de los usuarios que únicamente son ALUMNOS
def getListaUsuariosAlumnos():
    mostrarAlumnos = "SELECT * FROM usuarios WHERE perfil = 'Alumno'"
    cursor.execute(mostrarAlumnos)
    list_users = cursor.fetchall()
    # Se regresa como matriz de usuarios [m][n] donde 
        # m = usuarios registrados
        # n = atributos ([0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status )
    return list_users    

# Lista de los usuarios que únicamente son MAESTROS
def getListaUsuariosMaestros():
    mostrarMaestros = "SELECT * FROM usuarios WHERE perfil = 'Maestro'"
    cursor.execute(mostrarMaestros)
    list_users = cursor.fetchall()
    # Se regresa como matriz de usuarios [m][n] donde 
        # m = usuarios registrados
        # n = atributos ([0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status )
    return list_users    



# Funciones alumnos -------------------------------------------------------------------------------------------------
# Creación de nuevo alumno, se usará como "Guardar" en el programa
def nuevoAlumno(nombre_carrera, id_grupo, id_usuario, fecha_nacimiento):
    agregar_alumno = ("""
    INSERT INTO 
        alumnos 
            (nombre_carrera, id_grupo, id_usuario, fecha_nacimiento) 
    VALUES 
        (%s, %s, %s, %s)
    """)
    values = (nombre_carrera, id_grupo, id_usuario, fecha_nacimiento)
    cursor.execute(agregar_alumno, values)
    connection.commit()

# Editar alumno
def editarAlumno(id_alumno, nombre_carrera, id_grupo, id_usuario, fecha_nacimiento):
    fecha_str = fecha_nacimiento.strftime("%Y-%m-%d")
    editar_alumno = ("""
        UPDATE
            alumnos
        SET
            nombre_carrera = %s, 
            id_grupo = %s, 
            id_usuario = %s, 
            fecha_nacimiento = %s
        WHERE
            id_alumno = %s
    """)
    values = (nombre_carrera, id_grupo, id_usuario, fecha_str, id_alumno)
    cursor.execute(editar_alumno, values)
    connection.commit()

# Eliminar alumno (esto lo borra PERMANENTEMENTE)
def eliminarAlumno(id_alumno):
    eliminar_alumno = "DELETE FROM alumnos WHERE id_alumno = %s"
    cursor.execute(eliminar_alumno, (id_alumno,))
    connection.commit()

# Buscar alumno por su id, regresa también sus datos de usuario
def buscarIdAlumno(id_alumno):
    try:
        buscar_alumno = ("SELECT * FROM alumnos WHERE id_alumno = %s")
        cursor.execute(buscar_alumno, (id_alumno,))
        alumno_encontrado = cursor.fetchone()
        # Se regresa el alumno encontrado de forma
        # [0]=id_alumno  [1]=nombre_carrera  [2]=id_grupo  [3]=id_usuario  [4]=fecha_nacimiento 
        # [5]=id  [6]=nombre  [7]=paterno  [8]=materno  [9]=correo  [10]=contraseña  [11]=perfil  [12]=status
        return alumno_encontrado + buscarIdUsuario(alumno_encontrado[3])
    except:
        return None

# Devuelve sólo el id de usuario de un alumno en específico
def getIdUsuarioDeAlumno(id_alumno):
    buscar_id = ("SELECT id_usuario FROM alumnos WHERE id_alumno = %s")
    cursor.execute(buscar_id, (id_alumno,))
    id_usuario = cursor.fetchone()
    return id_usuario[0]

# Busca a un alumno por su id de usuario
def getAlumnoDeIdUsuario(id_usuario):
    buscar_id = ("SELECT * FROM alumnos WHERE id_usuario = %s")
    cursor.execute(buscar_id, (id_usuario,))
    id_usuario = cursor.fetchone()
    return id_usuario

# Regresa la lista de alumnos registrados ()
def getListaAlumnos():
    mostrar_alumnos = "SELECT * FROM alumnos"
    cursor.execute(mostrar_alumnos)
    lista_alumnos = cursor.fetchall()
    # Se regresa como matriz de alumnos [m][n] donde 
    # m = alumnos registrados
    # n = atributos ([0]=id_alumno  [1]=nombre_carrera  [2]=id_grupo  [3]=id_usuario  [4]=fecha_nacimiento)
    return lista_alumnos

# Regresa el último id registrado (para poder mostrar la cuenta de alumnos totales)
def getUltimoIdAlumnos():
    cursor.execute("SELECT MAX(id_alumno) FROM alumnos")
    result = cursor.fetchall()[0]
    if result[0] is not None: return result[0]
    else: return 0


def getCarreraPorCorreo(correo):
    mostrarAlumno = f"SELECT * FROM usuarios WHERE perfil = 'Alumno' AND correo = '{correo}'"
    cursor.execute(mostrarAlumno)
    list_users = cursor.fetchall()[0]
    # Se regresa como matriz de usuarios [m][n] donde 
    # m = usuarios registrados
    # n = atributos ([0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status )
    if list_users:
        id_usuario = list_users[0]
        alumno = getAlumnoDeIdUsuario(id_usuario)
        #[0]=id_alumno  [1]=nombre_carrera  [2]=id_grupo  [3]=id_usuario  [4]=fecha_nacimiento
        return alumno
    else:
        return None


# Funciones maestros ----------------------------------------------------------------------------------------------
# Creación de nuevo maestro, se usará como "Guardar" en el programa
def nuevoMaestro(id_usuario, id_materias, grado_estudios):
    agregar_maestro = ("""
    INSERT INTO 
        maestros 
            (id_usuario, id_materias, grado_estudios) 
    VALUES 
        (%s, %s, %s)
    """)
    values = (id_usuario, id_materias, grado_estudios)
    cursor.execute(agregar_maestro, values)
    connection.commit()

# Editar maestro
def editarMaestro(id_maestro, id_usuario, grado_estudios):
    editar_maestro = ("""
        UPDATE
            maestros
        SET
            id_usuario = %s, 
            grado_estudios = %s
        WHERE
            id_maestro = %s
    """)
    values = (id_usuario, grado_estudios, id_maestro)
    cursor.execute(editar_maestro, values)
    connection.commit()

# Eliminar maestro (esto lo borra PERMANENTEMENTE)
def eliminarMaestro(id_maestro):
    eliminar_maestro = "DELETE FROM alumnos WHERE id_maestro = %s"
    cursor.execute(eliminar_maestro, (id_maestro,))
    connection.commit()

# Buscar maestro por su id, regresa también sus datos de usuario
def buscarIdMaestro(id_maestro):
    try:
        buscar_maestro = (f"SELECT * FROM maestros WHERE id_maestro = {id_maestro}")
        cursor.execute(buscar_maestro)
        maestro_encontrado = cursor.fetchone()
        # Se regresa el maestro encontrado de forma
        # [0]=id_maestro, [1]=id_usuario, [2]=id_materias, [3]=grado_estudios
        # [4]=id  [5]=nombre  [6]=paterno  [7]=materno  [8]=correo  [9]=contraseña  [10]=perfil  [11]=status
        return maestro_encontrado + buscarIdUsuario(maestro_encontrado[1])
    except:
        return None

# Devuelve sólo el id de usuario de un maestro en específico
def getIdUsuarioDeMaestro(id_maestro):
    buscar_id = ("SELECT id_usuario FROM maestros WHERE id_maestro = %s")
    cursor.execute(buscar_id, (id_maestro,))
    id_usuario = cursor.fetchone()
    return id_usuario[0]

# Regresa la lista de maestros registrados ()
def getListaMaestros():
    mostrar_maestros = "SELECT * FROM maestros"
    cursor.execute(mostrar_maestros)
    lista_maestros = cursor.fetchall()
    # Se regresa como matriz de maestros [m][n] donde 
    # m = maestros registrados
    # n = atributos ([0]=id_maestro, [1]=id_usuario, [2]=id_materias, [3]=grado_estudios)
    return lista_maestros


# Regresa el último id registrado (para poder mostrar la cuenta de maestros totales)
def getUltimoIdMaestros():
    cursor.execute("SELECT MAX(id_maestro) FROM maestros")
    result = cursor.fetchall()[0]
    if result[0] is not None: return result[0]
    else: return 0

# Funciones carrera ----------------------------------------------------------------------------------------------
# Creación de carrera, se usará como "Guardar" en el programa
def nuevaCarrera(nombre, semestre):
    agregar_carrera = ("INSERT INTO carrera (nombre, semestre) VALUES (%s, %s) ")
    values = (nombre, semestre)
    cursor.execute(agregar_carrera, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Editar carrera
def editarCarrera(id_carrera, nombre, semestre):
    # Edita todos los atributos del carrera que tenga el id "id_carrera"
    editar_carrera = ("""
        UPDATE
            carrera
        SET
            nombre = %s, 
            semestre = %s
        WHERE
            id_carrera = %s
    """)
    values = (nombre, semestre, id_carrera)
    cursor.execute(editar_carrera, values)    
    # Guarda los cambios en la base de datos
    connection.commit()

# Eliminar carrera PERMANENTEMENTE
# (es de apoyo pero en el código no se necesitará)
def eliminarCarrera(id_carrera):
    eliminar_carrera = "DELETE FROM carrera WHERE id_carrera = %s"
    cursor.execute(eliminar_carrera, id_carrera)    
    # Guarda los cambios en la base de datos
    connection.commit()

# Busca una carrera por su id
def buscarIdCarrera(id_carrera):
    try:
        buscar_carrera = (f"SELECT * FROM carrera WHERE id_carrera = {id_carrera}")
        cursor.execute(buscar_carrera)
        carrera_encontrada = cursor.fetchone()
        # Se regresa el carrera encontrada de forma
        # [0]=id_carrera, [1]=nombre, [2]=semestre
        return carrera_encontrada
    except:
        return None
    
# Busca una carrera por su nombre
def buscarNombreCarrera(nombre):
    try:
        buscar_carrera = (f"SELECT * FROM carrera WHERE nombre = '{nombre}'")
        cursor.execute(buscar_carrera)
        carrera_encontrada = cursor.fetchall()
        # Se regresa el carrera encontrada de forma
        # [0]=id_carrera, [1]=nombre, [2]=semestre
        return carrera_encontrada[0]
    except:
        return None

# Mostrar lista de carreras
def getListaCarreras():
    mostrar_carreras = "SELECT nombre FROM carrera"
    cursor.execute(mostrar_carreras)
    lista_carreras = cursor.fetchall()  
    return lista_carreras

# Último id ingresado (Para la hora de agregar uno nuevo)
def getUltimoIdCarreras():
    cursor.execute("SELECT MAX(id_carrera) FROM carrera")
    result = cursor.fetchall()[0]    
    if result[0] is not None: return result[0]
    else: return 0

# Funciones materias ----------------------------------------------------------------------------------------------
# Creación de materia, se usará como "Guardar" en el programa
def nuevaMateria(nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera):
    agregar_materia = ("""
    INSERT INTO 
        materias 
            (nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera) 
    VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    values = (nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera)
    cursor.execute(agregar_materia, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Editar materia
def editarMateria(id_materia, nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera):
    # Edita todos los atributos de la materia que tenga el id "id_materia"
    editar_materia = ("""
        UPDATE
            materias
        SET
            nombre = %s,
            horario_entrada = %s,
            horario_salida = %s,
            dia = %s,
            maestro = %s,  
            aula = %s,
            creditos = %s, 
            semestre = %s, 
            carrera = %s
        WHERE
            id_materia = %s
    """)
    values = (nombre, horario_entrada, horario_salida, dia, maestro, aula, creditos, semestre, carrera, id_materia)
    cursor.execute(editar_materia, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Eliminar materia PERMANENTEMENTE
# (es de apoyo pero en el código no se necesitará)
def eliminarMateria(id_materias):
    eliminar_materia = "DELETE FROM materias WHERE id_materia = %s"
    cursor.execute(eliminar_materia, id_materias)
    # Guarda los cambios en la base de datos
    connection.commit()

# Busca una materia por su id
def buscarIdMateria(id_materia):
    try:
        buscar_materia = (f"SELECT * FROM materias WHERE id_materia = {id_materia}")
        cursor.execute(buscar_materia)
        materia_encontrada = cursor.fetchone()
        # Se regresa la materia encontrada de forma
        # [0]=id_materia, [1]=nombre, [2]=horario_entrada, [3]=horario_salida, [4]=dia, [5]=maestro, [6]=aula, [7]=creditos, [8]=semestre, [9]=carrera
        return materia_encontrada
    except:
        return None

# Mostrar lista de materias
def getListaMaterias():
    mostrar_materias = "SELECT * FROM materias"
    cursor.execute(mostrar_materias)
    lista_materias = cursor.fetchall()
    # Se regresa como matriz de materias [m][n] donde 
        # m = materias registradas
        # n = atributos ([0]=id_materia, [1]=nombre, [2]=horario_entrada, [3]=horario_salida, [4]=dia, [5]=maestro, [6]=aula, [7]=creditos, [8]=semestre, [9]=carrera)
    return lista_materias

# Mostrar lista de materias pero en las que específicamente un maestro las imparta
def getMateriasDelMaestro(maestro):
    mostrar_materias = "SELECT nombre FROM materias WHERE maestro = %s"
    cursor.execute(mostrar_materias, (maestro,))
    lista_materias = cursor.fetchall() 
    lista_bonita = []
    for materia in lista_materias:
        lista_bonita.append(materia[0])
    return tuple(lista_bonita)

# Mostrar lista de materias pero de una carrera solamente
def getMateriasDeCarrera(carrera):
    mostrar_materias = "SELECT * FROM materias WHERE carrera = %s"
    cursor.execute(mostrar_materias, (carrera,))
    lista_materias = cursor.fetchall() 
    lista_bonita = []
    for materia in lista_materias:
        lista_bonita.append(materia)
        # n = atributos ([0]=id_materia, [1]=nombre, [2]=horario_entrada, [3]=horario_salida, [4]=dia, [5]=maestro, [6]=aula, [7]=creditos, [8]=semestre, [9]=carrera)
    return lista_bonita

# Último id ingresado (Para la hora de agregar una nueva)
def getUltimoIdMaterias():
    cursor.execute("SELECT MAX(id_materia) FROM materias")
    result = cursor.fetchall()[0]
    if result[0] is not None: return result[0]
    else: return 0

# Funciones aulas ----------------------------------------------------------------------------------------------
# Creación de aula, se usará como "Guardar" en el programa
def nuevaAula(nombre, edificio):
    agregar_aula = ("INSERT INTO aula (nombre, edificio, nombre_completo) VALUES (%s, %s, %s)")
    values = (nombre, edificio, edificio+"-"+nombre)
    cursor.execute(agregar_aula, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Editar aula
def editarAula(id_aula, nombre, edificio):
    # Edita todos los atributos del aula que tenga el id "id_aula"
    editar_aula = ("""
        UPDATE
            aula
        SET
            nombre = %s, 
            edificio = %s,
            nombre_completo = %s
        WHERE
            id_aula = %s
    """)
    values = (nombre, edificio, edificio+"-"+nombre, id_aula)
    cursor.execute(editar_aula, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Eliminar aula PERMANENTEMENTE
# (es de apoyo pero en el código no se necesitará)
def eliminarAula(id_aula):
    eliminar_aula = "DELETE FROM aula WHERE id_aula = %s"
    cursor.execute(eliminar_aula, id_aula)
    # Guarda los cambios en la base de datos
    connection.commit()

# Busca un aula por su id
def buscarIdAula(id_aula):
    try:
        buscar_aulas = (f"SELECT * FROM aula WHERE id_aula = {id_aula}")
        cursor.execute(buscar_aulas)
        aula_encontrada = cursor.fetchone()
        # Se regresa el aula encontrada de forma
        # [0]=id_aula, [1]=nombre, [2]=edificio, [3]=nombre_completo
        return aula_encontrada
    except:
        return None
    
# Busca un aula por su nombre
def buscarNombredAula(nombre):
    try:
        buscar_aulas = (f"SELECT * FROM aula WHERE nombre = {nombre}")
        cursor.execute(buscar_aulas)
        aula_encontrada = cursor.fetchone()
        # Se regresa el aula encontrada de forma
        # [0]=id_aula, [1]=nombre, [2]=edificio, [3]=nombre_completo
        return aula_encontrada
    except:
        return None
    
# Busca un aula por su nombre completo
def buscarNombreCompletoAula(nombre_completo):
    try:
        buscar_aulas = (f"SELECT * FROM aula WHERE nombre_completo = '{nombre_completo}'")
        cursor.execute(buscar_aulas)
        aula_encontrada = cursor.fetchone()
        # Se regresa el aula encontrada de forma
        # [0]=id_aula, [1]=nombre, [2]=edificio, [3]=nombre_completo
        return aula_encontrada
    except:
        return None

# Mostrar lista de aulas
def getListaAulas():
    mostrar_aulas = "SELECT * FROM aula"
    cursor.execute(mostrar_aulas)
    lista_aulas = cursor.fetchall()
    # Se regresa como matriz de aulas [m][n] donde 
        # m = aula registrados
        # n = atributos ([0]=id_aula, [1]=nombre, [2]=edificio, [3]=nombre_completo)
    return lista_aulas

# Último id ingresado (Para la hora de agregar uno nuevo)
def getUltimoIdAulas():
    cursor.execute("SELECT MAX(id_aula) FROM aula")
    result = cursor.fetchall()[0]
    if result[0] is not None: return result[0]
    else: return 0

# Funciones grupos ----------------------------------------------------------------------------------------------
# Creación de grupo, se usará como "Guardar" en el programa
def nuevoGrupo(id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn):
    agregar_grupo = ("""
    INSERT INTO 
        grupos 
            (id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn) 
    VALUES 
        (%s, %s, %s, %s, %s, %s)
    """)
    values = (id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn)
    cursor.execute(agregar_grupo, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Editar grupo
def editarGrupo(id_grupos, id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn):
    # Edita todos los atributos del grupo que tenga el id "id_grupos"
    editar_grupo = ("""
        UPDATE
            grupos
        SET
            id_carrera = %s, 
            id_materia = %s, 
            id_alumnos = %s, 
            salon = %s, 
            semestre = %s, 
            max_alumn = %s
        WHERE
            id_grupos = %s
    """)
    values = (id_carrera, id_materia, id_alumnos, salon, semestre, max_alumn, id_grupos)
    cursor.execute(editar_grupo, values)
    # Guarda los cambios en la base de datos
    connection.commit()

# Eliminar grupo PERMANENTEMENTE
# (es de apoyo pero en el código no se necesitará)
def eliminarGrupo(id_grupos):
    eliminar_grupo = "DELETE FROM grupos WHERE id_grupos = %s"
    cursor.execute(eliminar_grupo, id_grupos)
    # Guarda los cambios en la base de datos
    connection.commit()

# Busca un grupo por su id
def buscarIdGrupo(id_grupos):
    try:
        buscar_grupo = (f"SELECT * FROM grupos WHERE id_grupos = {id_grupos}")
        cursor.execute(buscar_grupo)
        grupo_encontrado = cursor.fetchone()
        # Se regresa el grupo encontrada de forma
        # [0]=id_grupos, [1]=id_carrera, [2]=id_materia, [3]=id_alumnos, [4]=salon, [5]=semestre, [6]=max_alumn
        return grupo_encontrado
    except:
        return None

# Mostrar lista de grupos
def getListaGrupos():
    mostrar_grupos = "SELECT * FROM grupos"
    lista_grupos = []
    cursor.execute(mostrar_grupos)
    lista_grupos = cursor.fetchall()
    # Se regresa como matriz de grupos [m][n] donde 
        # m = grupos registrados
        # n = atributos ([0]=id_grupos, [1]=id_carrera, [2]=id_materia, [3]=id_alumnos, [4]=salon, [5]=semestre, [6]=max_alumn)
    return lista_grupos

# Último id ingresado (Para la hora de agregar uno nuevo)
def getUltimoIdGrupos():
    cursor.execute("SELECT MAX(id_grupos) FROM grupos")
    result = cursor.fetchall()[0]
    if result[0] is not None: return result[0]
    else: return 0










# Ejecutor "main" -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Executing...\n")
    
    #verificar_login(correo="ejemplo@gmail.com", contrasena="Pw123")
    #nuevoUsuario("Ramiro", "Lupercio", "Coronel", "ramiro@gmail.com", "Contrasena123$", "Maestro", "Activo")
    #print(buscarIdUsuario(3))
    #print("Usuarios\n", getListaUsuarios())
    #print("Alumnos\n",getListaUsuariosAlumnos())
    #print("Maestros\n",getListaUsuariosMaestros())
    #print(getListaAlumnos())
    #print(buscarIdAlumno(1))
    #print(getListaMaestros())
    #print(buscarIdMaestro(1))
    #nuevaCarrera("Ingeniería Informática", 9)
    #editarCarrera(0, "Ingeniería en Computación", 9)
    #print(buscarIdCarrera(0))
    #print(getListaCarreras())
    #editarMateria(1, "Programación Orientada a Objetos", "9:00:00", "10:50:00", "Maestro García Gómez", "LC05", 8, 3, "Ingeniería Informática")
    #editarMateria(4, "Ingeniería de Software", "11:00:00", "12:50:00", "Maestro García Gómez", "LC01", 8, 6, "Ingeniería en Computación")
    #nuevaMateria("Ingeniería de Software", "11:00", "12:50", "Maestro García Gómez", 8, 6, "Ingeniería en Computación")
    #print(getListaMaterias())
    #nuevaAula("LC05", "DUCT2")
    #print(getListaAulas())
    #editarUsuario(6, "Edgar", "Zepeda", "Urzúa", "edgar@gmail.com", "Pw123", "Alumno", "Activo")
    #nuevoUsuario("Jovita", "Pérez", "Solís", "jovita@gmail.com", "Jovis123$", "Maestro", "Activo")
    #print(getCarreraPorCorreo("andre@gmail.com"))
        # n = atributos ([0]=id  [1]=nombre  [2]=paterno  [3]=materno  [4]=correo  [5]=contraseña  [6]=perfil  [7]=status )
    #print(getMateriasDeCarrera("Ingeniería Informática"))
    print(buscarIdUsuario(4))

    print(buscarCorreoUsuario("ejemplo@gmail.com"))

    print("\nFinishing...")
    