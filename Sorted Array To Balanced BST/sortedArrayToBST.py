class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def sortedArrayToBST(numbers):
    # Empty List of numbers, there is no such conversion to a BST
    if not numbers:
        return None
    
    # Finding the root node, which would be the middle value in the list
    # and creating the root node of the tree
    middle = len(numbers) // 2
    root = Node(numbers[middle])
    
    # The left side of the tree is determined by all values less than the root value
    # which in the list is all the values before the middle value
    root.left = sortedArrayToBST(numbers[:middle])
    
    # The right side of the tree is determined by all values greater than the root value
    # which in the list is all the values after the middle value
    root.right = sortedArrayToBST(numbers[middle + 1:])

    return root


def preorderTransversal(tree):
    if not tree:
        return
    
    BalancedBST.append(tree.data)
    preorderTransversal(tree.left)
    preorderTransversal(tree.right)
    
    return BalancedBST

BalancedBST = []
numbers = [1, 2, 3, 4, 5, 6, 7]
tree = sortedArrayToBST(numbers)
print(preorderTransversal(tree))
    

