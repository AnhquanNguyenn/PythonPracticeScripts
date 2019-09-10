class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def getHeightHelper(root, data, height):
    if root == None:
        return 0

    # if we encounter the root node, the height is simply 1
    if root.data == data:
        return height
    
    # recursively going to the left sub tree
    downHeight = getHeightHelper(root.left, data, height + 1)
    
    if downHeight != 0:
        return downHeight
    
    # recursively going to the right sub tree
    downHeight = getHeightHelper(root.right, data, height + 1)
    
    return downHeight

def getHeight(root, data):
    return getHeightHelper(root, data, 1)

    
tempList = list()
desiredHeight = 3
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
for x in range(1, 8):
    height = getHeight(root, x)
    if height:
        print("Height of", x, "is", height)
        if height == desiredHeight:
            tempList.append(x)
    else:
        print(x, "is not in tree")
        
print("Nodes of height", desiredHeight, tempList)
    
    
    
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
