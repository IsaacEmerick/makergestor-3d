import dados
from dados import dados_sistema

from rich.panel import Panel
from rich.console import Console
console = Console()

def cadastro_filamento():
  console.print(Panel.fit("🧵  [bold #7A4332]Cadastrar Filamento[/]", border_style="#B2AABA"))
  try:
    nome = input("Nome/Cor do Filamento (ex: PLA Preto): ")
    peso_inicial = float(input("Peso total do carretel (em gramas): "))
    if peso_inicial <= 0:
      console.print("\n[red]❌ Erro: O peso inicial deve ser maior que zero.[/]")
      return
    valor_kg = float(input("Valor pago no KG (R$): "))
    valor_grama = valor_kg / peso_inicial

    dados_sistema["filamentos"].append({
      "nome": nome,
      "valor_kg": valor_kg,
      "valor_grama": valor_grama,
      "peso_inicial": peso_inicial,
      "peso_atual": peso_inicial
    })

    dados.salvar_dados()
    console.print(f"[green4]✅ Filamento {nome} cadastrado! Custo: R${valor_grama:.2f}/g[/]")
  except ValueError:
    console.print("\n[red]❌ Erro: Por favor, digite um valor numérico válido.[/]")

def listar_filamentos():
  if not dados_sistema["filamentos"]:
    console.print("[bold orange3]Nenhum filamento cadastrado no sistema.[/]")
    return False
  
  console.print(Panel.fit("🧵  [bold #7A4332]Lista de Filamentos", border_style="#B2AABA"))
  for i, fil in enumerate(dados_sistema["filamentos"], start=1):
    vida_util = (fil["peso_atual"] / fil["peso_inicial"]) * 100
    print(f"{i}. {fil['nome']} - R${fil['valor_kg']:.2f}/kg - Quantidade atual: {fil['peso_atual']}g ({vida_util:.1f}%)")
  return True
