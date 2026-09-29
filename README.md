# NEXA

## Ecossistema de aplicativos

O NEXA não é um aplicativo monolítico de uso exclusivo para clínicas. Ele é a marca de um ecossistema de aplicativos independentes conectados por identidade e serviços compartilhados.

### Aplicativos

- **Instrua** — jornada de atendimento, agenda, instruções, confirmação e check-in.
- **Nexa Bill** — faturamento e relatórios.
- **Nexa AI** — assistente e recursos de IA (planejado).
- **Nexa Study** — estudo e aprendizagem (planejado).
- **Nexa Work** — carreira e produtividade (planejado).
- **Nexa Central** — hub opcional do ecossistema.

### Princípio

Baixe somente o aplicativo que precisa. Use uma conta NEXA para acessar vários produtos e, quando disponível, assine recursos premium individualmente ou por bundles.

## Estrutura atual

Frontend em Kivy + KivyMD:

- `ui/` — layouts e identidade visual.
- `screens/` — comportamento das telas.
- `repositories/` — persistência local/cache legado.
- `core/api_client.py` — REST API.
- `core/session.py` — sessão em memória.
- `core/config.py` — configuração da API.
- `core/models.py` — modelos de ecossistema.
- `core/database.py` — SQLite local/cache.
- `main.py` — entrada mínima.

## Contrato de plataforma

A API compartilhada deve evoluir para expor:

- identidade/autenticação;
- perfil do usuário;
- organizações e memberships;
- catálogo de aplicativos;
- entitlements/planos;
- assinaturas e pagamentos;
- notificações;
- arquivos;
- auditoria.

Os domínios de produto continuam separados. O cliente não é a fonte de verdade para autorização, assinatura ou isolamento de dados.

## Aplicativos e repositórios

Neste estágio, `alexia-dev/Nexa` permanece como cliente/Central e `alexia-dev/Instrua` permanece separado como backend/API do Instrua. Novos produtos podem ganhar repositórios próprios sem quebrar o ecossistema.

## Segurança

- Tokens permanecem em memória no cliente.
- O backend valida autenticação e autorização.
- Dados por organização precisam ser isolados no servidor.
- Não versionar dados reais, documentos, tokens, senhas ou informações clínicas/financeiras.

## Estado

Fundação em implementação. A conexão completa cliente -> plataforma -> produto será fechada em etapas, com testes antes de considerar produção.
