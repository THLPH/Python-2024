class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, key):
    current = head
    while current is not None:
        if current.data == key:
            return True
        current = current.next
    return False

def insert_after_nth_node(head, n, value):
    if n <= 0:
        print("Invalid value.")
        return head
    new_node = ListNode(value)
    if n == 1:
        new_node.next = head.next
        head.next = new_node
        return head
    current = head
    count = 1
    while count < n and current is not None:
        current = current.next
        count += 1
    if current is None:
        print("Length <", n)
        return head
    new_node.next = current.next
    current.next = new_node
    return head

'''
Testing
'''

# Linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
current = head
for i in range(2, 6):
    current.next = ListNode(i)
    current = current.next
print("OG list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
print()

# Test search method
print("Searching 3:", search(head, 3))
print("Searching 6:", search(head, 6))

# Test insert_after_nth_node method
head = insert_after_nth_node(head, 3, 9)
print("List with 9 after 3 node:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
print()
