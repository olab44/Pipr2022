from word import Word, Synonim


def test_create_word():
    word = Word('oxygen')
    assert word.name() == 'oxygen'
    assert word.length() == 6


def test_synonim():
    data = {"word": "horizontal",
            "score": 40026149,
            "tags": ["syn", "n", "results_type:primary_rel"]}
    synonim = Synonim(data)
    assert synonim.name() == 'horizontal'
    assert synonim.score() == 40026149
    assert synonim.tags() == ["syn","n","results_type:primary_rel"]
    assert synonim.part_of_speech() == 'n'