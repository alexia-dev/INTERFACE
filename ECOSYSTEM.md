# NEXA ECOSYSTEM

NEXA is an ecosystem of independent applications connected by shared platform services.

## Product model

Each application can be installed and used independently:

- **Instrua** — appointments, service journeys, instructions, confirmations and check-in.
- **Nexa Bill** — billing, lots, guides, protocols and reports.
- **Nexa AI** — future assistant and AI tools.
- **Nexa Study** — future learning and study tools.
- **Nexa Work** — future productivity and career tools.
- **Nexa Central** — optional hub for discovering and launching NEXA applications.

The applications are not embedded inside one giant app. They share identity, platform capabilities and authorized data through APIs.

## Shared platform concepts

### NEXA Account

One account can access multiple applications.

### Organizations

A person can use NEXA personally and also belong to one or more organizations (clinic, salon, shop, service business, school, etc.).

### App access and entitlements

Access is controlled per application and per plan:

- FREE
- PREMIUM / PRO
- BUSINESS
- future bundles

The backend is the source of truth for permissions and entitlements.

## Repository direction

Current repositories:

- `alexia-dev/Nexa` — NEXA Central/client foundation.
- `alexia-dev/Instrua` — Instrua API/backend and its web shell.

Future applications can keep their own repositories while consuming the shared NEXA platform contracts.

## Client architecture

The NEXA Python client uses:

- `core/api_client.py` — REST communication
- `core/session.py` — in-memory authenticated session
- `repositories/` — local/cache compatibility
- `screens/` and `ui/` — presentation

SQLite is not the platform source of truth. It remains a local compatibility/cache layer while the API is adopted progressively.

## Important security rule

Never trust the client UI for authorization. The API must validate:

1. authenticated identity;
2. organization/app access;
3. role/permission;
4. resource ownership/tenant isolation;
5. premium/business entitlements.

Never commit real personal, health, billing, credential or token data.

## Current status

The ecosystem foundation is being implemented incrementally. The current branch adds the architecture contract without removing the working application shell.
