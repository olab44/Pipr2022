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
    word = phrase.split()
    letter, amount = frequency
    for word in phrase:
        amount_letters = counter(word)
        if letter not in amount_letters or amount_letters[letter] < amount:
            new_phrase.append(word)
    return new_phrase


print(word_frequency("Alice in wonderland went into a deep coma.", ("e", 2)))
