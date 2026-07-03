import psycopg2
from config import CONFIG

def atualizar_aposta():
	id_str = input("ID da aposta a alterar: ").strip()
	if not id_str:
		print("ID vazio. Operação cancelada.")
		return

	try:
		id_aposta = int(id_str)
	except ValueError:
		print("ID inválido. Operação cancelada.")
		return

	while True:
		valor_str = input("Novo valor (mínimo R$10 use ponto para decimal): ").strip()
		try:
			valor = float(valor_str)
			if valor < 10:
				print("O valor deve ser pelo menos R$10. Tente novamente.")
				continue
			break
		except ValueError:
			print("Valor inválido. Digite um número como 100.00")

	conexao = psycopg2.connect(**CONFIG)
	cursor = conexao.cursor()

	sql = """
	UPDATE apostas
	SET valor = %s
	WHERE id = %s
	"""
	cursor.execute(sql, (valor, id_aposta))
	conexao.commit()
	print(f"{cursor.rowcount} linha(s) atualizada(s)")

	cursor.close()
	conexao.close()