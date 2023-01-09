from preparing_christmas import Factory, read_from_file


def test_create_class():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory._elves == 40
    assert factory._elves_on_l4 == 0
    assert factory._working_elves == 40
    assert factory._file_brav_kids == 'brav_kids.txt'
    assert factory._file_naughty_kids == 'naughty_kids.txt'


def test_read_from_file_naughty():
    naughty_kids = 'naughty_kids.txt'
    list_naughty = ['Lena Mason\n', 'Ross Fisher\n', 'Gregory Curtis\n',
                    'Jadon Schaefer\n', 'Alessandra Lara\n', 'Liam Cain\n',
                    'Chana Rocha\n']

    assert read_from_file(naughty_kids) == list_naughty


def test_read_from_file_brav():
    brav_kids = 'brav_kids.txt'
    list_brav = ['Sidney Oneal\n', 'Jorden Larsen\n', 'Mikayla Pierce\n',
                 'Simeon Roy\n', 'Kassandra Ferguson\n', 'Rylee Chang\n',
                 'Nick Wiggins\n', 'Hassan Mcconnell\n', 'Eden Harmon\n',
                 'Iyana Henderson\n', 'Johnathon Lutz\n', 'Laurel Savage\n']
    assert read_from_file(brav_kids) == list_brav


def test_time_for_naughty():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 4)
    assert factory.time_for_naughty(7, 4) == 1


def test_presents_fot_naughty():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory.presents_for_naughty() == 7


def test_presents_for_brav():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory.presents_for_brav() == 12


def test_time_for_brav_optimistic():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory.time_for_brav(12, 40) == 1


def test_time_for_brav_typical():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 4)
    assert factory.time_for_brav(12, 4) == 6


def test_count_total_time_np():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 5)
    assert factory.count_total_time() == 6


def test_count_total_time_np_2():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 5)
    assert factory.count_total_time() == 5.5


def test_count_total_time_np_3():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 101)
    assert factory.count_total_time_odd() == 1


def test_count_total_time_parz():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 6)
    assert factory.count_total_time_even() == 3.5


def test_free_elves():
    factory = Factory('naughty_kids.txt', 'brav_kids.txt', 8)
    assert factory.free_elves(7, 7) == 4
    assert factory.free_elves(7, 5) == 2
    assert factory.free_elves(10, 13) == 4
    assert factory.free_elves(10, 12) == 4
