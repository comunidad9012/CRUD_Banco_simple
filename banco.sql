-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2022 a las 20:58:58
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `parcia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `dni` int(10) NOT NULL,
  `nombre_cliente` varchar(40) DEFAULT NULL,
  `pin` int(4) NOT NULL,
  `fecha_nacimiento` varchar(27) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL,
  `localidad` varchar(20) NOT NULL,
  `telefono` varchar(23) DEFAULT NULL,
  `email` varchar(23) DEFAULT NULL,
  `fecha_alta` datetime DEFAULT NULL,
  `grupo_clientes` varchar(1) DEFAULT NULL,
  `fondos` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`dni`, `nombre_cliente`, `pin`, `fecha_nacimiento`, `direccion`, `localidad`, `telefono`, `email`, `fecha_alta`, `grupo_clientes`, `fondos`) VALUES
(4234534, 'Pedro', 4567, '21021998', 'micasa', 'San Rafael', '5648980984', 'pedro@gmail.com', '2022-11-18 13:37:38', '3', 0),
(44058077, 'Carlos', 1234, '22072002', 'sucasa', 'San rafael', '343343', 'carlos@gmail.com', '2022-11-11 14:40:02', '4', 500);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`dni`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
