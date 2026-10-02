# NEXA — Automação, Dados, Processos e Gestão

O NEXA é um produto independente e adaptativo. Ele não é launcher do Instrua e não incorpora o Instrua.

A proposta é permitir que a pessoa ou empresa descreva como trabalha e faça o NEXA adaptar módulos, campos, dashboards, regras, relatórios e fluxos ao contexto.

## Princípios

- Genérico por padrão: saúde, tecnologia, consultoria, educação, beleza, manutenção, varejo e outros segmentos.
- Configurável: valores, códigos, regras, campos, fórmulas, categorias e modelos não ficam presos ao código.
- Automação e dados: importação de Excel/CSV, processamento, validação, relatórios e regras.
- Faturamento/financeiro como módulos configuráveis, não como definição do produto.
- Interface desktop/mobile responsiva.
- Instrua permanece em repositório e produto separados.

## Arquitetura atual

    NEXA/
    ├── main.py
    ├── app.py
    ├── ui/
    ├── screens/
    ├── repositories/
    ├── core/
    └── tests/

Visual: altere os arquivos .kv. Comportamento: altere screens/. Dados: altere repositories/. Infraestrutura/regras: altere core/.

## Persistência

A primeira fase usa SQLite local em App.user_data_dir. A camada de banco fica separada da UI para permitir evolução posterior para API/backend.

## Módulos atuais

- Dashboard
- Nexa Bill / faturamento
- Nexa Admin
- Central de dados

O módulo de faturamento deve evoluir para modelos universais: serviço, produto, projeto, hora, contrato, recorrência, comissão, convênio/seguro ou outros modelos configuráveis.

## Windows e Android

- .github/workflows/build-windows.yml — build Windows.
- .github/workflows/build-apk.yml — build Android.
- buildozer.spec — configuração Android.
- Windows usa Kivy 2.2.1 + KivyMD 1.2.0.
- Android usa a mesma base compatível inicialmente para reduzir divergência entre ambientes.

A existência do workflow não substitui uma execução real bem-sucedida.

## Segurança

Antes de dados reais, ainda são necessários autenticação, autorização/RBAC, auditoria, backup/recuperação, proteção de documentos, gestão de segredos e estratégia de sincronização.

Nunca versionar dados reais, documentos pessoais, tokens ou senhas.

## Próximas etapas

1. Consolidar o núcleo adaptativo/configurável.
2. Evoluir importação Excel/CSV e mapeamento de colunas.
3. Transformar regras de faturamento em motor genérico.
4. Criar dashboard contextual e automações.
5. Evoluir API/backend e sincronização.
6. Validar builds Windows e Android em execução real.