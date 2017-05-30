# Reverse a string

def reverse_string(string):

    letters = list(string)

    first = 0

    last = len(letters) - 1

    while first < last:

        letters[first], letters[last] = letters[last], letters[first]
        first += 1
        last -= 1

    return ''.join(letters)

print reverse_string("This is a string")

def reverse_words(string):

    words = string.split(" ")

    new_words = []

    for word in words:
        letters = list(word)

        first = 0
        last = len(letters) - 1

        while first < last:
            letters[first], letters[last] = letters[last], letters[first]
            first += 1
            last -= 1

        new_words.append(''.join(letters))

    return ' '.join(new_words)

print reverse_words("This is a string")