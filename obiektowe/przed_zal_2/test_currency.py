from currency import Price
import pytest


def test_create_price_gr():
    price = Price(30, 'gr')
    assert price.value == 30
    assert price.currency == 'gr'


def test_price_negative():
    with pytest.raises(ValueError):
        Price(-3, 'gr')


def test_price_wrong_currency():
    with pytest.raises(ValueError):
        Price(-3, 'dollar')


def test_price_empty():
    price = Price()
    assert price.value == 0
    assert price.currency == 'gr'


def test__str__():
    price = Price(40, 'eurocent')
    assert price.__str__() == 'the price is 40 eurocent'


def test__add__():
    assert Price(260 + 40) == Price(300)


def test__add__negative():
    with pytest.raises(ValueError):
        Price(240)
        Price(-40)


def test__sub__():
    assert Price(260 - 40) == Price(220)


def test__sub__negative():
    with pytest.raises(ValueError):
        Price(240)
        Price(-40)


def test__mul__():
    assert 3 * Price(40) == Price(120)


def test__rmul__():
    assert Price(40) * 3 == Price(120)
