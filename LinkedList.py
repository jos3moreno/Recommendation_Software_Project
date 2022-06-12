from Node import *


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_head_node(self):
        return self.head

    def size(self):
        '''Return the size of the linked list'''
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

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

    def show_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next

    def get_node_by_value(self, val):
        current = self.head
        idx = 0
        while current:
            if idx == val:
                return current.value
            idx += 1
            current = current.next
