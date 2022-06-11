from Node import *


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_head_node(self):
        return self.head

    def add_to_the_front(self, data):
        '''Add data to the list'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        '''Return the size of the linked list'''
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def add_at(self, data, position):
        '''Insert data at the specified position, '''
        if position > self.size() - 1:
            raise IndexError
            print("Index is out of bounds. ")
        current = self.head
        prev = None
        location = 0
        if position == 0:
            self.add_to_the_front(data)
        else:
            new_node = Node(data)
            while location < position:
                location += 1
                prev = current
                current = current.next
            prev.next = new_node
            new_node.next = current

    def add_to_the_end(self, data):
        '''Add Data to the end of the LinkedList'''
        current = self.head
        prev = None
        position = 0
        length = self.size()
        while position < length:
            prev = current
            current = current.next
            position += 1
        new_node = Node(data)
        if prev is None:
            new_node.next = current
            self.head = new_node
        else:
            prev.next = new_node

    def remove_head(self):
        self.head = self.head.next

    def remove_tail(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        last = current.next
        current.next = None
        last = None

    def remove_at(self, location):
        # List is empty
        if self.head is None:
            return
        if location == self.size() - 1:
            self.remove_tail()
        if location == 0:
            self.remove_head()
        idx = 0
        current = self.head
        prev = self.head
        tmp = self.head
        while current is not None:
            if idx == location:
                tmp = current.next
                break
            prev = current
            current = current.next
            idx += 1

    def show_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next

    def sort_list(self):
        current = self.head
        idx = None
        # Base case if list is empty
        if self.head is None:
            return
        else:
            while current is not None:
                idx = current.next
                while idx is not None:
                    if current.value > idx.value:
                        tmp = current.value
                        current.value = idx.value
                        idx.value = tmp
                    idx = idx.next
                current = current.next
