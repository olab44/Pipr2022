from changing_synonims import get_synonims, choose_synonim, switch_synonims
from word import Word


def test_get_synonims():
    word = 'big'
    top_ten_synonims = [
        {"word": "gigantic", "score": 40020060, "tags": ["syn", "adj", "results_type:primary_rel"]},
        {"word": "humongous", "score": 40020060, "tags": ["syn", "adj"]},
        {"word": "huge", "score": 40020059, "tags": ["syn", "adj"]},
        {"word": "gargantuan", "score": 40020056, "tags": ["syn", "adj"]},
        {"word": "immense", "score": 40020056, "tags": ["syn", "n", "adj"]},
        {"word": "colossal", "score": 40020050, "tags": ["syn", "adj"]},
        {"word": "prodigious", "score": 40020041, "tags": ["syn", "adj"]},
        {"word": "massive", "score": 40020022, "tags": ["syn", "n", "adj"]},
        {"word": "larger-than-life", "score": 40019997, "tags": ["syn", "adj"]},
        {"word": "oversized", "score": 40019939, "tags": ["syn", "adj"]}
    ]
    assert get_synonims(word) == top_ten_synonims


def test_choose_synonim():
    word = Word('big')
    assert choose_synonim(word) == 'gigantic'


def test_switch_synonim():
    word = 'nice'
    assert switch_synonims(word) == 'pleasant'

