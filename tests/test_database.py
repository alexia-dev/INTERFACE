from core.database import Database
from repositories.appointments import AppointmentRepository
from repositories.billing import BillingRepository


def test_local_data_persists(tmp_path):
    database = Database(tmp_path / "nexa.db")
    appointments = AppointmentRepository(database)
    billing = BillingRepository(database)

    appointments.create("Paciente Teste", "Consulta")
    billing.create("Paciente Teste", 35000)

    reopened = Database(tmp_path / "nexa.db")
    assert AppointmentRepository(reopened).recent()[0]["patient_name"] == "Paciente Teste"
    assert BillingRepository(reopened).recent()[0]["value_cents"] == 35000
