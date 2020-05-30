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

        # If it is full, set the current index


    def get(self):
        pass