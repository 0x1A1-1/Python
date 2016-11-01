class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, key):
        new_node = Node(key)

        if prev_node:
            new_node.next = prev_node.next
            prev_node.next = new_node

    def append(self, key):

        new_node = Node(key)

        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while(curr.next):
                curr=curr.next
            curr.next = new_node

    def printList(self):
        curr = self.head
        while (curr):
            print curr.key
            curr = curr.next

def initialLinkedList():
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 6.  So linked list becomes 6->None
    llist.append(9)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    return llist

def linkedListTesting():
    llist=initialLinkedList()
    print 'Created linked list is:'
    llist.printList()

def getMiddleNode():
    llist=initialLinkedList()

    curr=llist.head
    curr2=llist.head

    while curr2.next and curr2.next.next:
        curr2 = curr2.next.next
        curr = curr.next
    return curr.key

#linkedListTesting()
print getMiddleNode()
