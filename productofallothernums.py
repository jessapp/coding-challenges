# You have a list of integers, and for each index you want to find the product of 
# every integer except the integer at that index.

def get_products_of_all_ints_except_at_index(num_lst):

    if len(num_lst) < 2:
        return num_lst

    products_of_all_ints_except_at_index = [None] * len(num_list)

    product_so_far = 1

    i = 0

    while i < len(num_lst):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= num_lst[i]
        i += 1

    product_so_far = 1

    i = len(num_lst) - 1

    while i >= 0:
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= num_lst[i]
        i -= 1

    return products_of_all_ints_except_at_index


print get_products_of_all_ints_except_at_index([1, 7, 3, 4])


# def product_of_all_other_nums(num_list):
#     prod_list = []

#     for i in range(len(num_list)):
#         total = 1

#         for index, num in enumerate(num_list):
#             if index != i:
#                 total *= num
#         prod_list.append(total)

#     return prod_list

# product_of_all_other_nums([1, 2, 3, 4])