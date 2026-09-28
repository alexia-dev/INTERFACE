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

O projeto está sendo desenvolvido de forma incremental, começando pela organização dos dados e dos relatórios e evoluindo para uma aplicação multiplataforma.

## Visão do aplicativo

A evolução planejada do SIFAC contempla:

**📱 Celular**
- consulta de faturamentos;
- lançamento de novos lotes;
- conferência de informações;
- registro por foto/documento como etapa de automação futura.

**💻 Computador**
- painel de acompanhamento;
- pesquisa de registros;
- controle mensal e anual;
- geração e organização de relatórios.

A ideia é que celular e computador utilizem a mesma estrutura de dados, permitindo continuidade do trabalho entre dispositivos.

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

## Tecnologias atuais

- **Python 3.9+**
- **KivyMD**
- **Pandas**
- **Openpyxl**
- **Dateutil**

As tecnologias podem evoluir conforme o projeto avance para uma arquitetura multiplataforma.

## Estrutura atual

A versão atual do projeto é uma base de aplicação desktop para geração e organização de relatórios.

Arquivos principais:

- `main.py` — aplicação principal
- `build.py` — processo de empacotamento
- `criar_atalho.py` — criação de atalho
- `sistema-de-relat195179rios.ico` — ícone da aplicação

## Privacidade

O repositório não deve conter dados reais de pacientes, documentos pessoais, informações clínicas, protocolos reais ou qualquer outro dado identificável.

Os exemplos e testes do projeto devem utilizar **dados fictícios ou anonimizados**.

## Status

🚧 **Em desenvolvimento**

O projeto está passando de uma solução de relatórios para uma aplicação de controle de faturamento mais completa e simples de utilizar.

## Licença

Este projeto está licenciado sob a Licença MIT.

---

Desenvolvido por **Aléxia Mendes**.
