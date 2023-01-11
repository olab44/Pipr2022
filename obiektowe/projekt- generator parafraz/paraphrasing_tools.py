import requests
from urls import urls


def add_adj_to_noun(noun):
    possible_adj = requests.get(urls['related_adjectives'].format(word=noun)).json()
    if not possible_adj:
        return noun
    adj = possible_adj[0]['word']
    pair = [adj, noun]
    return ' '.join(pair)


def switch_rhymes(word):
    rhymes = requests.get(urls['rhymes_with'].format(word=word)).json()
    if len(rhymes) == 0:
        return word
    rhyme = rhymes[0]['word']
    return f'{rhyme}\n'


def switch_synonims(word):
    synonim = requests.get(urls['means_like'].format(word=word)).json()
    if len(synonim) == 0:
        return word
    return synonim[0]['word']


print(add_adj_to_noun('travel'))
print(switch_rhymes('go'))
print(switch_synonims('hard'))
