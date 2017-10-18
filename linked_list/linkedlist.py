"""I hate flake."""

from __future__ import print_function


class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):
    """I hate flake 8."""

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any."""
        self.head = None  # Current
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({})'.format(repr(item)) for item in self.items()]  # Current
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        # TODO: count number of items
        return len(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        # TODO: append given item
        new_node = Node(item)
        if self.is_empty() is not True:
            self.tail.next = new_node
            new_node.previous = self.tail
        else:
            self.head = new_node

        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        # TODO: prepend given item
        new_node = Node(item)
        if self.is_empty() is not True:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        # TODO: find given item and delete if found
        # Done with help from Fernando
        previous = None
        found = False
        current = self.head

        while current and found is False:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data not in list")

        if current.next is None:
            self.tail = previous

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        # TODO: find item where quality(item) is True
        for item in self.items():  # Linear
            if quality(item) is True:
                return item

    def _find_node(self, item):
        """Returns the first node it encounters where data is equal to item."""
        current_node = self.head  # Current
        while current_node is not None:  # Linear
            if current_node.data == item:
                return current_node
            current_node = current_node.next  # Current


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
