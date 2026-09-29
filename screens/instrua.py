from kivymd.app import MDApp
from screens.base import NexaScreen


class InstruaScreen(NexaScreen):
    def on_pre_enter(self, *args):
        self.refresh_recent()

    def add_appointment(self):
        patient = self.ids.patient_input.text.strip()
        appointment = self.ids.appointment_input.text.strip()
        if not patient or not appointment:
            self.ids.appointment_status.text = "Preencha paciente e consulta."
            return

        app = MDApp.get_running_app()
        app.appointments.create(patient, appointment)
        self.ids.patient_input.text = ""
        self.ids.appointment_input.text = ""
        self.ids.appointment_status.text = "Agendamento salvo com sucesso."
        self.refresh_recent()

    def refresh_recent(self):
        app = MDApp.get_running_app()
        rows = app.appointments.recent()
        if not rows:
            self.ids.recent_list.text = "Nenhum atendimento salvo ainda."
            return
        self.ids.recent_list.text = "\n".join(
            f"{row['patient_name']} • {row['appointment_type']} • {row['created_at']}"
            for row in rows
        )
