# NEXA — Plataforma de Gestão para Clínicas

O NEXA é a plataforma principal para organizar atendimento, faturamento, administração e pesquisa em módulos independentes.

## Arquitetura do app

Frontend em Kivy + KivyMD, organizado para facilitar alterações:

- `ui/` = visual e layouts
- `screens/` = comportamento das telas
- `repositories/` = persistência local/cache legado
- `core/api_client.py` = comunicação REST com o backend
- `core/session.py` = sessão em memória
- `core/database.py` = SQLite local/cache
- `main.py` = entrada mínima

### Regra para manutenção

Visual -> altere o `.kv` da tela.

Comportamento -> altere `screens/`.

Dados remotos -> use `core/api_client.py`.

Dados locais/cache -> `repositories/` e `core/database.py`.

Sessão -> `core/session.py`.

Essa separação prepara a troca progressiva do SQLite por API/backend sem reescrever a interface.

## API central

A primeira camada de cliente REST usa:

- `POST /api/v1/auth/login`
- `GET /api/v1/companies`
- `GET /api/v1/companies/{companyId}/patients`

O backend de referência é `alexia-dev/Instrua`.

## Dados locais

SQLite permanece como camada local/compatibilidade durante a transição; não é a fonte de verdade da plataforma conectada.

## Módulos

- Instrua: agenda, pacientes, confirmações, check-in e instruções.
- Nexa Bill: faturamento, lotes, guias, protocolos e relatórios.
- Nexa Admin: usuários, perfis e administração.
- Central: pesquisa e visão unificada.

## Backend / Instrua

O repositório `alexia-dev/Instrua` já contém a base Java 21 + Spring Boot + PostgreSQL + Flyway, com JWT, perfis, empresas/tenants, pacientes, auditoria, agenda, instruções, notificações e integrações.

A integração completa UI -> API -> PostgreSQL ainda exige validação de execução e expansão dos endpoints.

## Segurança

Antes de dados reais, a plataforma precisa de autenticação, autorização por papel, isolamento de tenant, auditoria, backups, proteção de documentos e estratégia de sincronização.

Nunca enviar ao repositório público nomes reais de pacientes, documentos pessoais, informações clínicas, planilhas reais, tokens ou senhas.

## Próximo estágio

1. Validar build e testes do backend.
2. Fechar login do NEXA com API.
3. Conectar Pacientes e Agenda ao Instrua.
4. Implementar o domínio do Nexa Bill na API.
5. Aplicar RBAC por endpoint e módulo.
6. Publicar builds de teste para Windows e Android.
