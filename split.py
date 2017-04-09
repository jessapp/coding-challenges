"""Split astring by splitter and return list of splits.

This should work like that built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implemented that.

"""


def split(astring, splitter):
    """Split astring by splitter and return list of splits."""

    out = []
    index = 0

    # while index count is less than the length of the string
    while index <= len(astring):

        #the current index is index
        curr_index = index
        # index is the first index in which splitter occurs in astring, from
        # the index point onward
        index = astring.find(splitter, index)

        # if the index isn't the last letter in the string
        if index != -1:
            # append a slice of the string between current_index and the index in 
            # which the splitter occurs
            out.append(astring[curr_index:index])
            # move the index over past the splitter occuring
            index += len(splitter)

        else:
            # couldn't find any more instances of splitter in astring
            out.append(astring[curr_index:])
            break

    return out


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
