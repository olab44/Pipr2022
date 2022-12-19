from casino import Casino, Player, EmptyNameError
import pytest


def test_player_create():
    player = Player('jane', [3, 3, 3, 3])
    assert player.name == 'jane'
    assert player.dices == [3, 3, 3, 3]
    assert player.result == 18


def test_player_create_empty_name():
    with pytest.raises(EmptyNameError):
        Player('')


def test_create_casino():
    casino = Casino([
        Player('jurek'), Player('mary'), Player('jane')
    ])
    assert casino.list_of_players == [Player('jurek'), Player('mary'), Player('jane')]


def test_add_player():
    casino = Casino([Player('james')])
    assert casino.list_of_players == [Player('james')]
    casino.add_player(Player('jonas'))
    assert casino.list_of_players == [Player('james'), Player('jonas')]


def test_remove_player():
    casino = Casino([Player('james'), Player('jonas')])
    casino.remove_player(Player('jonas'))
    assert casino.list_of_players == [Player('james')]


def test_throw_dice_the_same(monkeypatch):
    def fours(a, b):
        return 1
    casino = Casino([Player('james')])
    monkeypatch.setattr('casino.randint', fours)
    assert casino.throw_dice() == [1, 1, 1, 1]


def test_throw_dice_different_numbers(monkeypatch):
    def fours(a):
        return [3, 4, 5, 6]
    casino = Casino([Player('john')])
    monkeypatch.setattr('casino.Casino.throw_dice', fours)
    assert casino.throw_dice() == [3, 4, 5, 6]


def test_throw_dice_different():
    # checking if throw_dice returns list of four items, each in range <1, 6>
    casino = Casino([Player('john')])
    assert len(casino.throw_dice()) == 4
    for item in casino.throw_dice():
        assert casino.throw_dice()[0] in range(1, 7)


def test_game(monkeypatch):
    def fours(a):
        return [3, 3, 3, 6]
    casino = Casino([Player('john'), Player('jane'), Player('mark')])
    monkeypatch.setattr('casino.Casino.throw_dice', fours)
    assert casino.game() == [('john', 12), ('jane', 12), ('mark', 12)]


def test_game_harder_version(monkeypatch):
    def three_of_kind(a):
        return [3, 3, 3, 6]

    def four_of_kind(b):
        return [1, 1, 1, 1]

    def pair(c):
        return [6, 6, 2, 4]

    casino = Casino([Player('john'), Player('jane'), Player('mark')])
    # monkeypatch.setattr('casino.Casino.game', [])
    assert casino.game() == [('john', 12), ('jane', 18), ('mark', 10)]


def test_game_results_with_winner(monkeypatch):
    def this_game(a):
        return [('john', 12), ('jane', 18), ('mark', 10)]
    casino = Casino([Player('john'), Player('jane'), Player('mark')])
    monkeypatch.setattr('casino.Casino.game', this_game)
    assert casino.result_of_game() == 'jane won'


def test_game_results_draw(monkeypatch):
    def this_game(a):
        return [('john', 8), ('jane', 10), ('mark', 10)]
    casino = Casino([Player('john'), Player('jane'), Player('mark')])
    monkeypatch.setattr('casino.Casino.game', this_game)
    assert casino.result_of_game() == 'the game is unresolved'


def test_player_results_four_of_kind():
    player = Player('james', [4, 4, 4, 4])
    assert player.result == 24


def test_player_results_all_non_consecutive():
    player = Player('james', [5, 3, 3, 1])
    assert player.result == 15


def test_player_results_all_consecutive():
    player = Player('james', [4, 6, 6, 2])
    assert player.result == 20


def test_player_results_three_of_kind():
    player = Player('james', [3, 3, 3, 1])
    assert player.result == 13


def test_player_results_pair_1():
    player = Player('jurek', [4, 4, 3, 1])
    assert player.result == 8


def test_player_results_pair_2():
    player = Player('jurek', [4, 3, 3, 1])
    assert player.result == 6


def test_player_results_pair_3():
    player = Player('jurek', [6, 4, 3, 3])
    assert player.result == 6


def test_player_results_choosing_better():
    player = Player('jurek', [6, 6, 3, 3])
    assert player.result == 12
