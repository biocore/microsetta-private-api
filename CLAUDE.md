# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

microsetta-private-api is a private Flask/Connexion microservice for The Microsetta Initiative including the American Gut Project. It manages participant accounts, consent, sample tracking, surveys, and integrations with external services (Vioscreen, AuthRocket, Daklapack, etc.).

## Common Commands

```bash
# Install (editable mode, in conda env)
pip install -e . --no-deps

# Run tests
make test              # all tests via pytest
make test-cov          # tests with coverage
py.test microsetta_private_api/repo/tests/test_account.py           # single file
py.test microsetta_private_api/repo/tests/test_account.py::AccountTests::test_scrub  # single test

# Lint
make lint              # flake8 microsetta_private_api

# Initialize test database (requires running PostgreSQL)
python microsetta_private_api/LEGACY/build_db.py

# Run dev server (http://localhost:8082, Swagger UI at /api/ui)
python ./microsetta_private_api/server.py

# Celery worker (with embedded beat scheduler)
celery -A microsetta_private_api.celery_worker.celery worker -B --loglevel=info
```

## Architecture

### Request Flow

HTTP requests hit the **Connexion/Flask** layer, which routes based on the **OpenAPI 3.0 spec** (`api/microsetta_private_api.yaml`). The `operationId` fields in the spec map directly to Python functions (e.g., `microsetta_private_api.api.find_accounts_for_login`). API handlers live in `microsetta_private_api/api/`.

### Database Access Pattern

The codebase uses a **Repository pattern** with direct SQL via **psycopg2** (no ORM).

- **`repo/transaction.py`** — `Transaction` is a context manager that checks out a connection from a `ThreadedConnectionPool`. All database work must happen inside a `with Transaction() as t:` block. Cursors auto-set `search_path TO ag, barcodes, public, campaign`.
- **`repo/base_repo.py`** — `BaseRepo` takes a `Transaction` in its constructor. All repos inherit from it.
- **Repos** (`repo/*.py`) — Each repo handles SQL for one domain (AccountRepo, SampleRepo, SurveyTemplateRepo, etc.). API handlers create a Transaction, instantiate repo(s), and call methods.
- **Test pattern**: Tests use `unittest.TestCase`. Transactions opened in tests are **rolled back by default** (no explicit `t.commit()`), keeping the test database clean.

There is also a **legacy** `LEGACY/sql_connection.py` with a singleton `TRN` (Transaction) object — this is used only by the database build/migration scripts, not by the main application code.

### Database Schema & Migrations

- PostgreSQL with schemas: `ag`, `barcodes`, `public`, `campaign`
- Initial schema: `db/initialize.sql`
- Migrations: numbered SQL patches in `db/patches/` (0000.sql through 0144+.sql), applied sequentially
- Complex migrations that need Python logic are in `db/migration_support.py` (registered in `MIGRATION_LOOKUP` dict, keyed by patch filename)

### Key External Integrations

- **AuthRocket** — JWT-based authentication (`client/authrocket.py`)
- **Vioscreen** — Food frequency questionnaire service (`util/vioscreen.py`, `repo/vioscreen_repo.py`)
- **Celery + Redis** — Async task processing (worker config in `celery_worker.py`, `celery_utils.py`)
- **Flask-Babel** — i18n with translations in `translations/` (en_US, es_MX, es_ES, ja_JP)

### Configuration

`server_config.json` holds all service configuration (DB credentials, API keys, feature flags, external service endpoints). Accessed via `config_manager.SERVER_CONFIG` dict. Database connection params come from `config_manager.AMGUT_CONFIG` (a `DBConfig` instance).

## Dependencies

Managed via conda (`ci/conda_requirements.txt`) and pip (`ci/pip_requirements.txt`). CI uses Python 3.11 with `setuptools=78`. Key version pins: connexion < 2.7.1, werkzeug >= 2.2.2 < 2.4.0, pandas >= 1.5.0 < 3.0.0. Flask must be pinned to **>= 2.2.0, < 2.3.0** because both connexion and the codebase (`util/util.py`) depend on `flask.json.JSONEncoder`, which was removed in Flask 2.3.
