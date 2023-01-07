import requests
from word import Word
# from getting_lyrics import read_from_lyrics


def get_adjective(noun):
    possible = requests.get(f'https://api.datamuse.com/words?rel_jjb={noun}').json()
    if not possible:
        return None
    adj = possible[0]['word']
    return adj


def add_adj_to_noun(noun):
    adj = get_adjective(noun)
    pair = [adj, noun]
    if not adj:
        return noun
    return ' '.join(pair)


print(get_adjective('ice'))
print(add_adj_to_noun('ice'))
