from paraphrasing_tools import add_adj_to_noun, switch_rhymes, switch_synonims
from getting_lyrics import read_from_lyrics, write_to_lyrics
from random import choices, choice


words_not_to_change = ['I', 'you', 'he', 'she', 'it', 'we', ',they',
                        'my', 'your', 'his', 'her', 'its', 'our', 'their',
                    ]


# def paraphrase_rhyme():
#     lyrics = read_from_lyrics()
#     new_lyrics = []
#     for word in lyrics:
#         if '\n' in word and word not in words_not_to_change:
#             new_lyrics.append(switch_rhymes(word[:-2]))
#     return new_lyrics


def qualify_rhymes():
    lyrics = read_from_lyrics()
    new_lyrics = []
    for word in lyrics:
        if '\n' in word and word not in words_not_to_change:
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
        n_choice = choice(words_to_change)
        if n_choice not in chosen:
            chosen.append(n_choice)
    return chosen


def qualify_to_paraphrase():
    candidates = read_from_lyrics()
    qualified = []
    for word in candidates:
        if len(word) > 3 and '\n' not in word and word not in words_not_to_change:
            qualified.append(word)
    return qualified


def paraphrase(percentage):
    lyrics = read_from_lyrics()
    chosen = choose_what_paraphrase(percentage)
    # rhymes = qualify_rhymes()
    paraphrased = []
    index = 0
    for word in lyrics:
        if '\n' in word:
            paraphrased.append(switch_rhymes(word[:-2]))
        if word in chosen:
            if index % 2 == 1:
                paraphrased.append(switch_synonims(word))
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
            # if '\n' in word:
            #     file.write(word)
            file.write(f'{word} ')


# print(how_much_paraphrase(40))
# print(qualify_to_paraphrase())
# print(choose_what_paraphrase(40))

# print(read_from_lyrics())
# print(paraphrase_rhyme())
print(write_to_lyrics('Sonnet 2: When forty winters shall besiege thy brow', 'William Shakespeare', 'saved_lyrics.txt'))
print(paraphrase(40))
# print(write_to_new_lyrics('new_lyrics.txt', 40))

