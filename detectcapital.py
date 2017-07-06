"""Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way."""

def detect_capital(word):

    if word == word.upper():
        return True

    elif word == word.lower():
        return True

    elif word[0] == word[0].upper():
        for letter in word[1:]:
            if letter != letter.lower():
                return False
        return True

    return False


print detect_capital("USA")
print detect_capital("FlaG")
print detect_capital("caT")