from dados import dados_sistema
import dados
import filamentos

def configurar_energia():
  print("\n--- Alterar Tarifa de Energia (kWh) ---")
  print(f"Tarifa atual: {dados_sistema["tarifa_kwh"]:.2f}")
  try:
    valor = float(input("Digite o valor da Tarifa de Energia (R$/kWh): "))
    dados_sistema["tarifa_kwh"] = valor

    dados.salvar_dados()
    print(f"✅ Tarifa de Energia alterada para R${valor:.2f}/kWh com sucesso!")
  except ValueError:
    print("\n❌ Erro: Por favor, digite um valor numérico válido.")

def registrar_orcamento():
  print("\n--- Registrar Novo Orçamento ---")
  if dados_sistema["tarifa_kwh"] == 0.0:
    print("\n⚠️  Aviso: Você precisa configurar a Tarifa de Energia primeiro (Opção 3)")
    return
        
  if not dados_sistema["filamentos"]:
    print("\n⚠️  Aviso: Você precisa cadastrar pelo menos um filamento primeiro (Opção 1)")
    return
  
  try:
    cliente = input("Nome do cliente: ")
    peca = input("Nome da peça: ")
    peso_peca = float(input("Digite o peso da peça (em gramas): "))
    tempo_horas = float(input("Tempo estimado da impressão (em horas): "))

    # Selecionar filamento
    filamentos.listar_filamentos()
    id_filamento = int(input("Escolha o ID do filamento que será utilizado: "))

    if id_filamento < 1 or id_filamento > len(dados_sistema["filamentos"]):
      print("\n❌ Erro: O ID do filamento escolhido não existe. Orçamento cancelado.")
      return

    filamentos_escolhido = dados_sistema["filamentos"][id_filamento - 1]
    custo_filamento = peso_peca * filamentos_escolhido["valor_grama"]

    # Consumo média de uma impressora 3D pelas pesquisas realizadas é de 150W ou 0,15kW
    consumo_kw = 0.15
    custo_energia = tempo_horas * consumo_kw * dados_sistema["tarifa_kwh"]

    custo_total = custo_filamento + custo_energia
    margem_lucro = custo_total * 2 # 200% em cima do valor de custo
    preco_final = custo_total + margem_lucro

    print("\n📊 --- Resumo do Orçamento ---")
    print(f"Custo do Material: R${custo_filamento:.2f}")
    print(f"Custo da Energia: R${custo_energia:.2f}")
    print(f"Custo Total: R${custo_total:.2f}")
    print(f"💰 Preço Sugerido: R${preco_final:.2f}")

    salvar = input("\nDeseja aprovar e enviar para a fila de produção? (s/n): ")
    if salvar.lower() == "s":
      dados_sistema["fila_pedidos"].append({
        "id": dados.contador_pedidos,
        "cliente": cliente,
        "peca": peca,
        "preco_final": preco_final,
        "status": "Na Fila"
      })
      print(f"✅ Pedido #{dados.contador_pedidos} enviado para a fila de produção!")
      dados.contador_pedidos += 1
      dados.salvar_dados()
    else:
      print("❌ Pedido não enviado para a fila de produção.")
  except ValueError:
    print("\n❌ Erro: Entrada inválida. Por favor, verifique se o tipo de dado está correto.")

def visualizar_fila_producao():
  print("\n📋 --- Fila de Produção Atual ---")
  if not dados_sistema["fila_pedidos"]:
    print("A fila está vazia no momento.")
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
  print("\n 🗒️ --- Atualizar Status do Pedido ---")
  if not dados_sistema["fila_pedidos"]:
    print("⚠️  A fila está vazia.")
    return

  try:
    visualizar_fila_producao()
    id_pedido = int(input("\nDigite o ID do pedido que deseja atualizar o status: "))
    
    pedido_encontrado = None
    for pedido in dados_sistema["fila_pedidos"]:
      if pedido["id"] == id_pedido:
        pedido_encontrado = pedido
      
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
      else:
          print("❌ Opção inválida.")
          return
      
      dados.salvar_dados()
      print(f"✅ Status do pedido #{id_pedido} atualizado para {pedido_encontrado['status']}!")

  except ValueError:
    print("\n❌ Erro: O ID deve ser um número inteiro.")
