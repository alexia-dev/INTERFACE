from kivymd.app import MDApp

from screens.base import NexaScreen


class CentralScreen(NexaScreen):
    def search(self):
        query = self.ids.search_input.text.strip()
        if not query:
            self.ids.search_result.text = "Digite algo para pesquisar."
            return

        app = MDApp.get_running_app()
        appointments = app.appointments.recent(20)
        billings = app.billing.recent(20)
        matches = []
        needle = query.casefold()

        for row in appointments:
            if needle in row["patient_name"].casefold() or needle in row["appointment_type"].casefold():
                matches.append(
                    f"Instrua • {row['patient_name']} • {row['appointment_type']}"
                )

        for row in billings:
            if needle in row["patient_name"].casefold():
                matches.append(
                    f"Nexa Bill • {row['patient_name']} • {row['value_cents'] / 100:.2f}"
                )

        self.ids.search_result.text = (
            "\n".join(matches)
            if matches
            else "Nenhum resultado encontrado nos dados locais."
        )
