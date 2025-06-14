# Sistema de Gestão de Relatórios

O Sistema de Gestão de Relatórios é uma aplicação desktop desenvolvida em Python para geração de relatórios profissionais em formato Excel. O sistema permite criar relatórios financeiros, comerciais e de cobrança com interface intuitiva e design moderno.

## Recursos Principais

- 🚀 Geração de relatórios em Excel (.xlsx)
- 📊 Tipos de relatórios: Financeiro, Comercial e Cobrança
- 📅 Seleção de período com calendário integrado
- 🎨 Interface responsiva e acessível
- 🔍 Histórico de relatórios gerados
- ⚙️ Ajuste de tamanho de fonte

## Tecnologias Utilizadas

- **Python 3.9+**
- **KivyMD** (Interface gráfica moderna)
- **Pandas** (Manipulação de dados para Excel)
- **Openpyxl** (Geração de arquivos Excel)
- **Dateutil** (Manipulação de datas)

## Pré-requisitos

- Python 3.9 ou superior
- Gerenciador de pacotes pip

## Instalação

1. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
pip install kivy kivymd pandas openpyxl
```

## Executando a Aplicação

```bash
python main.py
```

## Funcionalidades

### Geração de Relatórios
- Cria arquivos Excel com timestamp único
- Dados organizados em planilhas
- Formatação automática

### Gestão de Período
- Seleção de datas inicial e final
- Calendário interativo
- Validação de intervalo de datas

### Personalização
- Tamanho de fonte ajustável
- Temas em tons de azul
- Interface responsiva para diferentes tamanhos de tela

## Estrutura da Interface

1. **Barra Superior**
   - Botão de menu para acessar opções
   - Controles para ajustar tamanho da fonte
   - Título do sistema

2. **Área Principal**
   - Seleção de tipo de relatório
   - Campos para data inicial e final
   - Botão de geração de relatório

3. **Menu Lateral**
   - Lista de opções com checkboxes
   - Acesso rápido aos tipos de relatório
   - Histórico e ajuda

## Personalização

### Configurações de Cores
Modifique as cores no arquivo `main.py`:
```python
# Tons de azul principais
PRIMARY_COLOR = [0.1, 0.4, 0.8, 1]     # Azul principal
SECONDARY_COLOR = [0.7, 0.8, 0.9, 1]   # Azul claro
BACKGROUND_COLOR = [0.9, 0.95, 1, 1]   # Fundo azul claro
```

### Adicionando Novos Tipos de Relatório
1. Adicione um novo botão na interface:
```python
MDRaisedButton:
    text: "Novo Relatório"
    on_release: app.select_report_type("novo_tipo")
```

2. Implemente a lógica de geração:
```python
def generate_novo_tipo_report(self, start_date, end_date):
    # Lógica específica para o novo tipo de relatório
    pass
```

## Licença

Este projeto está licenciado sob a Licença MIT.

## Suporte

Para suporte técnico ou relato de problemas, abra uma issue no repositório do projeto.

---

Desenvolvido por Aléxia Mendes com ❤️ usando Python e KivyMD - [2024]
