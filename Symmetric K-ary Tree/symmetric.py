class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# to be symmetric, they must have the same values in each subtree but a mirror image
# of one another
def isSymmetric(root):
    return isMirror(root, root)


def isMirror(root1, root2):
    # Empty trees are symmetric
    if root1 is None and root2 is None:
        return True
    
    if root1 is not None and root2 is not None:
        if root1.value == root2.value:
            return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))
    
    
    
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
if isSymmetric(root) == True:
    print("The Tree is Symmetric")
else: 
    print("The Tree is not Symmetric") 
    
root = Node(4)
root.left = Node(3)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(1)
root.right.left = Node(1)
root.right.right = Node(9)
if isSymmetric(root) == True:
    print("The Tree is Symmetric")
else:
    print("The Tree is not Symmetric")
    
root = Node(None)
if isSymmetric(root) == True:
    print("The Tree is Symmetric")
else:
    print("The Tree is not Symmetric")
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
if isSymmetric(root) == True:
    print("The Tree is Symmetric")
else:
    print("The Tree is not Symmetric")
