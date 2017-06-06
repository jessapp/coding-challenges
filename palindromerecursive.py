# Check if a string is a palindrome recursively

def recursive_palindrome(string):

    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return recursive_palindrome(string[1:-1])
    else:
        return False

print recursive_palindrome("aibohphobia")
print recursive_palindrome("hello")
