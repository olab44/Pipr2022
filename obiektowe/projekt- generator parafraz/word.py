
class Word:
    def __init__(self, name):
        self._name = name
        self._length = len(name)

    def name(self):
        return self._name

    def length(self):
        return self._length

    def __str__(self):
        return f'{self._name}'


class Pair:
    def __init__(self, adj, noun):
        self._adj = adj
        self._noun = noun

    def adj(self):
        return self._adj

    def noun(self):
        return self._noun


class Synonim:
    def __init__(self, data):
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


class Rhyme:
    def __init__(self, data):
        self._data = data

    def name(self):
        return self._data['word']

    def score(self):
        return self._data['score']

    def syllables(self):
        return self._data['numSyllables']

    def __str__(self):
        return f'{self.name()}'
