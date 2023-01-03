
class Word:
    def __init__(self, name):
        self._name = name
        self._length = len(name)

    def name(self):
        return self._name

    def length(self):
        return self._length
