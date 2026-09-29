# NEXA

## Ecossistema de aplicativos

O NEXA não é um aplicativo monolítico de uso exclusivo para clínicas. Ele é a marca de um ecossistema de aplicativos independentes conectados por identidade e serviços compartilhados.

### Aplicativos

- **Instrua** — jornada de atendimento, agenda, instruções, confirmação e check-in.
- **Nexa Bill** — faturamento, lotes, protocolos, conferência e relatórios.
- **Nexa AI** — assistente e recursos de IA.
- **Nexa Study** — estudo e aprendizagem (planejado).
- **Nexa Work** — carreira e produtividade (planejado).
- **Nexa Central** — hub opcional do ecossistema.

### Princípio

Baixe somente o aplicativo que precisa. Use uma conta NEXA para acessar vários produtos e, quando disponível, assine recursos premium individualmente ou por bundles.

## Fundação implementada

A branch `feature/nexa-ecosystem` já prepara o cliente para os primeiros contratos de plataforma:

- catálogo de aplicativos;
- organizações;
- entitlements/planos;
- resumo da jornada do Instrua;
- cliente REST para `/me`, organizações, apps, entitlements e jornada;
- temas Light/Dark persistentes no shell visual.

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

A API compartilhada deve evoluir para expor identidade/autenticação, perfil, organizações, catálogo de aplicativos, entitlements/planos, notificações, arquivos, auditoria e serviços de produto.

Os domínios de produto continuam separados. O cliente não é a fonte de verdade para autorização, assinatura ou isolamento de dados.

## Segurança

- Tokens permanecem em memória no cliente.
- O backend valida autenticação e autorização.
- Dados por organização precisam ser isolados no servidor.
- Não versionar dados reais, documentos, tokens, senhas ou informações clínicas/financeiras.

## Estado

Fundação em implementação. Os novos contratos de plataforma foram adicionados sem remover o shell existente. Antes de produção, precisamos validar build, testes, banco e integração ponta a ponta.
