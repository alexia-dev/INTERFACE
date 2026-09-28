# SIFAC — Sistema de Faturamento e Relatórios

O **SIFAC** é um projeto em desenvolvimento voltado para organizar e automatizar rotinas de faturamento e geração de relatórios.

A proposta é transformar processos que normalmente ficam espalhados entre planilhas, documentos e conferências manuais em um fluxo mais simples, organizado e fácil de acompanhar.

## Objetivo

O SIFAC foi pensado para:

- organizar informações de faturamento por ano e mês;
- registrar lotes, protocolos, quantidades e valores;
- facilitar a consulta de registros;
- gerar relatórios organizados;
- reduzir tarefas manuais repetitivas;
- funcionar de forma simples para pessoas com diferentes níveis de familiaridade com tecnologia.

## Visão do aplicativo

A evolução do SIFAC contempla **celular e computador**, usando a mesma aplicação e a mesma estrutura de dados.

**Celular**
- consulta de faturamentos;
- lançamento de novos lotes;
- conferência de informações;
- futura leitura de foto/documento.

**Computador**
- painel de acompanhamento;
- pesquisa de registros;
- controle mensal e anual;
- geração de relatórios.

## Abrir no celular

O repositório agora contém a configuração para gerar um **APK Android de teste** automaticamente pelo GitHub Actions.

No GitHub:
1. Abra a aba **Actions**.
2. Entre em **Build SIFAC Android APK**.
3. Clique em **Run workflow** para gerar manualmente.
4. Quando terminar, baixe o artefato **sifac-apk**.
5. Dentro do ZIP estará o APK para instalar no Android.

> Esta é uma build de desenvolvimento/teste. Assinatura de distribuição e publicação em loja ficam para uma etapa posterior.

## Funcionalidades em desenvolvimento

- Controle por ano e mês
- Cadastro de lotes
- Registro de protocolos
- Controle de quantidade de guias
- Controle de valores
- Status de processamento
- Pesquisa de registros
- Relatórios em Excel
- Dashboard de acompanhamento
- Evolução para sincronização entre dispositivos
- Automação de leitura de documentos

## Tecnologias

- **Python**
- **Kivy**
- **KivyMD**
- **Buildozer**
- GitHub Actions para build Android

## Arquivos principais

- `main.py` — aplicação principal
- `build.py` — processo de empacotamento desktop
- `buildozer.spec` — configuração do APK Android
- `.github/workflows/build-apk.yml` — automação de build Android

## Privacidade

O repositório não deve conter dados reais de pacientes, documentos pessoais, informações clínicas, protocolos reais ou qualquer outro dado identificável.

Os exemplos e testes do projeto devem utilizar **dados fictícios ou anonimizados**.

## Status

🚧 **Em desenvolvimento**

A carcaça atual está preparada para evoluir para um aplicativo multiplataforma.