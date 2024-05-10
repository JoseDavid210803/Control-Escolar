-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2024 at 02:03 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `control`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumnos`
--

CREATE TABLE `alumnos` (
  `id_alumno` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `nombre_carrera` varchar(25) NOT NULL,
  `grupo` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alumnos`
--

INSERT INTO `alumnos` (`id_alumno`, `id_usuario`, `fecha_nacimiento`, `nombre_carrera`, `grupo`) VALUES
(1, 2, '2010-05-24', 'Ingeniería en Computación', '1A');

-- --------------------------------------------------------

--
-- Table structure for table `aula`
--

CREATE TABLE `aula` (
  `id_aula` int(11) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  `edificio` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aula`
--

INSERT INTO `aula` (`id_aula`, `nombre`, `edificio`) VALUES
(1, 'LC01', 'DUCT1'),
(2, 'LC05', 'DUCT2');

-- --------------------------------------------------------

--
-- Table structure for table `carrera`
--

CREATE TABLE `carrera` (
  `id_carrera` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `semestre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `carrera`
--

INSERT INTO `carrera` (`id_carrera`, `nombre`, `semestre`) VALUES
(1, 'Ingeniería en Computación', '9'),
(2, 'Ingeniería Informática', '9');

-- --------------------------------------------------------

--
-- Table structure for table `grupos`
--

CREATE TABLE `grupos` (
  `id_grupos` int(20) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `id_alumnos` int(11) NOT NULL,
  `nombre_grupo` varchar(25) DEFAULT NULL,
  `salon` varchar(5) NOT NULL,
  `semestre` varchar(20) NOT NULL,
  `max_alumn` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grupos`
--

INSERT INTO `grupos` (`id_grupos`, `id_carrera`, `id_materia`, `id_alumnos`, `nombre_grupo`, `salon`, `semestre`, `max_alumn`) VALUES
(1, 1, 1, 1, '1A', '16', '6', 20);

-- --------------------------------------------------------

--
-- Table structure for table `horarios`
--

CREATE TABLE `horarios` (
  `id_horarios` int(11) NOT NULL,
  `turno` set('Matutino','Vespertino') NOT NULL,
  `hora` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `maestros`
--

CREATE TABLE `maestros` (
  `id_maestro` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_materias` int(11) NOT NULL,
  `grado_estudios` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `maestros`
--

INSERT INTO `maestros` (`id_maestro`, `id_usuario`, `id_materias`, `grado_estudios`) VALUES
(1, 3, 0, 'Preparatoria');

-- --------------------------------------------------------

--
-- Table structure for table `materias`
--

CREATE TABLE `materias` (
  `id_materia` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `horario_entrada` time NOT NULL,
  `horario_salida` time NOT NULL,
  `maestro` varchar(255) NOT NULL,
  `aula` varchar(255) NOT NULL,
  `creditos` int(11) NOT NULL,
  `semestre` varchar(15) NOT NULL,
  `carrera` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `materias`
--

INSERT INTO `materias` (`id_materia`, `nombre`, `horario_entrada`, `horario_salida`, `maestro`, `aula`, `creditos`, `semestre`, `carrera`) VALUES
(1, 'Programación Orientada a Objetos', '09:00:00', '10:50:00', 'Maestro García Gómez', 'LC05', 8, '3', 'Ingeniería Informática'),
(4, 'Ingeniería de Software', '11:00:00', '12:50:00', 'Maestro García Gómez', 'LC01', 8, '6', 'Ingeniería en Computación');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `a_paterno` varchar(15) NOT NULL,
  `a_materno` varchar(15) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contrasena` varchar(15) NOT NULL,
  `perfil` set('Alumno','Maestro','Administrador','') NOT NULL,
  `status` set('Activo','Inactivo') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `a_paterno`, `a_materno`, `correo`, `contrasena`, `perfil`, `status`) VALUES
(1, 'Ejemplo', 'Gómez', 'Rodríguez', 'ejemplo@gmail.com', 'Pw123', 'Administrador', 'Activo'),
(2, 'Alumno', 'Jiménez', 'Robles', 'alumno@gmail.com', 'Pw123', 'Alumno', 'Activo'),
(3, 'Maestro', 'García', 'Gómez', 'maestro@gmail.com', 'Pw123', 'Maestro', 'Activo'),
(4, 'Sofia', 'Herrera', 'Coss', 'sofia@gmail.com', 'Andy2808', 'Administrador', '');

--
-- Triggers `usuarios`
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
-- Indexes for dumped tables
--

--
-- Indexes for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id_alumno`),
  ADD UNIQUE KEY `id_carrera` (`nombre_carrera`),
  ADD UNIQUE KEY `id_usuario` (`id_usuario`),
  ADD UNIQUE KEY `grupo` (`grupo`);

--
-- Indexes for table `aula`
--
ALTER TABLE `aula`
  ADD PRIMARY KEY (`id_aula`);

--
-- Indexes for table `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`id_carrera`);

--
-- Indexes for table `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`id_grupos`),
  ADD UNIQUE KEY `id_grupos` (`id_grupos`),
  ADD UNIQUE KEY `id_carrera` (`id_carrera`),
  ADD UNIQUE KEY `id_materia` (`id_materia`),
  ADD UNIQUE KEY `id_alumnos` (`id_alumnos`),
  ADD UNIQUE KEY `nombre_grupo` (`nombre_grupo`);

--
-- Indexes for table `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`id_horarios`);

--
-- Indexes for table `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`id_maestro`),
  ADD UNIQUE KEY `id_usuario` (`id_usuario`),
  ADD UNIQUE KEY `id_materias` (`id_materias`);

--
-- Indexes for table `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id_materia`),
  ADD UNIQUE KEY `id_horario` (`horario_entrada`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id_alumno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `aula`
--
ALTER TABLE `aula`
  MODIFY `id_aula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `carrera`
--
ALTER TABLE `carrera`
  MODIFY `id_carrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `grupos`
--
ALTER TABLE `grupos`
  MODIFY `id_grupos` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `materias`
--
ALTER TABLE `materias`
  MODIFY `id_materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD CONSTRAINT `alumnos_ibfk_1` FOREIGN KEY (`grupo`) REFERENCES `grupos` (`nombre_grupo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
