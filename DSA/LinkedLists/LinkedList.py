def main():
    new_list = LinkedList()
    new_list.append(4)
    new_list.append(10)
    new_list.append(30)
    # new_list.display()

    new_list.delete_value(10)
    new_list.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        # To add at the beginning at O(1) time: constant time
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        # To add at the End of a list O(n) time: number of n : n which is the length of nodes
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        # traverse the List
        while self.head.next:
            self.head = self.head.next
        self.head.next = new_node

    def delete_value(self, target):
        
        # if nothing in my List
        if not self.head:
            return

        #Base case : If head have the target
        if self.head.data == target:
            self.head = self.head.next
            return
        
        #Regular case : Traverse the List
        while self.head.next and self.head.next.data == target:
            self.head.next = self.head.next.next
        
    def display(self):
        list = []
        #Traverse the List
        while self.head:
            list.append(str(self.head.data))
            self.head = self.head.next
        print(" -> ".join(list) + "-> NULL")
        

if __name__ == "__main__":
    main()