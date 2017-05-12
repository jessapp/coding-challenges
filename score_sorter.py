# Write a function that takes:

# a list of unsorted_scores
# the highest_possible_score in the game

# and returns a sorted list of scores in less than O(n log n) time.

def sort_scores(highest_possible_score, unsorted_scores):

    score_counts = [0] * (highest_possible_score + 1)

    for num in unsorted_scores:
        score_counts[num] += 1

    sorted_scores = []

    for score, count in enumerate(score_counts):

        for each_time in range(count):

            sorted_scores.append(score)

    return sorted_scores

# this uses COUNTING SORT
# If you have the highest possible number, make a list of that length
# Each index represents each number. Each value represents num times that number appears in original list