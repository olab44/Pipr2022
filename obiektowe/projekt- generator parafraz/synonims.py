import requests
from getting_lyrics import read_from_lyrics
from word import Synonim, Word


def get_synonims(word):
    all_synonims = requests.get(f'https://api.datamuse.com/words?ml={word}').json()
    return all_synonims[:10]


def choose_synonim(word):
    synonim = Synonim(get_synonims(word)[0])
    return synonim.name()


def switch_synonims(word):
    word = Word(choose_synonim(word))
    return word.name()


# print(get_synonims('big'))
print(choose_synonim('number'))
print(switch_synonims('big'))
