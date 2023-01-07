import requests
from word import Word


def get_synonims(word):
    all_synonims = requests.get(f'https://api.datamuse.com/words?ml={word}').json()
    return all_synonims[:10]


class Synonim:
    def __init__(self, word):
        data = get_synonims(word)[0]
        self._word = word
        self._data = data

    def name(self):
        return self._data['word']

    def score(self):
        return self._data['score']

    def tags(self):
        return self._data['tags']

    def part_of_speech(self):
        if len(self.tags()) == 1:
            return self.tags()[0]
        else:
            return self.tags()[1]


def choose_and_switch_synonims(word):
    synonim = get_synonims(word)[0]
    if not synonim:
        return word
    else:
        return synonim['word']
        # return syn.name()


# def switch_synonims(word):
#     synonim = Synonim(word)
#     return synonim.name()


# print(get_synonims('devil'))
print(choose_and_switch_synonims('devil'))
# print(switch_synonims('big'))
