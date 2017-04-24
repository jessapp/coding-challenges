#Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, 
#and returns the maximum monetary value the duffel bag can hold.
# (weight, value)

def max_duffle_bag_value(cake_lst, max_weight):

    max_values_at_capacities = [0] * (max_weight + 1)

    for current_capacity in range(max_weight + 1):

        current_max_value = 0

        for weight, value in cake_lst:

            if weight == 0 and value != 0:
                raise Exception("Infinite capacity")

            if weight <= current_capacity:
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - weight]

                current_max_value = max(max_value_using_cake, current_max_value)


        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight]