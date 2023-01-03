from word import Word


def test_create_word():
    word = Word('oxygen')
    assert word.name() == 'oxygen'
    assert word.length() == 6
