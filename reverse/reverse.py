class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Use recursion to solve this problem
        # Check if list is empty
        if node is None:
            return "This is an empty Data Structure."

        # Point the node's next to a new variable
        next = node.get_next()
        # Reverse the direction of the node's next
        node.set_next(prev)
        # If we are not at the tail, continue on, and reverse the LL
        if next is not None:
            self.reverse_list(next, node)
        # If the current node is the tail, make it the head
        else:
            self.head = node