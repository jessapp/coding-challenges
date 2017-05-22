"""Create a function which implements autocomplete given a certain set of words"""

def autocomplete(words, first_letter):

    word_dict = {}

    for word in words:
        if word[0] not in word_dict:
            word_dict[word[0]] = [word]
        else:
            word_dict[word[0]].append(word)

    if first_letter in word_dict:
        for word in word_dict[first_letter]:
            print word
    else:
        print "No autocomplete possible for this word"

