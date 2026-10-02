from __future__ import annotations

from typing import Any
from core.database import Database


class AiTools:
    def __init__(self, database: Database):
        self.database=database

    def summary(self) -> dict[str, Any]:
        bills=self.database.fetch_all("select count(*) as total, coalesce(sum(value_cents),0) as total_cents from billings")
        return {"billing": bills[0] if bills else {"total":0,"total_cents":0}}

    def billing_recent(self) -> dict[str, Any]:
        rows=self.database.fetch_all("select id, client_name, value_cents, created_at from billings order by id desc limit 20")
        return {"items":rows}

    def billing_divergences(self) -> dict[str, Any]:
        rows=self.database.fetch_all("""
            select client_name, count(*) as occurrences, sum(value_cents) as total_cents
            from billings group by client_name having count(*) > 1 order by occurrences desc
        """)
        return {"possibleDuplicates":rows}
