class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.sum = 0


def add_cum_sum(head):
    node = head
    cum_sum = 0
    while node:
        node.sum = node.value + cum_sum
        cum_sum = node.sum
        node = node.next


def removeConsecutiveSumTo0(head):
    add_cum_sum(head)
    dummy_head = Node(None)
    dummy_head.next = head

    seen_totals = dict()
    node = dummy_head
    index = 0
    while node:
        if node.sum in seen_totals:
            seen_totals[node.sum].next = node.next
        seen_totals[node.sum] = node
        index += 1
        node = node.next

    return dummy_head.next


head = Node(3)
head.next = Node(4)
head.next.next = Node(-7)
head.next.next.next = Node(5)
head.next.next.next.next = Node(-6)
head.next.next.next.next.next = Node(6)
head = removeConsecutiveSumTo0(head)

while head:
    print(head.value)
    head = head.next

node = Node(10)
node.next = Node(5)
node.next.next = Node(-10)
node.next.next.next = Node(-5)
node.next.next.next.next = Node(-3)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.value)
    node = node.next
