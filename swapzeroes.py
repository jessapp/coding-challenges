# Given a array (it has some zeros and non-zero numbers), sort it such that all 
# zeros should go to the right side of the array and non-zeros numbers shouldn't 
# change the order ex: 2, 0, 3, 1,0,4 ==> 2,3,1,4,0,0 Conditions: shouldn't use 
# extra space (temp variables ok), should do in 0(n) time 

def swap_zeroes(num_lst):

    if len(num_lst) <= 1:
        return num_lst

    first = 0
    second = 1


    while second < len(num_lst):

        # If the number at the first pointer is 0
        if num_lst[first] == 0:
            
            # If the number at the second pointer is not zero, swap them and increment both pointers
            if num_lst[second] != 0:
                num_lst[first], num_lst[second] = num_lst[second], num_lst[first]
                first += 1
                second += 1
            else:
                # otherwise, only increment the second pointer
                second += 1

        else:
            first += 1
            second += 1

    return num_lst

print swap_zeroes([2, 0, 3, 1, 0, 4])

print swap_zeroes([4, 5, 0, 0, 5, 6, 0])