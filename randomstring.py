# Generate a random string which can be separted into several "words" by spaces. 
# Split the string into a list, an return longest word with unique characters 

import random
import string

def generate_random_string():

    chars = string.ascii_uppercase

    final_words = []

    for i in range(10):

        num = random.randint(1, 10)

        word = ''.join(random.sample(chars * 6, num))

        final_words.append(word)

    return ' '.join(final_words)

def find_longest_unique(rand_str):

    unique_words = []

    for word in rand_str.split():
        chars = []

        for char in word:
            if char not in chars:
                chars.append(char)

        if len(chars) == len(word):
            unique_words.append(word)

    current_longest = None
    
    longest_length = 0        

    for unique_word in unique_words:
        if len(unique_word) > longest_length:
            longest_length = len(unique_word)
            current_longest = unique_word

    return current_longest

rand_str = generate_random_string()
print rand_str
print find_longest_unique(rand_str)
