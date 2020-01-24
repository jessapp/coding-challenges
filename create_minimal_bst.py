    # Given a sorted list of numbers, create an algorithm to create a bst with minimal height

def create_minimal_bst(sorted_nums):
    if sorted_nums == []:
        return None

    half = len(sorted_nums) / 2
    mid = sorted_nums[half]

    node = TreeNode(mid)
    node.left = create_minimal_bst(sorted_nums[0:half])
    node.right = create_minimal_bst(sorted_nums[half + 1:])

    return node 