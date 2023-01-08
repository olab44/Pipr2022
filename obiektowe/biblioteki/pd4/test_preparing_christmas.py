from preparing_christmas import ElvesWorking


def test_create_class():
    factory = ElvesWorking('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory._elves == 40
    assert factory._elves_on_l4 == 0
    assert factory._working_elves == 40
    assert factory._file_brav_kids == 'brav_kids.txt'
    assert factory._file_naughty_kids == 'naughty_kids.txt'


def test_read_from_file_naughty():
    naughty_kids = 'naughty_kids.txt'
    factory = ElvesWorking('naughty_kids.txt', 'brav_kids.txt', 40)
    list_naughty = ['Lena Mason\n', 'Ross Fisher\n', 'Gregory Curtis\n',
                    'Jadon Schaefer\n', 'Alessandra Lara\n', 'Liam Cain\n',
                    'Chana Rocha\n']

    assert factory.read_from_file(naughty_kids) == list_naughty


def test_read_from_file_brav():
    brav_kids = 'brav_kids.txt'
    list_brav = ['Sidney Oneal\n', 'Jorden Larsen\n', 'Mikayla Pierce\n',
                 'Simeon Roy\n', 'Kassandra Ferguson\n', 'Rylee Chang\n',
                 'Nick Wiggins\n', 'Hassan Mcconnell\n', 'Eden Harmon\n',
                 'Iyana Henderson\n', 'Johnathon Lutz\n', 'Laurel Savage\n']
    factory = ElvesWorking('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory.read_from_file(brav_kids) == list_brav


def test_time_for_naughty():
    factory = ElvesWorking('naughty_kids.txt', 'brav_kids.txt', 3)
    assert factory.time_of_work_naughty() == 0.5


def test_presents_fot_naughty():
    factory = ElvesWorking('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory.presents_for_naughty() == 7


def test_presents_fot_brav():
    factory = ElvesWorking('naughty_kids.txt', 'brav_kids.txt', 40)
    assert factory.presents_for_brav() == 12
