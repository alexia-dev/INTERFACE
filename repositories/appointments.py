from datetime import datetime, timezone

from core.database import Database


class AppointmentRepository:
    def __init__(self, database: Database):
        self.database = database

    def create(self, patient_name: str, appointment_type: str) -> int:
        created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        return self.database.execute(
            """
            INSERT INTO appointments(patient_name, appointment_type, created_at)
            VALUES (?, ?, ?)
            """,
            (patient_name, appointment_type, created_at),
        )

    def recent(self, limit: int = 5) -> list[dict]:
        rows = self.database.fetch_all(
            """
            SELECT id, patient_name, appointment_type, created_at
            FROM appointments
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [dict(row) for row in rows]

    def delete(self, appointment_id: int) -> None:
        self.database.execute(
            "DELETE FROM appointments WHERE id = ?",
            (appointment_id,),
        )
