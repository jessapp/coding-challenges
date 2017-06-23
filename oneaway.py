# Given two strings, write a function to check if they are one "edit" (or zero edits) away.
# An edit can be: inserting a character, removing a character, or replacing a character

def one_away(str1, str2):

    if str1 == str2:
        return True

    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)

    elif len(str1) - 1 == len(str2):
        return one_edit_insert(str2, str1)

    elif len(str1) + 1 = len(str2):
        return one_edit_insert(str1, str1)


    return False


def one_edit_replace(str1, str2):

    count = 0

    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count = count + 1

    if count == 1:
        return True

    return False

def one_edit_insert(str1, str2):

    index1 = 0

    index2 = 0

    while index2 < len(str2) and index1 < len(str1):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False

            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True
