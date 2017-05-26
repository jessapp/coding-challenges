# Make a trie given a list of words 

def make_trie(words):
    """Creates a trie based on a list of words"""

    root = {}
    end = "*"

    for word in words:
        print word

        current_dict = root

        for letter in word:

            current_dict = current_dict.setdefault(letter, {})

        current_dict[end] = {}

    return root


def in_trie(trie, word):
    """Checks to see if a word is in a trie"""

    current_dict = trie

    end = "*"

    for letter in word:

        if letter in current_dict:
            current_dict = current_dict[letter]

            if end in current_dict:
                return True

    return False
=
print in_trie(make_trie(["nap", "nape", "naples", "null"]), "apple")
print in_trie(make_trie(['foo', 'bar', 'baz', 'barz']), 'baz')
