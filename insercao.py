import psycopg2
from config import CONFIG

def inserir_apostas():
    conexao = psycopg2.connect(**CONFIG)
    cursor = conexao.cursor()

    sql = """
    INSERT INTO apostas (nome, selecao, valor)
    VALUES (%s, %s, %s)
    """

    nome = input("Nome: ").strip().lower()
    selecao = input("Seleção: ").strip().lower()

    while True:
        valor_str = input("Valor (mínimo R$10 use ponto para decimal): ").strip()
        try:
            valor = float(valor_str)
            if valor < 10:
                print("O valor deve ser pelo menos R$10. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número como 100.00")

    cursor.execute(sql, (nome, selecao, valor))

    conexao.commit()
    print("Aposta inserida com sucesso.")

    cursor.close()
    conexao.close()