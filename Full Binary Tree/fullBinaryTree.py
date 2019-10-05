class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.value, end=' ')
        printInorder(root.right)
        
def createFullBinaryTree(root):
    # Empty tree, or empty subtree base case
    if root is None:
        return None
    
    # Recursively check the left and right subtrees, to get values are None values
    root.left = createFullBinaryTree(root.left)
    root.right = createFullBinaryTree(root.right)
    
    # Returning the root value if there is no left or right subtree, just simply trying to take out
    # the nodes with single child nodes
    if root.left is None and root.right is None:
        return root
    
    # Doesn't pass the above cases, then we have a situation with a node with a single child node
    # Deleting the single child case, by changing the child to be the new root, and deleting the old parent
    if root.left is None:
        newRoot = root.right
        temp = root
        root = None
        del(temp)
        return newRoot
    if root.right is None:
        newRoot = root.left
        temp = root
        root = None
        del(temp)
        return newRoot
    
    return root
    
def createFullBinaryTreeHelper(root):
    tree = createFullBinaryTree(root)
    printInorder(tree)
    print('\n')
        

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

createFullBinaryTreeHelper(root)
#                               2
#                             /   \
#                            7     5   
#                             \     \
#                              6     9
#                             / \   /
#                            1  11  4
#
#           2
#          / \
#         6   4
#        / \
#       1  11

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
createFullBinaryTreeHelper(tree)

# Given this tree:
#     1
#    / \
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \
#   0   3
#      / \
#     9   4
