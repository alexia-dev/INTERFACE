# NEXA — Plataforma de Gestão para Clínicas

O NEXA é a plataforma principal para organizar atendimento, faturamento, administração e pesquisa em módulos independentes.

## Arquitetura do app

O frontend usa Kivy + KivyMD com uma separação simples para facilitar alterações:

```text
NEXA/
├── main.py                 # entrada mínima
├── app.py                  # composição, navegação e inicialização
├── ui/                     # aparência e layout
│   ├── theme.kv            # tokens e componentes visuais
│   ├── app.kv              # shell + menu lateral
│   ├── home.kv             # dashboard
│   ├── instrua.kv          # tela Instrua
│   ├── bill.kv             # tela Nexa Bill
│   ├── admin.kv            # tela Nexa Admin
│   └── central.kv          # tela Central
├── screens/                # comportamento de cada tela
├── repositories/           # acesso aos dados
├── core/                   # infraestrutura, incluindo SQLite
└── tests/                  # testes
```

### Regra para manutenção

**Visual:** altere somente o `.kv` da tela.

**Comportamento:** altere o arquivo correspondente em `screens/`.

**Dados:** altere o repositório em `repositories/`.

**Infraestrutura:** altere `core/`.

**Entrada do app:** `main.py` quase nunca precisa mudar.

Essa separação também deixa preparada uma futura troca de SQLite por API/backend sem precisar reescrever as telas.

## Mobile-first

O layout foi adaptado para celular sem criar uma segunda versão da interface. A mesma tela reorganiza os elementos conforme a largura disponível: o dashboard passa de duas colunas para uma, formulários ocupam a largura da tela e as áreas longas usam rolagem vertical.

O app não fixa mais uma janela desktop de `1000x680`. A interface usa `size_hint`, `dp`, `minimum_height` e layouts adaptáveis para funcionar em diferentes tamanhos de tela. O Kivy documenta `size_hint` como a forma de distribuir espaço proporcionalmente entre widgets e recomenda `system_size` em cenários onde o tamanho da janela precisa ser definido programaticamente. O KivyMD também oferece componentes responsivos e propriedades adaptativas para esse tipo de interface.

## Dados locais

O NEXA usa SQLite para persistência local inicial. O banco é criado no diretório gravável específico da aplicação por meio de `App.user_data_dir`.

Tabelas atuais:

- `appointments`
- `billings`

As operações ficam atrás de repositórios, portanto a UI não conhece SQL.

## Módulos atuais

- **Instrua:** agenda e atendimento.
- **Nexa Bill:** lançamentos de faturamento.
- **Nexa Admin:** administração inicial.
- **Central:** pesquisa unificada dos dados locais.

## Android e Windows

- `.github/workflows/build-apk.yml` — geração do APK Android.
- `.github/workflows/build-windows.yml` — build para Windows.
- `buildozer.spec` — configuração do app Android.

Os workflows precisam ser validados em execução real; a presença do YAML, sozinha, não comprova uma build bem-sucedida.

## Segurança

Antes de dados reais, o projeto ainda precisa de autenticação, autorização por papel, auditoria, backups, proteção de documentos e estratégia de sincronização.

Nunca enviar ao repositório público nomes reais de pacientes, documentos pessoais, informações clínicas, planilhas reais, tokens ou senhas.

## Próximo estágio

1. Login e RBAC.
2. Cadastros persistentes completos.
3. Expansão do Instrua.
4. Guias, lotes e relatórios do Nexa Bill.
5. Usuários, perfis e auditoria do Nexa Admin.
6. API/backend e sincronização.
