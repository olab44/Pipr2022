from preparing_christmas import Village, read_from_file, FormatTime
import pytest


def test_create_class():
    village = Village(10, 20, 40)
    assert village._elves == 40
    assert village._elves_on_l4 == 0
    assert village._working_elves == 40
    assert village._am_presents == 20
    assert village._am_sticks == 10


def test_village_error():
    with pytest.raises(ValueError):
        Village(10, 20, 40, 39)


def test_time_for_naughty():
    village = Village(4, 4, 4)
    assert village.time_for_sticks(7, 4) == 1


def test_time_for_naughty_long():
    village = Village(4, 7, 40)
    assert village.time_for_sticks(28, 2) == 7


def test_time_for_presents():
    village = Village(4, 7, 40)
    assert village.time_for_presents(12, 5) == 6


def test_time_for_presents_optimistic():
    village = Village(4, 7, 40)
    assert village.time_for_presents(10, 40) == 1


def test_count_total_time_odd():
    village = Village(4, 7, 5)
    assert village.count_total_time_odd() == 4


def test_count_total_time_odd_optimistic():
    village = Village(4, 7, 101)
    assert village.count_total_time_odd() == 1


def test_count_total_time_even():
    village = Village(8, 7, 6)
    assert village.count_total_time_even() == 3


def test_count_total_time_even_2():
    village = Village(13, 7, 4)
    assert village.count_total_time_even() == 5.5


def test_count_total_time():
    village = Village(13, 7, 10)
    assert village.count_total_time_even() == 2.5


def test_free_elves():
    village = Village(3, 6, 8)
    assert village.free_elves(7, 7) == 4
    assert village.free_elves(7, 5) == 2
    assert village.free_elves(10, 13) == 4
    assert village.free_elves(10, 12) == 4
    assert village.free_elves(7, 6) == 4


def test_format_time_int():
    time = FormatTime(540)
    assert time.days() == 22
    assert time.hours() == 12
    assert time.minutes() == 0


def test_format_time_fractorial():
    time = FormatTime(5.5)
    assert time.days() == 0
    assert time.hours() == 5
    assert time.minutes() == 30


def test_format_time_str():
    time = FormatTime(540)
    assert time.__str__() == '22 days, 12 hours and 0 minutes'


