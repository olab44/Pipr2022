from planets import Planet
from planets import distance
import pytest


def test_create_mercury():
    mercury = Planet('mercury', 0, (30, 50, 40))
    assert mercury.name() == 'mercury'
    assert mercury.moon_amount() == 0
    assert mercury.location() == (30, 50, 40)


def test_create_empty_name():
    with pytest.raises(ValueError):
        Planet('', 0, (30, 50, 40))


def test_create_moon_amount_negative():
    with pytest.raises(ValueError):
        Planet('mercury', -3, (30, 50, 50))


def test_create_location_less_than_three_variables():
    with pytest.raises(ValueError):
        Planet('mercury', 3, (30, 50))


def test_set_name():
    mercury = Planet('mercury', 0, (30, 50, 40))
    mercury.set_name('mars')
    assert mercury.name() == 'mars'


def test_set_empty_name():
    mercury = Planet('mercury', 0, (30, 50, 40))
    with pytest.raises(ValueError):
        mercury.set_name('')


def test_introduce():
    mercury = Planet('mercury', 5, (30, 50, 40))
    assert mercury.info() == 'mercury has 5 moons, his location is (30, 50, 40)'


def test_introduce_as_str():
    mercury = Planet('mercury', 0, (30, 50, 40))
    assert str(mercury) == mercury.info()


def test_set_moon_amount():
    mercury = Planet('mercury', 0, (30, 50, 40))
    mercury.set_moon_amount(4)
    assert mercury.moon_amount() == 4


def test_set_moon_amount_negative():
    mercury = Planet('mercury', 0, (30, 50, 40))
    with pytest.raises(ValueError):
        mercury.set_moon_amount(-5)


def test_set_location():
    mercury = Planet('mercury', 0, (30, 50, 40))
    mercury.set_location(40, 0, 0)
    assert mercury.location() == (40, 0, 0)


def test_set_location_missing():
    mercury = Planet('mercury', 5, (30, 50, 40))
    with pytest.raises(TypeError):
        mercury.set_location(50, 40)


def test_set_location_negative():
    mercury = Planet('mercury', 5, (30, 50, 40))
    with pytest.raises(ValueError):
        mercury.set_location(-40, 50, 60)


def test_distance():
    mercury = Planet('mercury', 0, (11, 5, 0))
    venus = Planet('venus', 5, (8, 1, 0))
    assert distance(mercury, venus) == 5
