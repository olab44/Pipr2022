import requests
from word import Word
from urls import urls


def get_poetry(title):
    # return requests.get(urls['poetry_lyrics']).json()
    return requests.get(f'https://poetrydb.org/title/{title}/lines').json()


def verses(title):
    poem = get_poetry(title)
    lyrics = poem[0]['lines']
    return [line for line in lyrics]


def read_from_lyrics():
    words = []
    with open('saved_lyrics.json', 'r') as file:
        for line in file:
            verse = line.split(' ')
            for word in verse:
                word = Word(word)
                # if '\n' in word._name:
                #     words.append(word._name[:-2])
                # else:
                words.append(word._name)
        return words


def write_to_lyrics_json(title, file):
    with open('saved_lyrics.json', 'w') as file:
        data = verses(title)
        for verse in data:
            line = f'{verse}\n'
            file.write(line)


# print(get_poetry('Ozymandias'))
# print(verses('Ozymandias'))
# print(write_to_lyrics_json('Ozymandias', 'lyrics.txt'))
# print(read_from_lyrics())
