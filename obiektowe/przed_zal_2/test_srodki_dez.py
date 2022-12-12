from srodki_dez import Storage, Order, NotEnoughStuffError
import pytest


def test_storage_create():
    st = Storage(20, 30, 50, 5)
    assert st.glicerine == 20
    assert st.aloes == 30
    assert st.alcohol == 50
    assert st.conservant == 5


def test_order_create():
    order = Order([('aloes_gel', 3), ('mask', 4), ('desin_gel', 2)])
    assert order.products == {'aloes_gel': 3, 'mask': 4, 'desin_gel': 2} 


def test_products_needs():
    order = Order([('aloes_gel', 3), ('desin_gel', 2), ('mask', 5)])
    assert order.products_needs() == {'alcohol': 3.24, 'glicerine': 0.36, 'aloes': 1.05, 'conservant': 0.25}


def test_checking_avaiability():
    storage = Storage(3, 5, 0, 0)
    order = Order([('aloes_gel', 3), ('desin_gel', 2), ('mask', 5)])
    with pytest.raises(ValueError):
        order.checking_avaiability(storage)
