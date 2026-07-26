class SinglyNode:
    def __int__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    
    def append(self, data):
        new_node = SinglyNode
        