import requests
from word import Word
from urls import urls
import json


# def get_poetry(author, title):
#     # return requests.get(urls['poetry_lyrics']).json()
#     return requests.get(f'https://poetrydb.org/title/{title}').json()


def get_poetry(title, author):
    if not author:
        return requests.get(f'https://poetrydb.org/title/{title}').json()
    return requests.get(f'https://poetrydb.org/author,title/{author};{title}').json()


class Lyrics:
    def __init__(self, title, author):
        data = get_poetry(title, author)[0]
        self._data = data

    def title(self):
        return self._data['title']

    def author(self):
        return self._data['author']

    def lines(self):
        return self._data['lines']

    def length(self):
        return self._data['linecount']


def read_from_lyrics():
    words = []
    with open('saved_lyrics.txt', 'r') as file:
        for line in file:
            verse = line.split(' ')
            for word in verse:
                word = Word(word)
                # if '\n' in word._name:
                #     words.append(word._name[:-2])
                # else:
                words.append(word._name)
        return words


def write_to_lyrics_json(title, author, file_handle):
    with open('saved_lyrics.txt', 'w') as file_handle:
        data = Lyrics(title, author)
        for verse in data.lines():
            line = f'{verse}\n'
            file_handle.write(line)


# print(get_poetry('To my mother', 'Edgar Allan Poe'))
# print(write_to_lyrics_json('To my mother', 'Edgar Allan Poe', 'saved_lyrics.txt'))
# print(read_from_lyrics())
