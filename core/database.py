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
