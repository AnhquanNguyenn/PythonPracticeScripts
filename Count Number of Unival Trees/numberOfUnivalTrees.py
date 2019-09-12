class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    
def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
# traverses the tree in a bottom up manner. We will find out if a node has been visited 
# by returning true/false
def helper(root):
    if root is None:
        return 0, True
    
    # recursively determine if there are individual subtrees that are unival trees and getting a total count going 
    # through the left subtree and right subtree
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        # cannot be a unival tree if different values, so we skip and return current count
        if root.left is not None and root.data != root.left.data:
            return total_count, False
        if root.right is not None and root.data != root.right.data:
            return total_count, False
        return total_count + 1, True
    return total_count, False


root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)
print(count_unival_subtrees(root))
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
#The 5 trees are:
#- The three single '1' leaf nodes. (+3)
#- The single '0' leaf node. (+1)
#- The[1, 1, 1] tree at the bottom. (+1)

root = Node('a')
root.left = Node('a')
root.right = Node('a')
root.right.left = Node('a')
root.right.right = Node('a')
root.right.right = Node('A')
print(count_unival_subtrees(root))
#   a       2 a leaves and 1 A leaf. The A leat caues all of its parents to not be counted as a unival tree 
#  / \
# a   a
#     /\
#    a  a
#        \
#         A

root = Node('a')
root.left = Node('c')
root.right = Node('b')
root.right.left = Node('b')
root.right.right = Node('b')
root.right.right.right = Node('b')
print(count_unival_subtrees(root)) 
#  a            leaf at c and every b
# / \
#c   b
#    /\
#   b  b
#       \
#         b
