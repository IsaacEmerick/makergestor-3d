# MakerGestor 3D

## 📌 Descrição do Problema
Makers e entusiastas da impressão 3D frequentemente transformam seu hobby em uma fonte de renda extra. No entanto, enfrentam grandes dificuldades na hora de precificar suas encomendas. O cálculo manual muitas vezes ignora custos invisíveis, como o consumo contínuo de energia elétrica da impressora e o desgaste do material, resultando em peças vendidas com prejuízo. Além disso, à medida que o volume de pedidos cresce, o controle da fila de produção se torna caótico e desorganizado.

## 🚀 Solução Proposta
Sistema via interface de linha de comando (CLI) projetado para automatizar a precificação e organizar o fluxo de trabalho de pequenas operações de impressão 3D. A solução permite cadastrar os custos base (filamento e energia) e calcula de forma instantânea o custo real de produção, aplicando uma margem de lucro. Além do módulo financeiro, o sistema converte os orçamentos em pedidos reais e os organiza em uma fila de produção.

## 🛠️ Tecnologias Utilizadas
- Python 3.11
- Biblioteca nativa `json` para persistência de dados
- Arquitetura modularizada

## ⚙️ Como Executar
Pré-requisito: Ter o Python instalado na máquina.
Execute o comando abaixo na raiz do projeto:
```bash
$ python main.py
```
## 📂 Estrutura do Projeto
```
makergestor-3d/
├── main.py
├── dados.py
├── filamentos.py
├── producao.py
├── maker_dados.json (gerado automaticamente)
└── README.md
```

## 🧩 Funcionalidades Implementadas
- Cadastrar filamento (UC01 / RF01)
- Configurar tarifa de energia elétrica (UC02 / RF02)
- Registrar novo orçamento e converter em pedido (UC03 e UC04 / RF03, RF04 e RF05)
- Visualizar fila de produção (UC05 / RF07)
- Cancelar pedido da fila (UC07 / RF08)
- Persistência automática de dados em JSON (RNF04)

## 📸 Demonstração (prints / GIFs / link para vídeo)
![Demonstração MakerGestor 3D](makergestor.gif)

## 👨‍💻 Integrantes do Grupo
- Isaac Vieira Emerick (commits: feat, refactor, docs)

## 🔗 Links (Miro, repositório, vídeo)
- Miro: https://miro.com/app/board/uXjVHaGlv1M=/?share_link_id=775108170292
- GitHub: https://github.com/IsaacEmerick/makergestor-3d