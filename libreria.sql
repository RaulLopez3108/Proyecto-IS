CREATE DATABASE IF NOT EXISTS libreria;
USE libreria;

DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS libros;

CREATE TABLE usuarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    USUARIO VARCHAR(50) NOT NULL UNIQUE,
    CORREO VARCHAR(255) NOT NULL UNIQUE,
    CONTRASENA VARCHAR(255) NOT NULL,
    ROL ENUM('admin', 'usuario') NOT NULL DEFAULT 'usuario'
);

CREATE TABLE libros (
    NOMBRE VARCHAR(50) NOT NULL,
    AUTOR VARCHAR(50) NOT NULL,
    PUBLICACION DATE NOT NULL,
    GENERO VARCHAR(255) NOT NULL,
    SINOPSIS TEXT(355) NOT NULL,
    PORTADA VARCHAR(255)  -- Guardar nombre de imagen en la portada "HarryPotter.jpg"
);

DROP USER IF EXISTS 'admin'@'localhost';
DROP USER IF EXISTS 'lector'@'localhost';

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'Admin1234!';
GRANT ALL PRIVILEGES ON libreria.* TO 'admin'@'localhost';


CREATE USER IF NOT EXISTS 'lector'@'localhost' IDENTIFIED BY 'Lector1234!';
GRANT SELECT ON libreria.libros TO 'lector'@'localhost';
GRANT SELECT ON libreria.usuarios TO 'lector'@'localhost';

FLUSH PRIVILEGES;

INSERT INTO usuarios (USUARIO, CORREO, CONTRASENA, ROL) 
VALUES ('admin', 'admin@gmail.com', '$2b$12$YcCpCQyLVhHxsugvToppjuPApAqkrIXcIQb.pQAvW36sArfd2YyRy', 'admin')
ON DUPLICATE KEY UPDATE USUARIO=USUARIO;

