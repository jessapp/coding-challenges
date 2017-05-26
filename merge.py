#We have our lists of orders sorted numerically already, in lists. 
#Write a function to merge our lists of orders into one sorted list.

def merge_lists(lst1, lst2):

    return_lst = []

    while lst1 != [] or lst2 != []:

        if lst1 == []:
            return_lst.append(lst2.pop(0))

        elif lst2 == []:
            return_lst.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            return_lst.append(lst1.pop(0))
        else:
            return_lst.append(lst2.pop(0))

    return return_lst