import os

# Estrutura de dados(simulando o banco de dados)
dados_sistema = {
  "tarifa_kwh" : 0.0,
  "filamentos" : [],
  "fila_pedidos" : []
}

def exibir_menu():
  print("\n" + "="*40)
  print(" 🛠️  MAKER GESTOR 3D - CLI")
  print("="*40)
  print("1. Cadastrar Filamento")
  print("2. Alterar Tarifa de Energia (kWh)")
  print("3. Registrar Novo Orçamento")
  print("4. Visualizar Fila de Produção")
  print("0. Sair")
  print("="*40)
  
def configurar_energia():
  print("\n--- Alterar Tarifa de Energia (kWh)")
  print(f"Tarifa atual: {dados_sistema["tarifa_kwh"]}")
  try:
    valor = float(input("Digite o valor da Tarifa de Energia (R$/kWh): "))
    dados_sistema["tarifa_kwh"] = valor
    print(f"✅ Tarifa de Energia alterada para R${valor:.2f}/kWh com sucesso!")
  except ValueError:
    print("\n❌ Erro: Por favor, digite um valor numérico válido.")

def registrar_orcamento():
  print("\n--- Registrar Novo Orçamento")
  if dados_sistema["tarifa_kwh"] == 0.0:
    print("\n ⚠️  Aviso: Você precisa configurar a Tarifa de Energia primeiro (Opção 2)")
    return
  
  try:
    # Pergunta ao usário as informações da peça que será feito orçamento
    peso_peca = float(input("Digite o peso da peça (em gramas): "))
    tempo_horas = float(input("Tempo estimado da impressão (em horas): "))

    # TODO: adicionar busca pela lista de filamentos, temporáriamente o valor será de R$ 90,00/kg (R$0,09g)
    custo_filamento = peso_peca * 0.09

    # Consumo média de uma impressora 3D pelas pesquisas realizas é de 150W ou 0,15kW
    consumo_kw = 0.15
    custo_energia = tempo_horas * consumo_kw * dados_sistema["tarifa_kwh"]

    custo_total = custo_filamento + custo_energia
    margem_lucro = custo_total * 2 # 200% em cima do valor de custo
    preco_final = custo_total + margem_lucro

    print("\n📊 --- Resumo do Orçamento ---")
    print(f"Custo do Material: R${custo_filamento:.2f}")
    print(f"Custo da Energia: R${custo_energia:.2f}")
    print(f"Custo Total: R${custo_total:.2f}")
    print(f"💰 Preço Sugerido (com lucro): R${preco_final:.2f}")

  except ValueError:
    print("\n❌ Erro: Por favor, certifiquece de usar apenas números para os valores de peso e tempo.")

def main():
  while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print("\n[🚧 Módulo em desenvolvimento]")
    elif opcao == "2":
      configurar_energia()
    elif opcao == "3":
      registrar_orcamento()
    elif opcao == "4":
      print("\n[🚧 Módulo em desenvolvimento]")
    elif opcao == "0":
      print("\n Encerrando o MakerGestor 3D. Até logo!...")
      break
    else:
      print("\n❌ Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
  main()
