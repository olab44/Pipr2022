import requests
from word import Rhyme, Word

url = 'https://api.datamuse.com/words?rel_rhy={word}&ml={word}'
url1 = 'https://api.datamuse.com/words?rel_rhy={word}'


def get_rhyming_words(word):
    return requests.get(f'https://api.datamuse.com/words?rel_rhy={word}&ml={word}').json()


def choose_rhyming_word(word):
    rhyme = Rhyme(get_rhyming_words(word)[0])
    return rhyme.name()


def switch_rhyme(word):
    word = Word(choose_rhyming_word(word))
    return word


word = Word('go')
# print(get_rhyming_words('go'))
# print(choose_rhyming_word('go'))
# print(switch_rhyme('go'))
