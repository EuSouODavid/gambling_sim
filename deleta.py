import psycopg2
from config import CONFIG

def excluir_aposta(nome_aposta="David"):
	conexao = psycopg2.connect(**CONFIG)
	cursor = conexao.cursor()

	sql = "DELETE FROM apostas WHERE nome = %s"
	cursor.execute(sql, (nome_aposta,))
	conexao.commit()

	print(cursor.rowcount, "linha(s) removida(s)")
	cursor.close()
	conexao.close()