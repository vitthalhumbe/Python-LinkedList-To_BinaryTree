from binarytree import build


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = LinkedListNode(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next :
            last = last.next

        last.next = new_node

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

    def push(self, new_data):
        new_node = LinkedListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result




if __name__ == '__main__':
    llist = LinkedList()
    data = [int(x) for x in input("Enter values: ").split()]
    for i in data:
        llist.push(i)

    print("\n\nGiven data Stored in Linked List Data Structure: ")
    llist.printList()
    treeData = llist.to_list()

    Tree = build(treeData)

    print("\n\nLinked List converted into Binary Tree: \n")
    print(Tree)
