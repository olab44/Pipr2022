import requests


def get_poetry(title):
    return requests.get(f'https://poetrydb.org/title/{title}/lines').json()


def verses(title):
    poem = get_poetry(title)
    lyrics = poem[0]['lines']
    return [line for line in lyrics]


def write_to_lyrics(title, file):
    with open('saved_lyrics.txt', 'w') as file:
        data = verses(title)
        for verse in data:
            line = f'{verse}\n'
            file.write(line)


print(verses('Ozymandias'))
print(write_to_lyrics('Ozymandias', 'lyrics.txt'))
