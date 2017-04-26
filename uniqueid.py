# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

def find_unique_int(lst):

    # First solution: 

    # stack = []

    # for drone_id in lst:
    #     if drone_id not in stack:
    #         stack.append(drone_id)
    #     else:
    #         stack.remove(drone_id)

    # return "".join(stack)

    # Second solution:

    ids_and_occurences = {}

    for drone_id in lst:
        ids_and_occurences[drone_id] = ids_and_occurences.get(drone_id, 0) + 1

    for drone_id, frequency in ids_and_occurences.items():
        if frequency == 1:
            return drone_id