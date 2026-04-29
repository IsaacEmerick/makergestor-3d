import filamentos
import producao

def exibir_menu():
  print("\n" + "="*40)
  print(" 🛠️  MAKER GESTOR 3D - CLI")
  print("="*40)
  print("1. Cadastrar Filamento")
  print("2. Listar Filamentos")
  print("3. Alterar Tarifa de Energia (kWh)")
  print("4. Registrar Novo Orçamento")
  print("5. Visualizar Fila de Produção")
  print("0. Sair")
  print("="*40)
  
def main():
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
    elif opcao == "0":
      print("\n Encerrando o MakerGestor 3D. Até logo!...")
      break
    else:
      print("\n❌ Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
  main()
