#String Compression
#Compress a string with counts of repeated characters. For example, aaabbc becomes a3b2c1
#If the compressed string is longer than the original, return the original 

def compress_string(string):

    char_counts = {}

    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1

    new_string = ""

    for letter, count in char_counts.items():
        new_string = new_string + letter + str(count)

    if len(new_string) < len(string):
        return new_string
    else:
        return string

print compress_string("aaabbbcccjjjshhh")
print compress_string("aaaaaaaaaaa")