import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Pasted the BST code from other project
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # Logorithmic time
        # If greater than or equal go right
        if value >= self.value:
            # check if .right exists
            if self.right is not None:
                # if so, make that node call insert with the same value
                self.right.insert(value)
            # if not,  create a node with that value, set node as right child
            else:
                new_node = BSTNode(value)
                self.right = new_node
        # Else, go left!
        else:
            if self.left is not None:
                # if so, make that node call insert with the same value
                self.left.insert(value)
            # if not,  create a node with that value, set node as left child
            else:
                new_node = BSTNode(value)
                self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            return self.right.contains(target) if self.right is not None else False
        else:
            return self.left.contains(target) if self.left is not None else False


# Instantiate the BST class
BST = BSTNode()



end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

"""
Runtime of a nested loop is: 6.731910943984985 seconds. It has a runtime complexity of O(n**2)
"""

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
