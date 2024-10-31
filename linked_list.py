#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repl__(self):
        return f"[{self.data}] [{self.next}]"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
            print(last_node)

        last_node.next = new_node

    def display(self):
        current_node = self.head

        if not current_node:
            return "List is empty"

        while current_node:  # Traverse through the list
            print(current_node.data, end=' --> ' if current_node.next else '')
            current_node = current_node.next
        
        print("None")  # Indicate the end of the list

    def remove(self, data):
        pass

my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)


my_list.display()

