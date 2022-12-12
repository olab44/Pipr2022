from polynomial_pd.polynomial import Polynomial
import pytest


def test_create_polynomial_typical():
    pol = Polynomial([(1, 3), (0, 4)])
    assert pol._representation == [(1, 3), (0, 4)]
    assert pol._degrees == [1, 0]
    assert pol._coefficients == [3, 4]


def test_create_polynomial_sort():
    pol = Polynomial([(1, 3), (0, 15), (2, 9)])
    assert pol._representation == [(2, 9), (1, 3), (0, 15)]
    assert pol._degrees == [2, 1, 0]
    assert pol._coefficients == [9, 3, 15]


def test_create_polynomial_degree_zero():
    with pytest.raises(ValueError):
        Polynomial([(3, 0), (1, 3), (0, 4)])


def test_create_polynomial_degree_negative():
    with pytest.raises(ValueError):
        Polynomial([(-3, 0), (1, 3), (0, 4)])


def test_create_polynomial_coeff_zero():
    with pytest.raises(ValueError):
        Polynomial([(3, 0), (1, 0), (0, 4)])


def test_create_polynomial_degree_repeat():
    with pytest.raises(ValueError):
        Polynomial([(3, 6), (3, 1), (0, 4)])


def test_polynomial_description():
    pol = Polynomial([(7, 3), (2, 9), (0, 4)])
    assert pol.__str__() == '3x^7+9x^2+4'


def test_polynomial_description_negative():
    pol = Polynomial([(7, 3), (2, -9), (0, 4)])
    assert pol.__str__() == '3x^7-9x^2+4'


def test_polynomial_degree():
    pol = Polynomial([(7, 3), (4, 9), (0, 4)])
    assert pol._degrees == [7, 4, 0]
    assert pol.degree == 7


def test_polynomial_coefficient():
    pol = Polynomial([(7, 3), (4, 9), (0, 4)])
    assert pol.coefficient(4) == 9


def test_polynomial_value():
    pol = Polynomial([(5, 3), (4, 9), (0, 4)])
    assert pol.value(2) == 244


def test_polynomial_value_negative():
    pol = Polynomial([(5, 3), (4, -9), (0, 4)])
    assert pol.value(-1) == -8


def test_polymonial__add__():
    assert Polynomial([(4, 3), (2, 7), (1, 2), (0, 3)]) + ([(4, 7), (1, 10), (0, -2)]) == [(4, 10), (2, 7), (1, 12), (0, 1)]


def test_polynomial__sub__():
    assert Polynomial([(4, 3), (2, 7), (1, 2), (0, 3)]) - Polynomial([(4, 7), (1, 10), (0, -2)]) == Polynomial([(4, -4), (2, 7), (1, -8), (0, 5)])