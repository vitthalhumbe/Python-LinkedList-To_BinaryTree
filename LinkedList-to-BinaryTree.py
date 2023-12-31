# Importing the 'build' function from the 'binarytree' library
from binarytree import build

# Definition of a node in the linked list
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition of a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Appending a new node with the given data to the linked list
    def append(self, new_data):
        new_node = LinkedListNode(new_data)

        # If the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the linked list and append the new node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Printing the linked list
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

    # Pushing a new node with the given data to the front of the linked list
    def push(self, new_data):
        new_node = LinkedListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # Converting the linked list to a Python list
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

# Main program
if __name__ == '__main__':
    # Creating a linked list and populating it with user-input values
    llist = LinkedList()
    data = [int(x) for x in input("Enter values: ").split()]
    for i in data:
        llist.push(i)

    # Displaying the linked list
    print("\n\nGiven data Stored in Linked List Data Structure: ")
    llist.printList()
    
    # Converting the linked list to a Python list
    treeData = llist.to_list()

    # Building a binary tree from the Python list
    Tree = build(treeData)

    # Displaying the binary tree
    print("\n\nLinked List converted into Binary Tree: \n")
    print(Tree)
