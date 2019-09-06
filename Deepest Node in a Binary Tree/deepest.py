class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def height(root):
    if (not root):
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    # Since height at root node starts a 1
    return max(leftHeight, rightHeight) + 1

def deepest(root, levels):
    if (not root):
        return
    
    if levels == 1:
       print(root.data, end = "", flush = True)
    elif levels > 1:
        deepest(root.left, levels - 1)
        deepest(root.right, levels - 1)
    

# Test Case 1
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')
#
#      a 
#     / \
#    b   c
#   /
#  d      
           
levels = height(root)
deep = deepest(root, levels)
print(",", levels)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.right.left = Node(5)
root2.right.right = Node(6)
root2.right.left.right = Node(7)
root2.right.right.right = Node(8)
root2.right.left.right.left = Node(9)

#           1
#          / \
#         2   3
#       /    / \
#      4    5   6
#            \   \
#             7   8
#            /
#           9

levels = height(root2)
deep = deepest(root2, levels)
print(",", levels)

