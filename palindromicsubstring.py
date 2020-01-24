#Given a string, find the longest substring which is palindrome. For example, if the
#given string is 'forgeeksskeegfor' the output should be 'geeksskeeg'

def longest_subsequence(input_str):

    # base case - the whole string is a palindrome

    if input_str == input_str[::-1]:
        return input_str

    palindromes = []

    for i in range(len(input_str)):
        print "i", i
        for j in range(0, i):
            print "j", j
            substring = input_str[j:i + 1]
            print "substring", substring

            if substring == substring[::-1]:
                palindromes.append(substring)

    base_count = 0

    longest_pal = None

    for word in palindromes:
        if len(word) > base_count:
            base_count = len(word)
            longest_pal = word

    return longest_pal



print longest_subsequence("forgeeksskeegfor")


# Dynamic programming solution:

class Solution:   
    def get_longest_pal(self, s, left, right):
        while left >= 0 and right < len(s) and s[right] == s[left]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # Odd case
            odd_pal = self.get_longest_pal(s, i, i)
            if len(odd_pal) > len(res):
                res = odd_pal
            
            # Even case
            even_pal = self.get_longest_pal(s, i, i+1)
            if len(even_pal) > len(res):
                res = even_pal
                
        return res