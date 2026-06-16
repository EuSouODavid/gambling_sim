import psycopg2
from config import CONFIG

conexao = psycopg2.connect(**CONFIG)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM apostas")

apostas = cursor.fetchall()
for aposta in apostas:
    print(aposta)

# exemplo de consulta com filtro:
# sql = "SELECT * FROM apostas WHERE id = %s"
# cursor.execute(sql, (1,))
# aposta = cursor.fetchone()
# print(aposta)
