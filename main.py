import filamentos
import producao
import dados

from rich.panel import Panel
from rich.console import Console
console = Console()

def exibir_menu():
  console.print(Panel.fit("🛠️  [bold #7A4332]MAKER GESTOR 3D - CLI[/]", border_style="#B2AABA"))
  console.print("[1] [green]Cadastrar Filamento[/]")
  console.print("[2] [green]Listar Filamentos[/]")
  console.print("[3] [yellow]Alterar Tarifa de Energia (kWh)[/]")
  console.print("[4] [blue]Registrar Novo Orçamento[/]")
  console.print("[5] [blue]Visualizar Fila de Produção[/]")
  console.print("[6] [blue]Atualizar Status do Pedido[/]")
  console.print("[7] [blue]Cancelar Pedido[/]")
  console.print("[0] [red]Sair[/]")
  console.print("")
  
def main():
  dados.carregar_dados()

  while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      filamentos.cadastro_filamento()
    elif opcao == "2":
      filamentos.listar_filamentos()
    elif opcao == "3":
      producao.configurar_energia()
    elif opcao == "4":
      producao.registrar_orcamento()
    elif opcao == "5":
      producao.visualizar_fila_producao()
    elif opcao == "6":
      producao.atualizar_status()
    elif opcao == "7":
      producao.cancelar_pedido()
    elif opcao == "0":
      console.print("\n[bold #7A4332]Encerrando o MakerGestor 3D. Até logo!...[/]")
      break
    else:
      console.print("\n[bold red]❌ Opção inválida. Por favor, escolha uma opção válida.[/]")

if __name__ == "__main__":
  main()
