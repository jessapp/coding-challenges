#We have a list of integers, where:

#The integers are in the range 1..n1..n
#The list has a length of n+1n+1
#It follows that our list has at least one integer which appears at least twice. 
#But it may have several duplicates, and each duplicate may appear more than twice.

#Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)

def find_dups_space(num_lst):

    # set pointers at beginning and end of list
    floor = 1

    ceiling = len(num_lst) - 1


    while floor < ceiling:

        # Divide the range into and upper and lower range
        # Which do not converge 

        mid = floor + (ceiling - floor) / 2

        lower_range_floor, lower_range_ceiling = floor, mid

        upper_range_floor, upper_range_ceiling = mid + 1, ceiling


        items_in_lower_range = 0

        for item in num_lst:

            # Count how many nums fall into the lower range
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

            distinct_nums_in_lower_range = lower_range_ceiling - lower_range_floor + 1

            if items_in_lower_range > distinct_nums_in_lower_range:
                # In this case, there must be a duplicate in the lower range
                # So we go back through this approach iteratively 

                floor, ceiling = lower_range_floor, lower_range_ceiling
            else:
                # Otherwise, there must be a duplicate in the upper range

                floor, ceiling = upper_range_floor, upper_range_ceiling
                
    # When the floor and ceiling converge, we have a repeat number
    return floor