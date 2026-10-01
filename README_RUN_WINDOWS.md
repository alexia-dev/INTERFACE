# Executar o NEXA real no Windows

O NEXA deste repositório é o aplicativo Python + Kivy/KivyMD. O arquivo HTML de demo não é necessário para executar o aplicativo real.

## Opção mais simples

1. Clone ou baixe o repositório.
2. Abra a pasta do NEXA.
3. Dê duplo clique em **run_nexa.bat**.

O launcher:
- verifica o Python 3.11;
- cria o ambiente virtual local em `.venv`;
- instala `requirements-windows.txt`;
- inicia `main.py`.

## Pelo VS Code

Abra a pasta do repositório e execute:

```powershell
.\.venv\Scripts\python.exe main.py
```

Na primeira execução, rode antes:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-windows.txt
```

## Observação

A API padrão do cliente é `http://127.0.0.1:8080`. O NEXA consegue abrir localmente mesmo sem a API, porque o shell e os módulos que usam o SQLite local são inicializados no próprio aplicativo. Recursos que dependem da API ficam disponíveis quando o backend estiver em execução.

O objetivo do launcher é tornar o projeto reproduzível a partir do próprio Git, sem depender de caminhos absolutos da máquina de desenvolvimento.
