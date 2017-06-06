#Write a function that takes a string as a parameter and returns a new string 
#that is the reverse of the old string, recursively

def rev_string(string, new_string = ""):

    if len(string) == 0:
        return new_string

    new_string += string[-1]
    
    return rev_string(string[:-1], new_string)    

print rev_string("Hello")