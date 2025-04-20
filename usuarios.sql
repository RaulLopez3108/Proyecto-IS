CREATE TABLE usuarios(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    USUARIO VARCHAR(20) NOT NULL,
    CONTRASEÑA VARCHAR(50) NOT NULL   
);

INSERT INTO usuarios (USUARIO,CONTRASEÑA)
VALUES 
('Raul','contraseña'),
('Gabriela','abc123'),
('Gael','123abc'),
('JesusFlores','def'),
('JesusAlberto','fed');

select * from usuarios;


    