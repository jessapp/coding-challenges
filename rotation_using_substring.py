# Check if one string is a rotation of another when given the method is_substring

def is_rotation(string1, string2):
    length = len(string1)
    if length == len(string2) and len > 0:
        double = string1 + string1
        return is_substring(double, string2)