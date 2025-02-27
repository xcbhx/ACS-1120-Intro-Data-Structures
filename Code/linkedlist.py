#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) Linear for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) constant time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Linear time because you always need to visit each node."""
        # TODO: Loop through all nodes and count one for each
        node_length = 0
        node = self.head 
        while node is not None:
            node_length += 1 
            node = node.next
        return node_length


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Constant time because it maintains a tail pointer, so I can 
        access the last node and append the new node without traversing the entire list."""
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail
        # Node instance
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # Link the old tail to the new node
            self.tail = new_node # Move the tail pointer to the new node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) constant because you can directly access the head and 
        insert a new node at the beginning with traversing the list."""
        # TODO: Create new node to hold given item
        # TODO: Prepend(means add a new node to beginning of linked list) node before head, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # Point new node to the current head
            self.head = new_node # Update head to the new node


    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(1) Constant because if the item you're looking 
        for is the first node in the list. item function returns True for the first node.
        TODO: Worst case running time: O(n) Linear because if the item you're looking 
        for is at the end of the list or not present then you have to traverse all nodes in the list."""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        node = self.head # Start at the head
        while node is not None:
            if node.data == item: 
                return True
            node = node.next # Move to the next node
        return False


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Constant time because the item to be deleted
        is the first node (the head) of the linked list. 
        TODO: Worst case running time: O(n) Linear time because the items to be deleted is
         either the last node in the list or it is not present at all."""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        previous = None
        current = self.head

        while current is not None:
            if current.data == item:
                if previous is None: # Delete the head
                    self.head = current.next
                    if current.next is None: # If deleting the only node
                        self.tail = None
                else:
                    previous.next = current.next # bypass the current node
                    if current.next is None: # If deleting the tail
                        self.tail = previous
                
                return # Item deleted

            previous = current 
            current = current.next

        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
