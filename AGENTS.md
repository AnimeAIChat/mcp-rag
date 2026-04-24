# AGENTS.md — Guidelines for Agentic Coding Agents

## Project Overview

MCP-based RAG service with a Python backend (FastAPI + MCP) and a Svelte 5 frontend dashboard.
Python 3.13+, package manager `uv`, frontend uses `pnpm`.

---

## Build / Dev / Test Commands

### Python Backend

```bash
# Install dependencies (dev)
uv sync

# Install with optional local embeddings
uv sync --extra local-embeddings

# Run server
uv run mcp-rag serve

# Initialize data directory
uv run mcp-rag init --data-dir ./data

# Compile check
uv run python -m compileall src
```

### Frontend (Svelte 5 + Vite)

```bash
cd frontend

# Install dependencies
pnpm install

# Dev server
pnpm dev

# Build (outputs to ../src/mcp_rag/static/app)
pnpm build
```

### Testing

Framework: **Python `unittest`** (standard library, NOT pytest).

```bash
# Run all tests
uv run python -m unittest discover -s tests

# Run a single test file
uv run python -m unittest tests/test_config.py

# Run a specific test class
uv run python -m unittest tests/test_config.ConfigManagerTests

# Run a single test method
uv run python -m unittest tests/test_config.ConfigManagerTests.test_missing_config_uses_defaults_without_eager_file_creation
```

Tests use `tempfile.TemporaryDirectory()` for isolation, `unittest.mock.AsyncMock` for mocks, and `FastAPI.testclient.TestClient` for HTTP integration tests. Async tests use `unittest.IsolatedAsyncioTestCase`.

---

## Code Style Conventions

### Python

**Imports:**
- `from __future__ import annotations` at the top of every file
- Standard library → third-party → relative imports (`.` prefix)
- No import sorting tool; maintain consistent manual ordering

**Formatting:**
- 4-space indentation
- Double quotes preferred (but single quotes exist in codebase)
- Trailing commas in multi-line structures
- No explicit line length enforcement, but keep lines reasonable

**Type Hints:**
- Extensive use throughout; `from __future__ import annotations` enables `dict[str, Any]` syntax
- Union types: `str | None` (not `Optional[str]`)
- Use `dataclass(slots=True, frozen=True)` for immutable value objects
- Pydantic `BaseModel` for configuration objects with `Field()` for defaults/descriptions
- Prefer built-in generics: `dict[str, Any]`, `list[str]`, `Mapping[str, Any]`

**Naming:**
- Classes: `PascalCase` (`ConfigManager`, `ServiceRuntime`)
- Functions/methods: `snake_case` (`normalize_tenant`, `reload_if_changed`)
- Constants: `UPPER_SNAKE_CASE` (`_ACTIVE_STATUS`, `_PUBLIC_SCOPE`)
- Private members: `_leading_underscore` (`_lock`, `_settings`)

**Error Handling:**
- Custom exception hierarchies for domain errors (e.g., `SecurityError` subclasses)
- `try/except` with `print()` for non-critical failures
- `contextlib.suppress(FileNotFoundError)` for optional file reads
- `logging.warning()` for recoverable errors
- Pair `validate()` (returns decision) with `require()` (raises exception) methods

**Concurrency:**
- `threading.RLock` for thread-safe operations (config, SQLite)
- `asyncio.Lock` for async-safe operations
- `dataclasses.field(default_factory=Lock, repr=False)` for locks in dataclasses

### JavaScript / Svelte (Frontend)

- ES modules with relative paths (`.js`, `.svelte` extensions required)
- Svelte 5 (runes style)
- Plain CSS with custom properties (design tokens in `:root`)
- Native `fetch` for API calls (thin wrapper in `src/lib/api.js`)
- camelCase for JS variables/functions

---

## Architecture

Layered architecture:
```
HTTP/MCP Shell → Context → Service Facade → Services → Core Indexing → Retrieval
```

Key patterns:
- `ServiceRuntime` as lazy dependency container with double-checked locking
- `SettingsProxy` for hot-reloadable configuration
- Tenant-based multi-tenancy with `base_collection + user_id + agent_id` scoping
- Request/Response dataclasses with `__post_init__` for normalization

---

## Docstrings and Comments

- Docstrings are in **Chinese**
- Module-level comments may be in English
- Follow existing language convention when adding comments

---

## No Linter/Formatter Configured

There are no ESLint, Prettier, Ruff, Black, mypy, or pyright configs. Follow the existing code conventions manually. No `.editorconfig` or `Makefile` exists either.

---

## No Cursor/Copilot Rules

No `.cursorrules`, `.cursor/rules/`, or `.github/copilot-instructions.md` files exist in this repo.
