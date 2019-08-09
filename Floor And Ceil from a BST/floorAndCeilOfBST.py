# Creating a node for our binary search tree with data, and a left and right node
class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def ceil(root, input):
    # if there is an empty tree, then there is no ceiling
    if root == None:
        return -1

    # if root equals the key, then we have already found the ceiling
    if root.key == input:
        return root.key

    # If the root is less than the input, the ceiling must be in the right subtree
    if root.key < input:
        return ceil(root.right, input)

    # Last check the root, or the left subtree for the ceiling
    value = ceil(root.left, input)
    if value >= input:
        return value
    else:
        return root.key


root = Node(8)

root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

for i in range(16):
    print((i, ceil(root, i)))
