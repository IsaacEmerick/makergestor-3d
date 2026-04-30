import json
import os

FILE = 'maker_dados.json'

# Estrutura de dados(simulando o banco de dados)
dados_sistema = {
  "tarifa_kwh" : 0.0,
  "filamentos" : [],
  "fila_pedidos" : []
}

contador_pedidos = 1

def carregar_dados():
  global dados_sistema, contador_pedidos
  if os.path.exists(FILE):
    with open(FILE, 'r', encoding='utf-8') as f:
      dados_carregados = json.load(f)
      dados_sistema.update(dados_carregados)

      if dados_sistema["fila_pedidos"]:
        ultimo_id = max(pedido["id"] for pedido in dados_sistema["fila_pedidos"])
        contador_pedidos = ultimo_id + 1

def salvar_dados():
  with open(FILE, 'w', encoding='utf-8') as f:
    json.dump(dados_sistema, f, indent=4, ensure_ascii=False)
