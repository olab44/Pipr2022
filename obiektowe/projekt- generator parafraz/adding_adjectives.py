import requests
from getting_lyrics import read_from_lyrics


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


# def adding_adjective():
#     base = read_from_lyrics()
#     paraphrased = []
#     for word in base:
#         if len(word) > 3:
#             pair = add_adj_to_noun(word)
#             paraphrased.append(pair)
#             if not pair:
#                 paraphrased.append(word)
#         else:
#             paraphrased.append(word)
#     return paraphrased


# print(adding_adjective())
# print(get_adjective('ice'))
print(add_adj_to_noun('ice'))
