import psycopg2
from psycopg2.extras import RealDictCursor
from config import CONFIG

conexao = psycopg2.connect(**CONFIG)
print("Conectado!")
cursor = conexao.cursor(cursor_factory=RealDictCursor)

sql = "DELETE FROM apostas WHERE id = %s"
cursor.execute(sql, (3,))
conexao.commit()

print(cursor.rowcount, "linha(s) removida(s)")
cursor.close()
conexao.close()