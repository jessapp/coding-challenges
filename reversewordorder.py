#Write a function reverse_words() that takes a string message 
# and reverses the order of the words in-place.

def reverse_words(string):

    string_list = string.split(" ")

    first = 0

    last = len(string_list) - 1

    while first < last:
        string_list[first], string_list[last] = string_list[last], string_list[first]

        first += 1
        last +=1

    return " ".join(string_list)