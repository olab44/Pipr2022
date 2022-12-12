from respiratory import Hospital, Patient, WhereToGo
from respiratory import EmptyCityError, OutOfRangeCityError


def test_create_hospital():
    hospital = Hospital('Warszawa', 100, 30, 300, 120)
    assert hospital.city == 'Warszawa'
    assert hospital.covid_beds == 100
    assert hospital.resp_cov == 30
    assert hospital.non_covid_beds == 300
    assert hospital.oiom_n_cov == 120


def test_create_patient():
    patient = Patient('Warszawa', 'negative', 'critical')
    assert patient.city == 'Warszawa'
    assert patient.covid == 'negative'
    assert patient.status == 'critical'


def test_is_critical():
    patient = Patient('Warszawa', 'negative', 'critical')
    assert patient.is_critical() is True


def test_has_covid():
    patient = Patient('Warszawa', 'negative', 'critical')
    assert patient.has_covid() is False


