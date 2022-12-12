from item import Item, Container
import pytest


def test_item_create():
    notebook = Item(1)
    assert notebook.mass == 1


def test_item_create_negative():
    with pytest.raises(ValueError):
        Item(-4)


def test_container_create():
    box = Container(20, 30)
    assert box.lift_cap == 30


def test_container_create_negative():
    with pytest.raises(ValueError):
        Container(20, -3)


def test_put_item():
    box = Container(20, 30)
    thing = Item(20)
    box.put_item(thing)
    assert box.items_in_box() == [Item(20)]
    thing2 = Item(10)
    box.put_item(thing2)
    assert box.items_in_box() == [Item(20), Item(10)]
