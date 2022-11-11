def counter(word):
    word_counter = {}
    for letter in word:
        if letter not in word_counter:
            word_counter[letter] = 1
        else:
            word_counter[letter] += 1
    return word_counter


# print(counter('tablet'))


def word_frequency(phrase, frequency):
    new_phrase = []
    words = phrase.split()
    letter, amount = frequency
    for word in words:
        amount_letters = counter(word)
        if letter not in amount_letters or amount_letters[letter] < amount:
            new_phrase.append(word)
    return (new_phrase)


print(word_frequency("Alice in wonderland went into a deep coma.", ("e", 2)))


def random_word_frequency(phrase, amount_of_krotki):
    amount_of_krotki = [("a", 2), ("l", 3)]
    words = phrase.split()
    for krotka in amount_of_krotki:
        letter, amount = krotka
        for word in words:
                letters = counter(word)
                if letter not in letters or letters[letter] < amount:
                    pass
                else:
                    words.remove(word)
    return words


print(random_word_frequency("I literally can't deal with this drama right now.", [("a", 2), ("l", 3)]))
