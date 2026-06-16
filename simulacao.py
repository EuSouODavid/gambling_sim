import psycopg2
from config import CONFIG

def simular_apostas():
    conexao = psycopg2.connect(**CONFIG)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM apostas")
    apostas = cursor.fetchall()

    vencedor = input("Nome da seleção campeã: ").strip()

    premio_total = sum(float(a[3]) for a in apostas)

    vencedores = [a for a in apostas if str(a[2]).lower() == vencedor.lower()]

    if not vencedores:
        print("Nenhum vencedor para essa seleção.")
    else:
        total_vencedores = sum(float(a[3]) for a in vencedores)
        for _id, nome, selecao, valor in vencedores:
            parcela = (float(valor) / total_vencedores) * premio_total if total_vencedores else 0
            print(f"{nome}: apostou R${float(valor):.2f} -> receberá R${parcela:.2f}")

    cursor.close()
    conexao.close()

