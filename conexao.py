import psycopg2
from config import CONFIG

conexao = psycopg2.connect(**CONFIG)
print("Conectado!")
cursor = conexao.cursor()


sql_tabela = """
CREATE TABLE IF NOT EXISTS apostas (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
selecao VARCHAR(50),
valor NUMERIC(7,2) check (valor >= 10)
)"""
cursor.execute(sql_tabela)
conexao.commit()
print("Tabela criada com sucesso!")