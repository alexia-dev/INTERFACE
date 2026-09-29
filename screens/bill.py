from kivymd.app import MDApp
from screens.base import NexaScreen


def parse_brl_to_cents(value: str) -> int | None:
    normalized = value.strip().replace("R$", "").replace(" ", "")
    normalized = normalized.replace(".", "").replace(",", ".")
    try:
        amount = float(normalized)
    except ValueError:
        return None
    if amount < 0:
        return None
    return int(round(amount * 100))


def format_brl(cents: int) -> str:
    return f"R$ {cents / 100:.2f}".replace(".", ",")


class BillScreen(NexaScreen):
    def on_pre_enter(self, *args):
        self.refresh_recent()

    def add_bill(self):
        patient = self.ids.bill_patient.text.strip()
        value = parse_brl_to_cents(self.ids.bill_value.text)
        if not patient or value is None:
            self.ids.bill_status.text = "Preencha atendimento e um valor válido."
            return

        app = MDApp.get_running_app()
        app.billing.create(patient, value)
        self.ids.bill_patient.text = ""
        self.ids.bill_value.text = ""
        self.ids.bill_status.text = "Faturamento salvo com sucesso."
        self.refresh_recent()

    def refresh_recent(self):
        app = MDApp.get_running_app()
        rows = app.billing.recent()
        if not rows:
            self.ids.recent_billing.text = "Nenhum lançamento salvo ainda."
            return
        self.ids.recent_billing.text = "\n".join(
            f"{row['patient_name']} • {format_brl(row['value_cents'])} • {row['created_at']}"
            for row in rows
        )
