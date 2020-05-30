class RingBuffer:
    def __init__(self, capacity=3):
        # Set up the values for the class
        self.capacity = capacity
        # how values will be appended
        self.list = []
        # Set the current index
        self.x = 0

    def append(self, item):
        # If it is not full, add the item to the current index
        # This is checking to see how long the list is, and if it is less
        # then the max capacity to add the item to the list object 'self.list'
        if len(self.list) < self.capacity:
            self.data.append(item)
        # If it is full, set the current index to 0 and overwrite
        else:
            # Assign the self.list current index to equal the oldest position starting from 0
            self.list[self.x] = item
        # To keep code dry, increment the self.x to one index higher.
        # We do this to 1. Increase the current index to a higher level
        self.x += 1



    def get(self):
        pass