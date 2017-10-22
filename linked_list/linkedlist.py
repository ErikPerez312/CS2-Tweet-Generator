from __future__ import print_function
# CSUTOJ

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None

        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        return len(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)

        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        
        self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""

        current_node = self.head  # Constant time
        previous_node = None  # Constant time
        node_found = False  # Constant time

        # Try to find item in linked list. If found, set 'node_found' to 'True'
        while current_node is not None and node_found is False:  # Linear time
            if current_node.data == item:  # constant time
                node_found = True  #constant time
            else:
                previous_node = current_node  # constant time
                current_node = current_node.next  # constant time

        if node_found is False:  # constant time
            raise ValueError("Item not in list")  # constant time
        
        if current_node.next is None:  # constant time
            self.tail = previous_node  # constant time

        # 'Previous_node' is 'None' when 'item' is the head
        if previous_node is None:  # constant time
            self.head = current_node.next  # constant time
        else:
            previous_node.next = current_node.next 

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        for item in self.items():
            if quality(item) is True:
                return item 


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))

    print("-----------------------------")
    # Enable this after implementing delete:
    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()