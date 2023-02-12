#!/usr/bin/python3
"""Class defitions for a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of a node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of a node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node of a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of a node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list by"""
    def __init__(self):
        """Initializes the singly linked list"""
        self.__head = None

    def __str__(self):
        """Ensures the singly linked list is printable
           one node number by line
        """
        if self.__head is None:
            return ""
        temp = []   # To store each data of the linked lists(in string form)
        trav = self.__head  # Used to traverse the linked list
        while trav:
            temp.append(str(trav.data))
            trav = trav.next_node
        return '\n'.join(temp)
        # return a string containing all the numbers of the  linked list
        # with '\n' in between them

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list
            (increasing order)
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        trav = self.__head  # Used to travers the linked list
        while trav.next_node:
            if value <= trav.next_node.data:
                temp = trav.next_node
                trav.next_node = new_node
                new_node.next_node = temp
                return
            trav = trav.next_node

        trav.next_node = new_node
