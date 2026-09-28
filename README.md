# NEXA — Plataforma de Gestão para Clínicas

O **NEXA** é a plataforma principal. Ela organiza módulos independentes para diferentes etapas da operação de uma clínica.

## Estrutura do produto

- **Instrua** — agenda, pacientes, confirmações e instruções.
- **Nexa Bill** — faturamento, lotes, guias, protocolos e relatórios de faturamento.
- **Nexa Admin** — gestão e administração.
- **Central** — pesquisa e visão unificada.

O antigo projeto **SIFAC** passa a ser o módulo **Nexa Bill** dentro do ecossistema NEXA. O conceito de faturamento continua separado do módulo clínico, permitindo que cada parte evolua sem transformar o produto em um único bloco de funcionalidades.

## Estado atual

O repositório já possui:

- 📱 workflow para build Android;
- 💻 workflow para build Windows;
- 🧪 CI e testes básicos;
- 🧩 estrutura inicial da plataforma modular;
- 🔒 orientação para não colocar dados reais de pacientes no repositório público.

## Arquitetura planejada

**Android / Windows / Web → API → banco central**

A plataforma pode futuramente usar uma base local no celular para conectividade limitada e sincronização posterior.

### Módulos

`NEXA`
→ `Instrua`
→ `Nexa Bill`
→ `Nexa Admin`
→ `Central`

## Próximas etapas técnicas

1. Tirar dados fixos do painel e usar base local.
2. Criar cadastro real de lotes e pesquisa no Nexa Bill.
3. Integrar API + banco central.
4. Adicionar importação de Excel/PDF.
5. Adicionar OCR com conferência antes de salvar.
6. Criar autenticação, perfis de acesso, backup e trilha de alterações antes de dados reais.

## Privacidade

O código público não deve conter nomes reais de pacientes, documentos pessoais, informações clínicas, protocolos reais ou outros dados identificáveis.

Use apenas dados fictícios ou anonimizados durante o desenvolvimento.

## Arquivos principais

- `main.py` — aplicação principal NEXA
- `buildozer.spec` — configuração Android
- `.github/workflows/build-apk.yml` — build Android
- `.github/workflows/ci.yml` — testes e validação
- `.github/workflows/build-windows.yml` — build Windows
- `tests/test_basic.py` — testes iniciais

## Status

🚧 Em desenvolvimento
