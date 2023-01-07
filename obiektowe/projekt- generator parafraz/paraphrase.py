from changing_rhymes import switch_rhyme
from adding_adjectives import add_adj_to_noun
from changing_synonims import choose_and_switch_synonims
from getting_lyrics import read_from_lyrics


words_not_to_change = ['I', 'you', 'he', 'she', 'it', 'we', ',they',
                        'my', 'your', 'his', 'her', 'its', 'our', 'their',
                        ]


def paraphrase_adj():
    lyrics = read_from_lyrics()
    new_lyrics = []
    max_amount = len(lyrics)
    # amount = int(percentage * max_amount // 100)
    # return amount
    for word in lyrics:
        if len(word) > 3 and word not in words_not_to_change:
            pair = add_adj_to_noun(word)
            new_lyrics.append(pair)
        else:
            new_lyrics.append(word)
    return new_lyrics


def paraphrase_syn():
    lyrics = paraphrase_adj()
    new_lyrics = []
    for word in lyrics:
        if len(word) > 3 and word not in words_not_to_change:
            new_lyrics.append(choose_and_switch_synonims(word))
        else:
            new_lyrics.append(word)
    return new_lyrics


def write_to_new_lyrics(file):
    lyrics = paraphrase_syn()
    with open('new_lyrics.txt', 'w') as file:
        for word in lyrics:
            file.write(f'{word} ')


# print(paraphrase())
print(write_to_new_lyrics('new_lyrics.txt'))
