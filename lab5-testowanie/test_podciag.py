import podciag


def test_max_progression_typical():
    assert podciag.max_progression(2, [4, 2, 6, 7]) == [7, 6]


def test_max_progression_empty():
    assert podciag.max_progression(2, []) == 'the list is empty'


def test_max_progression_too_long():
    assert podciag.max_progression(5, [4, 2, 6, 7]) == 'the list is too short'
