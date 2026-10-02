import sqlite3
from pathlib import Path


class Database:
    """Small SQLite gateway kept independent from the UI."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.initialize()

    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_name TEXT NOT NULL,
                    appointment_type TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS providers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    active INTEGER NOT NULL DEFAULT 1
                );

                CREATE TABLE IF NOT EXISTS insurers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    active INTEGER NOT NULL DEFAULT 1
                );

                CREATE TABLE IF NOT EXISTS procedures (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL,
                    name TEXT NOT NULL,
                    table_type TEXT,
                    unit TEXT,
                    active INTEGER NOT NULL DEFAULT 1,
                    notes TEXT
                );

                CREATE TABLE IF NOT EXISTS price_rules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    provider_id INTEGER NOT NULL,
                    insurer_id INTEGER NOT NULL,
                    procedure_id INTEGER NOT NULL,
                    modality TEXT NOT NULL,
                    amount_cents INTEGER NOT NULL CHECK(amount_cents >= 0),
                    valid_from TEXT NOT NULL,
                    valid_to TEXT,
                    active INTEGER NOT NULL DEFAULT 1,
                    notes TEXT,
                    FOREIGN KEY(provider_id) REFERENCES providers(id),
                    FOREIGN KEY(insurer_id) REFERENCES insurers(id),
                    FOREIGN KEY(procedure_id) REFERENCES procedures(id)
                );

                CREATE TABLE IF NOT EXISTS import_mappings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    source_format TEXT NOT NULL,
                    source_column TEXT NOT NULL,
                    target_field TEXT NOT NULL,
                    required INTEGER NOT NULL DEFAULT 0,
                    active INTEGER NOT NULL DEFAULT 1
                );

                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    entity_type TEXT NOT NULL,
                    entity_id TEXT,
                    action TEXT NOT NULL,
                    previous_value TEXT,
                    new_value TEXT,
                    changed_by TEXT,
                    changed_at TEXT NOT NULL,
                    reason TEXT
                );

                CREATE TABLE IF NOT EXISTS billings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_name TEXT NOT NULL,
                    value_cents INTEGER NOT NULL CHECK(value_cents >= 0),
                    created_at TEXT NOT NULL
                );
                """
            )

    def execute(self, sql: str, parameters: tuple = ()) -> int:
        with self.connect() as connection:
            cursor = connection.execute(sql, parameters)
            return int(cursor.lastrowid or 0)

    def fetch_all(self, sql: str, parameters: tuple = ()) -> list[sqlite3.Row]:
        with self.connect() as connection:
            return list(connection.execute(sql, parameters).fetchall())
