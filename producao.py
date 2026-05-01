from dados import dados_sistema
import dados
import filamentos

from rich.panel import Panel
from rich.console import Console
console = Console()

def configurar_energia():
  print(Panel.fit("⚡  [bold #7A4332]Alterar Tarifa de Energia (kWh) ---", border_style="#B2AABA"))
  print(f"Tarifa atual: {dados_sistema['tarifa_kwh']:.2f}")
  try:
    valor = float(input("Digite o valor da Tarifa de Energia (R$/kWh): "))
    dados_sistema["tarifa_kwh"] = valor

    dados.salvar_dados()
    print(f"✅ Tarifa de Energia alterada para R${valor:.2f}/kWh com sucesso!")
  except ValueError:
    print("\n❌ Erro: Por favor, digite um valor numérico válido.")

def registrar_orcamento():
  console.print(Panel.fit("💰  [bold #7A4332]Registrar Novo Orçamento[/]", border_style="#B2AABA"))
  if dados_sistema["tarifa_kwh"] == 0.0:
    console.print("\n[bold orange3]⚠️  Aviso: Você precisa configurar a Tarifa de Energia primeiro (Opção 3)[/]")
    return
        
  if not dados_sistema["filamentos"]:
    console.print("\n[bold orange3]⚠️  Aviso: Você precisa cadastrar pelo menos um filamento primeiro (Opção 1)[/]")
    return
  
  try:
    cliente = input("Nome do cliente: ")
    peca = input("Nome da peça: ")
    peso_peca = float(input("Digite o peso da peça (em gramas): "))
    tempo_horas = float(input("Tempo estimado da impressão (em horas): "))
    materiais_usados = []

    # Selecionar filamento
    multi_cor = input("\nSua impressão utiliza mais de um filamento? (s/n): ")
    if multi_cor.lower() == 's':
      console.print("[bold green]Iniciando mix de filamentos...[/]")
      peso_restante = peso_peca
      custo_filamento = 0.0
      custo_total_material = 0.0

      while True:
        if peso_restante <= 0:
          console.print("\n[orange3] ⚠️  Peça pronta![/]")
          break

        filamentos.listar_filamentos()
        id_filamento = int(input("Escolha o ID dos filamentos que serão utilizados: (Um por vez | 0 para finalizar): "))

        if id_filamento > len(dados_sistema["filamentos"]):
          console.print("\n[red]❌ Erro: O ID do filamento escolhido não existe.[/]")
          continue

        if id_filamento < 1:
          break

        filamento_escolhido = dados_sistema["filamentos"][id_filamento - 1]
        peso_usado = float(input(f"Quantas gramas de {filamento_escolhido['nome']} a peça usa? Faltam {peso_restante:.2f}g para finalizar o mix."))

        if peso_usado > filamento_escolhido["peso_atual"]:
          console.print(f"[bold orange3] ⚠️  Alerta: Você não tem {peso_usado:.2f}g no carretel! Tem apenas {filamento_escolhido['peso_atual']:.2f}g[/]")
          console.print(f"[orange3] Compre mais filamento {filamento_escolhido['nome']}! E cadastre no sistema![/]")
          continue

        custo_parcial = peso_usado * filamento_escolhido["valor_grama"]
        custo_total_material += custo_parcial
        peso_restante -= peso_usado

        materiais_usados.append({
          "id_filamento": id_filamento,
          "nome": filamento_escolhido["nome"],
          "peso_usado": peso_usado,
          "custo": custo_parcial
        })

        custo_filamento = custo_total_material

        console.print(f"[green4]{peso_usado:.2f}g de {filamento_escolhido['nome']} adicionado!")

    else:
      while True:
        filamentos.listar_filamentos()
        id_filamento = int(input("Escolha o ID do filamento que será utilizado: "))

        if id_filamento < 1 or id_filamento > len(dados_sistema["filamentos"]):
          print("\n❌ Erro: O ID do filamento escolhido não existe. Tente novamente.")
          continue

        filamento_escolhido = dados_sistema["filamentos"][id_filamento - 1]
        custo_filamento = peso_peca * filamento_escolhido["valor_grama"]
        materiais_usados.append({
          "id_filamento": id_filamento,
          "nome": filamento_escolhido["nome"],
          "peso_usado": peso_peca,
          "custo": custo_filamento
        })
        break

    # Consumo média de uma impressora 3D pelas pesquisas realizadas é de 150W ou 0,15kW
    consumo_kw = 0.15
    custo_energia = tempo_horas * consumo_kw * dados_sistema["tarifa_kwh"]

    custo_total = custo_filamento + custo_energia
    margem_lucro = custo_total * 2 # 200% em cima do valor de custo
    preco_final = custo_total + margem_lucro

    console.print(Panel.fit("[bold #7A4332]📊 Resumo do Orçamento[/]", border_style="#B2AABA"))
    console.print(f"🧵 Custo do Material: [green]R${custo_filamento:.2f}[/]")
    console.print(f"⚡ Custo da Energia: [yellow]R${custo_energia:.2f}[/]")
    console.print(f"📉 Custo Total: [bold orange4]R${custo_total:.2f}[/]")
    console.print(f"💰 [bold green4]Preço Sugerido: R${preco_final:.2f}[/]")

    salvar = input("\nDeseja aprovar e enviar para a fila de produção? (s/n): ")
    if salvar.lower() == "s":
      dados_sistema["fila_pedidos"].append({
        "id": dados.contador_pedidos,
        "cliente": cliente,
        "peca": peca,
        "preco_final": preco_final,
        "status": "Na Fila",
        "materiais": materiais_usados,
        "descontado": False
      })
      print(f"✅ Pedido #{dados.contador_pedidos} enviado para a fila de produção!")
      dados.contador_pedidos += 1
      dados.salvar_dados()
    else:
      print("❌ Pedido não enviado para a fila de produção.")
  except ValueError:
    print("\n❌ Erro: Entrada inválida. Por favor, verifique se o tipo de dado está correto.")

def visualizar_fila_producao():
  console.print(Panel.fit("📋  [bold #7A4332]Fila de Produção Atual", border_style="#B2AABA"))
  if not dados_sistema["fila_pedidos"]:
    console.print("[orange3]⚠️  A fila está vazia.")
    return
  
  for pedido in dados_sistema["fila_pedidos"]:
    print(f"  [ID: {pedido['id']}] Cliente: {pedido['cliente']} | Peça: {pedido['peca']} | Status: {pedido.get('status', 'Na Fila')} | Valor: R${pedido['preco_final']:.2f}")

def cancelar_pedido():
  print("\n--- Cancelar Pedido ---")
  visualizar_fila_producao()
  try:
    id_pedido = int(input("Digite o ID do pedido que deseja cancelar: "))
    if id_pedido < 1 or id_pedido > len(dados_sistema["fila_pedidos"]):
      print("\n❌ Erro: O ID do pedido escolhido não existe. Cancelamento cancelado.")
      return
    
    pedido_cancelado = dados_sistema["fila_pedidos"].pop(id_pedido - 1)
    print(f"✅ Pedido #{pedido_cancelado['id']} cancelado com sucesso!")
    dados.salvar_dados()
  except ValueError:
    print("\n❌ Erro: Entrada inválida. Por favor, verifique se o tipo de dado está correto.")

def atualizar_status():
  console.print(Panel.fit("🗒️  [bold #7A4332]Atualizar Status do Pedido", border_style="#B2AABA"))
  if not dados_sistema["fila_pedidos"]:
    console.print("[orange3]⚠️  A fila está vazia.")
    return

  try:
    visualizar_fila_producao()
    id_pedido = int(input("\nDigite o ID do pedido que deseja atualizar o status: "))
    
    pedido_encontrado = None
    for pedido in dados_sistema["fila_pedidos"]:
      if pedido["id"] == id_pedido:
        pedido_encontrado = pedido
        break

    if not pedido_encontrado:
      print(f"\n❌ Pedido #{id_pedido} não encontrado.")
      return
    
    print(f"\nStatus atual: {pedido_encontrado.get('status', 'Na Fila')}")
    print("1. Na Fila")
    print("2. Imprimindo")
    print("3. Finalizado")
    novo_status_opcao = input("Escolha o novo status (1-3): ")

    if novo_status_opcao == '1':
      pedido_encontrado["status"] = "Na Fila"
    elif novo_status_opcao == '2':
      pedido_encontrado["status"] = "Imprimindo"
    elif novo_status_opcao == '3':
      pedido_encontrado["status"] = "Finalizado"

      if not pedido_encontrado.get("descontado", False):
        console.print("\n[bold yellow]📦 Baixando materiais do estoque...[/]")

        for material in pedido_encontrado.get("materiais", []):
          id_filamento = material["id_filamento"]
          peso_gasto = material["peso_usado"]

          filamento = dados_sistema["filamentos"][id_filamento - 1]
          filamento["peso_atual"] -= peso_gasto
          vida_util = (filamento["peso_atual"] / filamento["peso_inicial"]) * 100

          if filamento["peso_atual"] < 0:
            console.print(f"[bold red]⚠️  Atenção: O estoque de {filamento['nome']} ficou negativo ({filamento['peso_atual']:.2f}g)![/]")
          console.print(f"[-] {peso_gasto:.2f}g de {filamento['nome']}. Resta: {filamento['peso_atual']:.2f}g ({vida_util:.1f}%)")

        pedido_encontrado["descontado"] = True
    else:
      print("❌ Opção inválida.")
      return
    
    dados.salvar_dados()
    print(f"✅ Status do pedido #{id_pedido} atualizado para {pedido_encontrado['status']}!")

  except ValueError:
    print("\n❌ Erro: O ID deve ser um número inteiro.")
