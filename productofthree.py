# Given a list of integers, find the highest product you can get from three of the integers.

def product_of_three(nums):
    # In order to take negative numbers into account, need to take highest and
    # lowest into account

    highest = max(nums[0], nums[1])

    lowest = min(nums[0], nums[1])

    highest_product_of_2 = nums[0] * nums[1]
    lowest_product_of_2  = nums[0] * nums[1]

    highest_product_of_3 = nums[0] * nums[1] * nums[2]

    for num in nums[2:]:

        highest_product_of_3 = max(highest_product_of_3, num * highest_product_of_2, num * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2, num * highest, num * lowest)

        lowest_product_of_2 = min(lowest_product_of_2, num * highest, num * lowest)


        highest = max(highest, num)

        lowest = min(lowest, num)

    return highest_product_of_3