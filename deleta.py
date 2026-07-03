import psycopg2
from config import CONFIG

def excluir_aposta():
	conexao = psycopg2.connect(**CONFIG)
	cursor = conexao.cursor()

	id_str = input("ID da aposta a excluir: ").strip()
	if not id_str:
		print("ID vazio. Operação cancelada.")
		cursor.close()
		conexao.close()
		return

	try:
		id_aposta = int(id_str)
	except ValueError:
		print("ID inválido. Operação cancelada.")
		cursor.close()
		conexao.close()
		return
	
	sql = "DELETE FROM apostas WHERE id = %s"
	cursor.execute(sql, (id_aposta,))
	conexao.commit()

	print(f"{cursor.rowcount} linha(s) removida(s)")
	cursor.close()
	conexao.close()