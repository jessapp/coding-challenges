# Given scores of N athletes, find their relative ranks and the people with the top 
# three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and 
# "Bronze Medal".

# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

def relative_ranks(scores):

    sorted_scores = sorted(scores)[::-1]

    score_keeper = {}

    final = []

    for i in range(len(sorted_scores)):
        score_keeper[sorted_scores[i]] = i

    for key, val in score_keeper.items():
        if val == 0:
            gold = key
        elif val == 1:
            silver = key
        elif val == 2:
            bronze = key


    for score in scores:
        if score == gold:
            final.append("Gold Medal")
        elif score == silver:
            final.append("Silver Medal")
        elif score == bronze:
            final.append("Bronze Medal")
        else:
            final.append(score)

    return final

print relative_ranks([3, 5, 2, 4, 1])