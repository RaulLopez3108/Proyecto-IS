import mysql.connector 

def conectar_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "usuarios",
        port = 3307
    ) 

def verificar_usuario(username,password):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT CONTRASEÑA FROM usuarios WHERE USUARIO = %s",(username,))
    resultado = cursor.fetchone()
    if resultado and password == resultado[0]:
        return True
    return False

def agregar_usuario(username,password):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (USUARIO, CONTRASEÑA) VALUES (%s, %s)", (username, password))
    conexion.commit()
    cursor.close()

