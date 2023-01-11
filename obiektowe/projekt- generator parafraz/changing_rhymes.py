import requests

url = 'https://api.datamuse.com/words?rel_rhy={word}&ml={word}'
url1 = 'https://api.datamuse.com/words?rel_rhy={word}'


def get_rhyming_words(word):
    return requests.get(f'https://api.datamuse.com/words?rel_rhy={word}&ml={word}').json()


# def choose_rhyming_word(word):
#     rhyme = Rhyme(get_rhyming_words(word)[0])
#     return rhyme.name()


def switch_rhyme(word):
    rhymes = get_rhyming_words(word)
    if len(rhymes) == 0:
        return word
    rhyme = rhymes[0]['word']
    return f'{rhyme}\n'


# print(get_rhyming_words('go'))
# print(choose_rhyming_word('go'))
# print(switch_rhyme('go'))
