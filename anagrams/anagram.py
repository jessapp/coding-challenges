"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""

def make_dictionary(words):
    """Make a dict where the key is letter and the value is a list of words
    with the same letters"""

    anagrams = {}

    for word in words:
        sort_word = ''.join(sorted(word))
        anagrams.setdefault(sort_word, []).append(word)

    return anagrams


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    anagram_dict = make_dictionary(wordlist)

    most_anagrams = 0
    anagram_lst = None

    for anagram, lst in anagram_dict.items():
        if len(lst) > most_anagrams:
            most_anagrams = len(lst)
            anagram_lst = lst

    return sorted(anagram_lst)[0]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
