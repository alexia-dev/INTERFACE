from datetime import datetime, timezone

from core.database import Database


class BillingRepository:
    def __init__(self, database: Database):
        self.database = database

    def create(self, client_name: str, value_cents: int) -> int:
        created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        return self.database.execute(
            """
            INSERT INTO billings(client_name, value_cents, created_at)
            VALUES (?, ?, ?)
            """,
            (client_name, value_cents, created_at),
        )

    def recent(self, limit: int = 5) -> list[dict]:
        rows = self.database.fetch_all(
            """
            SELECT id, client_name, value_cents, created_at
            FROM billings
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [dict(row) for row in rows]

    def delete(self, billing_id: int) -> None:
        self.database.execute(
            "DELETE FROM billings WHERE id = ?",
            (billing_id,),
        )
