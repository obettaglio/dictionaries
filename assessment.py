"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    words = phrase.split(" ")

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_price = {"Watermelon": 2.95,
                   "Cantaloupe": 2.50,
                   "Musk": 3.25,
                   "Christmas": 14.25}

    return melon_price.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    word_length_dict = {}

    for word in words:
        length = len(word)
        if length in word_length_dict:
            word_length_dict[length].append(word)
            word_length_dict[length].sort()         # sort words in each list
        else:
            word_length_dict[length] = [word]

    word_length_list = [(key, value) for key, value in word_length_dict.items()]

    return sorted(word_length_list)                 # sort tuples by number


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {"sir": "matey",
                         "hotel": "fleabag inn",
                         "student": "swabbie",
                         "man": "matey",
                         "professor": "foul blaggart",
                         "restaurant": "galley",
                         "your": "yer",
                         "excuse": "arr",
                         "students": "swabbies",
                         "are": "be",
                         "restroom": "head",
                         "my": "me",
                         "is": "be"}

    pirate_phrase = []

    words = phrase.split(" ")

    for word in words:
        if word in english_to_pirate:
            word = english_to_pirate[word]
        pirate_phrase.append(word)

    pirate_phrase = " ".join(pirate_phrase)

    return pirate_phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # for every word, create dictionary of first letter: [word]
    # set new first letter to current word[-1]
    # lookup will be by first letter
    # value will be list of words starting with first letter

    first_word = names[0]                           # set first word entered
    first_letter_dictionary = {}                    # dictionary to hold word:first_letter

    for word in names:                              # iterate through words entered
        if word[0] in first_letter_dictionary:
            first_letter_dictionary[word[0]] += [word]
        else:
            first_letter_dictionary[word[0]] = [word]     # add {word: first_letter} to dictionary

    game_list = []                                  # list to hold final product
    game_list.append(first_word)                    # add first word
    current_word = game_list[-1]                    # current_word = last word in game_list
    new_first_letter = current_word[-1]             # new_first_letter = last character of current_word

    game_incomplete = True

    while game_incomplete:                          # while entries exist with key new_first_letter
        try:
            new_word_list = first_letter_dictionary[new_first_letter]
        except:
            return game_list

        for word in new_word_list:
            if word in game_list:                   # if word in list has been used in game
                used_word_index = new_word_list.index(word)
                new_word_list.pop(used_word_index)  # remove word from list

        if not new_word_list:                       # if list of unused possible words is empty
            game_incomplete = False                 # break loop

        else:                                       # if possible words remain
            new_word = new_word_list[0]             # set new word to first word in possibility list
            new_first_letter = new_word[-1]

            game_list.append(new_word)              # add new word to game_list

    return game_list


#####################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
