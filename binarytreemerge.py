"""Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null 
node will be used as the node of new tree.

Input: 

    Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 

Merged tree:
         3
        / \
       4   5
      / \   \ 
     5   4   7

"""

def merge_trees(root1, root2):

    if root1 is None and root1 is None:
        return None

    if root1:
        val1 = root1.val
        left1 = root1.left
        right1 = root1.right
    else:
        val1 = 0
        left1 = None
        right1 = None

    if root2:
        val2 = root2.val
        right2 = root2.right
        left2 = root2.left
    else:
        val2 = 0
        right2 = None
        left2 = None


    new_node = Node(val1 + val2)

    new_node.left = merge_trees(left1, left2)

    new_node.right = merge_trees(right1, right2)

    return new_node


