from kivymd.app import MDApp

from core.billing_format import format_brl, parse_decimal_amount
from screens.base import NexaScreen




class BillScreen(NexaScreen):
    def on_pre_enter(self, *args):
        self.refresh_recent()

    def add_bill(self):
        client = self.ids.bill_patient.text.strip()
        value = parse_decimal_amount(self.ids.bill_value.text)
        if not client or value is None:
            self.ids.bill_status.text = "Preencha atendimento e um valor válido."
            return

        app = MDApp.get_running_app()
        app.billing.create(client, value)
        self.ids.bill_patient.text = ""
        self.ids.bill_value.text = ""
        self.ids.bill_status.text = "Faturamento salvo com sucesso."
        self.refresh_recent()

    def delete_latest(self):
        rows = MDApp.get_running_app().billing.recent(1)
        if not rows:
            self.ids.bill_status.text = "Não há lançamento para excluir."
            return
        MDApp.get_running_app().billing.delete(rows[0]["id"])
        self.ids.bill_status.text = "Último lançamento excluído."
        self.refresh_recent()

    def refresh_recent(self):
        app = MDApp.get_running_app()
        rows = app.billing.recent()
        if not rows:
            self.ids.recent_billing.text = "Nenhum lançamento salvo ainda."
            return
        self.ids.recent_billing.text = "\n".join(
            f"{row['client_name']} • {format_brl(row['value_cents'])} • {row['created_at']}"
            for row in rows
        )
