class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def validate(root, left, right):

    # Empty trees are valid binary search trees, base condition
    if root == None:
        return True
    
    # If there is a left node, we need to check that it is less than the root/parent
    if (left != None and root.data <= left.data):
        return False
    
    # If there is a right node, we need to check that it is greater than the root/parent
    if (right != None and root.data >= right.data):
        return False

    # recursively check the left and right node, in respect to the root/parent
    return validate(root.left, left, root) and validate(root.right, root, right)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
left = None
right = None

print(validate(root, left, right))

#    5
#   / \
#  3   7
# / \ /
#1  4 6

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)
left = None
right = None

#    5
#   / \
#  3   7
# / \ /
#3  4 6
print(validate(root, left, right))