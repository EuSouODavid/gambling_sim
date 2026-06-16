import psycopg2
from config import CONFIG

def inserir_apostas():
    conexao = psycopg2.connect(**CONFIG)
    cursor = conexao.cursor()

    sql = """
    INSERT INTO apostas (nome, selecao, valor)
    VALUES (%s, %s, %s)
    """
    aposta1 = ("David", "Brasil", 100.00)
    aposta2 = ("Henrique", "Argentina", 200.00)

    cursor.execute(sql, aposta1)
    cursor.execute(sql, aposta2)
    conexao.commit()

    cursor.close()
    conexao.close()