import psycopg2
from config import CONFIG

def listar_apostas():
    conexao = psycopg2.connect(**CONFIG)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM apostas ORDER BY nome DESC")

    apostas = cursor.fetchall()
    for aposta in apostas:
        print(aposta)

    cursor.close()
    conexao.close()
