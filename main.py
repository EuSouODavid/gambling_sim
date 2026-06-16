from rich.console import Console
from rich.panel import Panel
import os

from insercao import inserir_apostas
from lista import listar_apostas
from atualiza import atualizar_aposta
from deleta import excluir_aposta

console = Console()

menu = ("""
1. Incluir Aposta
2. Listar Apostas(por nome)
3. Alterar Aposta
4. Excluir Aposta
0. Finalizar
""")

while True:
    os.system("cls")
    console.print(Panel.fit(menu, title="Menu Principal"))

    opcao = int(input("Opção: "))

    if opcao == 1:
        inserir_apostas()
        print("Apostas inseridas com sucesso!")
    elif opcao == 2:
       listar_apostas()
    elif opcao == 3:
        atualizar_aposta()
    elif opcao == 4:
        excluir_aposta()
    elif opcao == 0:
        console.print("[bold cyan]Fim do Programa[/bold cyan]")
        break
    else:
        console.print("[bold red]Opção inválida[/bold red]")

    input("\nPressione Enter para continuar...")