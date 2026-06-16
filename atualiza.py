import psycopg2
from config import CONFIG

def atualizar_aposta(valor=150.00, nome="David"):
	conexao = psycopg2.connect(**CONFIG)
	cursor = conexao.cursor()

	sql = """
	UPDATE apostas
	SET valor = %s
	WHERE nome = %s
	"""
	cursor.execute(sql, (valor, nome))
	conexao.commit()
	print(cursor.rowcount, "linha(s) atualizada(s)")

	cursor.close()
	conexao.close()