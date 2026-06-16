import psycopg2
from psycopg2.extras import RealDictCursor
from config import CONFIG

conexao = psycopg2.connect(**CONFIG)
print("Conectado!")
cursor = conexao.cursor(cursor_factory=RealDictCursor)

sql = """
INSERT INTO apostas (nome, selecao, valor)
VALUES (%s, %s, %s)
"""
aposta1 = ("David", "Brasil", 100.00)
aposta2 = ("Henrique", "Argentina", 200.00)
cursor.execute(sql, aposta1)
cursor.execute(sql, aposta2)
conexao.commit()
print("Apostas inseridas com sucesso!")