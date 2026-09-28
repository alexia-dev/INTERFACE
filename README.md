# SIFAC — Sistema de Faturamento e Relatórios

O **SIFAC** está evoluindo de uma base de relatórios para uma aplicação multiplataforma de controle de faturamento.

## Onde estamos

O repositório já possui estrutura para:

- 📱 gerar APK Android por GitHub Actions;
- 💻 preparar build do aplicativo para Windows;
- 🧪 validar a estrutura automaticamente com testes;
- 🔒 manter o repositório sem dados reais de pacientes ou documentos.

## Android

O workflow **Build SIFAC Android APK** gera uma build de desenvolvimento e publica o APK como artefato.

No GitHub: **Actions → Build SIFAC Android APK → Run workflow → sifac-apk**.

## Windows

O workflow **Build SIFAC Windows** prepara um executável `.exe` sob demanda ou a partir de uma tag v*.

## Próximas etapas técnicas

1. Tirar os dados fixos do painel e passar para uma base local.
2. Criar cadastro real de lotes e pesquisa.
3. Migrar o armazenamento para uma API + banco central quando a sincronização celular/computador entrar.
4. Adicionar importação de Excel/PDF.
5. Adicionar OCR posteriormente, sempre mostrando os campos identificados para conferência antes de salvar.
6. Criar autenticação, perfis de acesso, backup e trilha de alterações antes de usar dados reais.

## Arquitetura planejada

**Android / Windows / Web → API → banco central**

No celular, uma base local pode ser usada para permitir trabalho com conectividade limitada e posterior sincronização.

## Privacidade

O código público não deve conter nomes reais de pacientes, documentos pessoais, informações clínicas, protocolos reais ou outros dados identificáveis.

Para desenvolvimento, use apenas dados fictícios ou anonimizados.

## Arquivos principais

- `main.py` — aplicação
- `buildozer.spec` — configuração Android
- `.github/workflows/build-apk.yml` — build Android
- `.github/workflows/ci.yml` — testes e validação
- `.github/workflows/build-windows.yml` — build Windows
- `tests/test_basic.py` — testes iniciais

## Status

🚧 Em desenvolvimento
