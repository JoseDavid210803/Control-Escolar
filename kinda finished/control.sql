-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-05-2024 a las 15:15:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `control`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `id_alumno` int(11) NOT NULL,
  `nombre_carrera` varchar(25) DEFAULT NULL,
  `id_grupo` int(11) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`id_alumno`, `nombre_carrera`, `id_grupo`, `id_usuario`, `fecha_nacimiento`) VALUES
(1, 'Ingeniería en Computación', NULL, 2, '2001-02-03'),
(2, 'Ingeniería Informática', NULL, 4, '2006-07-06'),
(3, 'Ingeniería en Computación', NULL, 6, '2000-11-15'),
(4, 'Ingeniería en Computación', NULL, 9, '2024-05-10'),
(5, 'Ingeniería Informática', NULL, 10, '2004-12-22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aula`
--

CREATE TABLE `aula` (
  `id_aula` int(11) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  `edificio` varchar(10) NOT NULL,
  `nombre_completo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aula`
--

INSERT INTO `aula` (`id_aula`, `nombre`, `edificio`, `nombre_completo`) VALUES
(1, 'LC01', 'DUCT1', 'DUCT1-LC01'),
(2, 'LC05', 'DUCT2', 'DUCT2-LC05'),
(3, 'A005', 'DEDX', 'DEDX-A005'),
(4, 'A008', 'DEDX', 'DEDX-A008'),
(5, 'A018', 'DEDV', 'DEDV-A018');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `id_carrera` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `semestre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`id_carrera`, `nombre`, `semestre`) VALUES
(1, 'Ingeniería en Computación', '10'),
(2, 'Ingeniería Informática', '9'),
(3, 'Ingeniería Civíl', '8'),
(4, 'Licenciatura en Física', '10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `id_grupos` int(20) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `id_alumnos` int(11) NOT NULL,
  `salon` varchar(5) NOT NULL,
  `semestre` varchar(20) NOT NULL,
  `max_alumn` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `grupos`
--

INSERT INTO `grupos` (`id_grupos`, `id_carrera`, `id_materia`, `id_alumnos`, `salon`, `semestre`, `max_alumn`) VALUES
(1, 1, 1, 1, 'LC01', '5', 35);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestros`
--

CREATE TABLE `maestros` (
  `id_maestro` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_materias` int(11) DEFAULT NULL,
  `grado_estudios` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `maestros`
--

INSERT INTO `maestros` (`id_maestro`, `id_usuario`, `id_materias`, `grado_estudios`) VALUES
(1, 3, NULL, 'Normal Superior'),
(2, 5, NULL, 'Normal Superior'),
(3, 7, 0, 'Doctorado'),
(4, 8, 0, 'Normal Superior');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `id_materia` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `horario_entrada` time NOT NULL,
  `horario_salida` time NOT NULL,
  `dia` enum('Lunes','Martes','Miércoles','Jueves','Viernes') DEFAULT NULL,
  `maestro` varchar(255) NOT NULL,
  `aula` varchar(255) NOT NULL,
  `creditos` int(11) NOT NULL,
  `semestre` varchar(15) NOT NULL,
  `carrera` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`id_materia`, `nombre`, `horario_entrada`, `horario_salida`, `dia`, `maestro`, `aula`, `creditos`, `semestre`, `carrera`) VALUES
(1, 'Programación Orientada a Objetos', '09:00:00', '10:50:00', 'Miércoles', 'Maestro García Gómez', 'LC05-DUCT2', 8, '3', 'Ingeniería Informática'),
(4, 'Ingeniería de Software', '11:00:00', '12:50:00', 'Miércoles', 'Maestro García Gómez', 'LC01-DUCT1', 8, '6', 'Ingeniería en Computación'),
(6, 'Estructura de Datos', '09:00:00', '10:50:00', 'Lunes', 'Jovita Pérez Solís', 'A005 DEDX', 6, '3', 'Ingeniería Informática'),
(7, 'Bases de Datos', '07:00:00', '08:50:00', 'Martes', 'Ramiro Lupercio Coronel', 'LC01-DUCT1', 6, '2', 'Ingeniería Informática'),
(8, 'Física I', '07:00:00', '10:50:00', 'Jueves', 'Fernanda Solórzano Maldonado', 'A018-DEDV', 8, '1', 'Licenciatura en Física');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `a_paterno` varchar(15) NOT NULL,
  `a_materno` varchar(15) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contrasena` varchar(15) NOT NULL,
  `perfil` set('Alumno','Maestro','Administrador','') NOT NULL,
  `status` set('Activo','Inactivo') NOT NULL DEFAULT 'Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `a_paterno`, `a_materno`, `correo`, `contrasena`, `perfil`, `status`) VALUES
(1, 'Ejemplo', 'Gómez', 'Rodríguez', 'ejemplo@gmail.com', 'Pw123', 'Administrador', 'Activo'),
(2, 'Alumno', 'Jiménez', 'Robles', 'alumno@gmail.com', 'Pw123', 'Alumno', 'Activo'),
(3, 'Maestro', 'García', 'Gómez', 'maestro@gmail.com', 'Pw123', 'Maestro', 'Activo'),
(4, 'André', 'Solórzano', 'Maldonado', 'andre@gmail.com', 'Pw123', 'Alumno', 'Activo'),
(5, 'Ramiro', 'Lupercio', 'Coronel', 'ramiro@gmail.com', 'Pw123', 'Maestro', 'Activo'),
(6, 'Edgar Faustino', 'Zepeda', 'Urzúa', 'edgar@gmail.com', 'Pw123', 'Alumno', 'Activo'),
(7, 'Jovita', 'Pérez', 'Solís', 'jovita@gmail.com', 'Jovis123$', 'Maestro', 'Activo'),
(8, 'Fernanda', 'Solórzano', 'Maldonado', 'fer@gmail.com', 'Fer123$$', 'Maestro', 'Activo'),
(9, 'Anahí', 'Jiménez', 'Gómez', 'anahi@gmail.com', 'Nahi123$$', 'Alumno', 'Activo'),
(10, 'José Humberto', 'Peña', 'Peraza', 'jose@gmail.com', 'Jose123$', 'Alumno', 'Activo');

--
-- Disparadores `usuarios`
--
DELIMITER $$
CREATE TRIGGER `validate_email` BEFORE INSERT ON `usuarios` FOR EACH ROW BEGIN
    IF NEW.correo NOT REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid email format';
    END IF;
END
$$
DELIMITER ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id_alumno`),
  ADD UNIQUE KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `aula`
--
ALTER TABLE `aula`
  ADD PRIMARY KEY (`id_aula`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`id_carrera`);

--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`id_grupos`);

--
-- Indices de la tabla `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`id_maestro`),
  ADD UNIQUE KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id_materia`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id_alumno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `aula`
--
ALTER TABLE `aula`
  MODIFY `id_aula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `id_carrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `grupos`
--
ALTER TABLE `grupos`
  MODIFY `id_grupos` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `maestros`
--
ALTER TABLE `maestros`
  MODIFY `id_maestro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `id_materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
