class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate(root):
    # Empty tree
    if root is None:
        return 0
    
    # We have a leaf node
    if root.left is None and root.right is None:
        return int(root.value)
    
    # recursively go down the left and right subtree and parse expressions
    leftSum = evaluate(root.left)
    rightSum = evaluate(root.right)
    
    # evaluate expressions 
    if root.value == '+':
        return leftSum + rightSum
    elif root.value == '-':
        return leftSum - rightSum
    elif root.value == '*':
        return leftSum * rightSum
    else:
        return leftSum // rightSum
        

tree = Node('*')
tree.left = Node('+')
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node('+')
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))

root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('20')
print(evaluate(root))

root = Node('+')
root.left = Node('*')
root.left.left = Node('5')
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('/')
root.right.right.left = Node('20')
root.right.right.right = Node('2')
print(evaluate(root))
