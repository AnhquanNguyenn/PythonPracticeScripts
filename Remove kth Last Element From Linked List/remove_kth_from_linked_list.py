class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth_from_linked_list(head, k):
    # if there is an empty list
    if not head:
        return head

    nodeQueue = []
    currentNode = head

    while currentNode:
        if len(nodeQueue) == (k + 1):
            nodeQueue.pop(0)
        nodeQueue.append(currentNode)
        currentNode = currentNode.next

    # deleting the last node
    if k == 1:
        nodeQueue[0].next = None
        return head
    # Deleting first node
    elif k == len(nodeQueue):
        return nodeQueue[1]
    # Deleting node in between
    else:
        nodeQueue[0].next = nodeQueue[2]
        return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(head)

head = remove_kth_from_linked_list(head, 3)
print(head)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(head)
head = remove_kth_from_linked_list(head, 5)
print(head)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(head)
head = remove_kth_from_linked_list(head, 1)
print(head)
