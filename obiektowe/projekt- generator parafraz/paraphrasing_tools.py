import requests
from urls import urls


def add_adj_to_noun(noun):
    possible_adj = requests.get(urls['related_adjectives'].format(word=noun)).json()
    if len(possible_adj) == 0:
        return noun
    adj = possible_adj[0]['word']
    pair = [adj, noun]
    return ' '.join(pair)


def switch_rhymes(word):
    rhymes = requests.get(urls['rhymes_with'].format(word=word)).json()
    if len(rhymes) == 0:
        return f'{word}\n'
    rhyme = rhymes[0]['word']
    return f'{rhyme}\n'


def switch_synonims(word):
    synonim = requests.get(urls['means_like'].format(word=word)).json()
    if len(synonim) == 0:
        return word
    return synonim[0]['word']


# print(add_adj_to_noun('from'))
# print(switch_synonims('from'))