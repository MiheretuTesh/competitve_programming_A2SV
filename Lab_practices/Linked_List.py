class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def deleteNode(self, new_data):
        node = self.head
        prevNode = 0
        if (node.data == new_data):
            self.head = node.next
            node = None
        
        while node != None:
            if(node.data == new_data):
                break
            prevNode = node
            node = node.next
        
        prevNode.next = node.next
        node = None

        node = self.head
        while node:
            print(node.data)
            node = node.next
    def printMiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)


lst = LinkedList()
lst.push(1)
lst.push(2)
lst.push(3)
lst.push(5)
# print(lst.printList())
lst.deleteNode(2)
