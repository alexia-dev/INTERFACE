# NEXA — Plataforma de Gestão para Clínicas

O **NEXA** é a plataforma principal para organizar módulos independentes da operação clínica, mantendo atendimento, faturamento e administração separados por domínio.

## Estrutura do produto

- **Instrua** — jornada clínica: agenda, pacientes, consultas, confirmações, check-in, instruções e notificações.
- **Nexa Bill** — faturamento: guias, lotes, protocolos, conferência, valores, importação e relatórios.
- **Nexa Admin** — administração: usuários, perfis, configurações, auditoria e indicadores.
- **Central** — busca e visão unificada, respeitando permissões e o contexto da clínica.

O módulo de faturamento do NEXA utiliza a identidade **Nexa Bill**. O faturamento continua separado do fluxo clínico para manter a experiência simples e permitir evolução independente.

## Arquitetura-alvo

A primeira etapa será um **monólito modular** com API central e banco PostgreSQL multi-tenant:

```text
Android / Windows / Web
          ↓
       NEXA API
          ↓
      PostgreSQL
          ↓
   módulos do NEXA
```

A separação entre módulos será feita por domínio dentro do mesmo backend. Microserviços ficam como possibilidade futura, não como requisito do MVP.

## Multi-tenant e segurança

Toda entidade pertencente a uma clínica deverá carregar o contexto do tenant. A API deve aplicar esse contexto em todas as consultas e comandos.

Perfis planejados:

- PLATFORM_ADMIN
- COMPANY_OWNER
- COMPANY_ADMIN
- RECEPTION
- CLINICAL
- BILLING
- PATIENT

Antes de dados reais, o projeto deverá ter autenticação, autorização por papel, trilha de auditoria, backups e proteção de documentos.

## Estado atual

- 📱 workflow Android configurado;
- 💻 workflow Windows configurado;
- 🧪 CI e testes básicos;
- 🧩 shell inicial modular;
- 🔒 política de não usar dados reais no repositório público.

> Os workflows ainda precisam ser validados em execução real. A existência do YAML não significa que o APK/EXE já foi comprovadamente gerado com sucesso.

## Próximas etapas

1. Estruturar o backend modular.
2. Formalizar o modelo multi-tenant.
3. Criar API REST documentada.
4. Implementar autenticação e RBAC.
5. Evoluir Instrua.
6. Criar o domínio Nexa Bill.
7. Adicionar auditoria e backups.
8. Depois, importar Excel/PDF e implementar OCR com conferência humana.
9. Mais adiante, adicionar cache/offline e sincronização.

## Regras para documentos e dados

Nunca enviar ao GitHub:

- nomes reais de pacientes;
- documentos pessoais;
- informações clínicas;
- protocolos reais;
- planilhas reais;
- tokens, senhas ou segredos.

Use dados fictícios ou anonimizados nos exemplos e testes.

## Estrutura sugerida

```text
nexa/
├── modules/
│   ├── instrua/
│   ├── nexa_bill/
│   ├── nexa_admin/
│   └── central/
├── core/
│   ├── auth/
│   ├── tenant/
│   ├── audit/
│   └── storage/
├── tests/
└── docs/
```

## Build e CI/CD

- `.github/workflows/ci.yml` — sintaxe, testes e validações;
- `.github/workflows/build-apk.yml` — Android;
- `.github/workflows/build-windows.yml` — Windows.

O pipeline deve bloquear merges quando testes falharem.

## Interface

A interface do NEXA segue a linguagem visual migrada das telas antigas do projeto: estética clínica moderna, superfícies claras, lilás/violeta como acento, cartões com cantos arredondados e navegação modular.

O nome e a identidade apresentados na interface são **NEXA**.

## Status

🚧 Em desenvolvimento
