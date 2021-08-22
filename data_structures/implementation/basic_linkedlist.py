from typing import Optional, TypeVar, Generic
from node.basic_node import Node

T = TypeVar('T')


class LinkedList(Generic[T]):
    """
    Class for Linked List data structure
    """
    head: Optional[Node] = None
    # speed insertion up a little bittle
    tail: Optional[Node] = None

    def __init__(self, *data: T) -> None:
        """
        function to initialize linkedlist
        """
        if len(data) == 0:
            return
        if self.linked_list_is_empty():
            self.head = Node(data[0])
        current: Node = self.head
        for value in data[1:]:
            current.next = Node(value)
            current = current.next
        self.tail = current

    def linked_list_is_empty(self) -> bool:
        """
        function to check if linked list is empty
        """
        if self.head == None:
            return True
        return False

    def get_final_node(self) -> Node:
        return self.tail
        # old version:
        # current: Node = self.head
        # while(current.next):
        #     current = current.next
        # print(current)
        # return current

    def append(self, data: T) -> Node:
        """
        function to append new node at tail of linkedlist
        """
        if self.linked_list_is_empty():
            self.head, self.tail = Node(data)
            return
        old_tail = self.get_final_node()
        self.tail = old_tail.next = Node(data)
        return self.tail

    def prepend(self, data: T) -> Node:
        """
        function to append new node at head of linkedlist
        """
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        return self.head

    def delete(self, data: T) -> None:
        """
        function to delete node by value
        """
        last = None
        current = self.head
        while(current.value != data):
            last = current
            current = current.next
        last.next = current.next
        current.value = None
        current.next = None

    def printValues(self) -> None:
        """
        function to print values of all nodes
        """
        if self.linked_list_is_empty():
            print("Linked List is  empty")
            return
        current: Node = self.head
        while(current.next):
            print(current.value, end=' ')
            current = current.next
        print(current.value)

    def heads_and_tails(self) -> None:
        """
        function to print head and tail nodes
        """
        print(f'head: {self.head}, value: {self.head.value}')
        print(f'tail: {self.tail}, value: {self.tail.value}')
