import psycopg2
from config import CONFIG

conexao = psycopg2.connect(**CONFIG)
cursor = conexao.cursor()

sql = """
UPDATE apostas
SET valor = %s
WHERE nome = %s
"""
cursor.execute(sql, (150.00, "David"))
conexao.commit()
print(cursor.rowcount, "linha(s) atualizada(s)")