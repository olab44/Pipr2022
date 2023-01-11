from changing_rhymes import switch_rhyme
from adding_adjectives import add_adj_to_noun
from changing_synonims import choose_and_switch_synonims
from getting_lyrics import read_from_lyrics
from random import choices, choice


words_not_to_change = ['I', 'you', 'he', 'she', 'it', 'we', ',they',
                        'my', 'your', 'his', 'her', 'its', 'our', 'their',
                        ]


def paraphrase_rhyme():
    lyrics = read_from_lyrics()
    new_lyrics = []
    for word in lyrics:
        if '\n' in word:
            new_lyrics.append(switch_rhyme(word[:-2]))
        else:
            new_lyrics.append(word)
    return new_lyrics


def how_much_paraphrase(percentage):
    lyrics = read_from_lyrics()
    amount_to_paraphrase = int(percentage * len(lyrics) / 100)
    return amount_to_paraphrase


def choose_what_paraphrase(percentage):
    words_to_change = qualify_to_paraphrase()
    amount = how_much_paraphrase(percentage)
    chosen = []
    for number in range(amount + 1):
        chosen.append(choice(words_to_change))
    return chosen


def qualify_to_paraphrase():
    candidates = read_from_lyrics()
    qualified = []
    for word in candidates:
        if len(word) > 3 and '\n' not in word and word not in words_not_to_change:
            qualified.append(word)
    return qualified


def qualify_to_paraphrase_rhyme():
    candidates = read_from_lyrics()
    qualified = []
    for word in candidates:
        if '\n' in word and word not in words_not_to_change:
            qualified.append(word)
    return qualified


def add_index(percentage):
    chosen = choose_what_paraphrase(percentage)
    list_of_pairs = []
    index = 0
    for word in chosen:
        pair = word, index
        list_of_pairs.append(pair)
        index +=1
    return list_of_pairs


def paraphrase(percentage):
    lyrics = read_from_lyrics()
    chosen = choose_what_paraphrase(percentage)
    paraphrased = []
    for word in lyrics:
        if word in chosen:
            index = 0
            for word in chosen:
                if index % 2 == 1:
                    paraphrased.append(choose_and_switch_synonims(word))
                    index += 1
                if index % 2 == 0:
                    paraphrased.append(add_adj_to_noun(word))
                    index += 1
        else:
            paraphrased.append(word)
    return paraphrased


def write_to_new_lyrics(file, percentage):
    lyrics = paraphrase(percentage)
    with open('new_lyrics.txt', 'w') as file:
        for word in lyrics:
            file.write(f'{word} ')


# print(paraphrase_syn())
# print(how_much_paraphrase(40))
# print(qualify_to_paraphrase())
# print(choose_what_paraphrase(40))
print(paraphrase(40))
# print(add_index(40))
# print(paraphrase_rhyme())
# print(write_to_new_lyrics('new_lyrics.txt'))

