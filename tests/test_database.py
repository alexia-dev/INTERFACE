from core.database import Database
from repositories.appointments import AppointmentRepository
from repositories.billing import BillingRepository


def test_local_data_persists(tmp_path):
    database = Database(tmp_path / "nexa.db")
    appointments = AppointmentRepository(database)
    billing = BillingRepository(database)

    appointment_id = appointments.create("Paciente Teste", "Consulta")
    billing_id = billing.create("Paciente Teste", 35000)

    reopened = Database(tmp_path / "nexa.db")
    assert AppointmentRepository(reopened).recent()[0]["id"] == appointment_id
    assert BillingRepository(reopened).recent()[0]["id"] == billing_id

    AppointmentRepository(reopened).delete(appointment_id)
    BillingRepository(reopened).delete(billing_id)

    assert AppointmentRepository(reopened).recent() == []
    assert BillingRepository(reopened).recent() == []
