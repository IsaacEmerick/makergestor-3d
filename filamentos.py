from dados import dados_sistema

def cadastro_filamento():
  print("\n--- Cadastrar Filamento ---")
  try:
    nome = input("Nome/Cor do Filamento (ex: PLA Preto): ")
    valor_kg = float(input("Valor pago no KG (R$): "))

    valor_grama = valor_kg / 1000
    dados_sistema["filamentos"].append({
      "nome": nome,
      "valor_kg": valor_kg,
      "valor_grama": valor_grama
    })

    print(f"✅ Filamento {nome} cadastrado! Custo: R${valor_grama:.2f}/g")
  except ValueError:
    print("\n❌ Erro: Por favor, digite um valor numérico válido.")

def listar_filamentos():
  if not dados_sistema["filamentos"]:
    print("Nenhum filamento cadastrado no sistema.")
    return False
  
  print("\n--- Lista de Filamentos ---")
  for i, fil in enumerate(dados_sistema["filamentos"], start=1):
    print(f"{i}. {fil['nome']} - R${fil['valor_kg']:.2f}/kg")
  return True
