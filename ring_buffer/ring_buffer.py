class RingBuffer:
    def __init__(self, capacity):
        # Set up the values for the class
        self.capacity = capacity
        # how values will be appended
        self.data = []
        # Set the current index
        self.x = 0

    def append(self, item):
        # If it is not full, add the item to the current index
        # This is checking to see how long the list is, and if it is less
        # then the max capacity to add the item to the list object 'self.list'
        if len(self.data) < self.capacity:
            self.data.append(item)
        # If it is full, set the current index to 0 and overwrite
        else:
            # Assign the self.list current index to equal the oldest position starting from 0
            self.data[self.x] = item
        # Increment the current index's value
        self.x += 1
        # Check if the index is the same as the capacity of the list
        # If it is, then reassign the current index to 0
        if self.x == self.capacity:
            self.x = 0

    def get(self):
        # Return all elements in the right order
        return self.data
