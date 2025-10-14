import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "aluno",
    database = "yoriih"
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM yoriih.loja")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

cursor.close()
conexao.close()

