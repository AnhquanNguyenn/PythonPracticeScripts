class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def insertValue(node, key):
    # Empty tree, we simply create a new node with the contents of the key 
    if node == None:
        return Node(key)
    
    if key < node.value:
        node.left = insertValue(node.left, key)
    elif key > node.value:
        node.right = insertValue(node.right, key)
        
    return node

def secondLargest(root):
    # Initial count of visited nodes
    count = [0]
    secondLargestUtil(root, count) 
    
def secondLargestUtil(root, count):
    # Base case, and to prevent unnecessary recursive calls
    if root == None or count[0] >= 2:
        return
    
    # Following reverse inorder traversal, so the largest element is visited first
    secondLargestUtil(root.right, count)
    
    count[0] += 1
    if count[0] == 2:
        print("Second Largest Node is", root.value)
        return
    # Recursively move through each element, the next smallest element
    secondLargestUtil(root.left, count)
    
##         50
#       /     \
#      30     70
#     / \     / \
#    20 40   60 80
#
root = None
root = insertValue(root, 50)
insertValue(root, 30)
insertValue(root, 20)
insertValue(root, 40)
insertValue(root, 70)
insertValue(root, 60)
insertValue(root, 80)
secondLargest(root)

root = None
root = insertValue(root, 5)
insertValue(root, 10)
secondLargest(root)

root = None
root = insertValue(root, 5)
insertValue(root, 10)
insertValue(root, 20)
insertValue(root, 30)
secondLargest(root)
    
