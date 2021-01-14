class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # we don't know if a node will be coming after this yet

    def get_value(self):
        return self.value # when we call this method it will return the value

class LinkedList:
    def __init__(self):
        # Head and tail are pointers
        self.head = None # Points to the first node
        self.tail = None # Points to the last node
    
    def add_to_tail(self, value):
        new_node = Node(value) # create a new node 

        # check if self.head is None
        if self.head is None: # is operator compares the identity of the two objects, == compares the value
            self.head = new_node
            self.tail = new_node
            return # if statement will end here and stop running

        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            return 

        previous_head = self.head
        self.head = new_node
        self.head.next = previous_head

    def remove_head(self):
        if self.head is None:
            return
        
        data = self.head.get_value()

        if self.head.next is None:
            self.head = None
            self.tail = None
            return data
        
        self.head = self.head.next 
        return data 

    def remove_tail(self):
        if self.head is None:
            return

        pointer = self.head
        data = self.tail.get_value()

        if self.head.next is None:
            self.head = None
            self.tail = None
            return data

        while pointer.next.next is not None:
            pointer = pointer.next

        self.tail = pointer
        self.tail.next = None
        return data 

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size 

    def enqueue(self, value):
        self.size += 1
        return self.storage.append(value)

    def dequeue(self): 
        if self.size == 0:
            return

        self.size -= 1
        return self.storage.pop(0)

class Stack:    
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1

        return self.storage.append(value) 

    def pop(self):
        if len(self.storage) == 0:
            return
            
        self.size -= 1

        remove_item = self.storage[-1]
        del self.storage[-1]
        return remove_item

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

** the node on the left is going to be lesser and the node on the right is always going to be greater **
All values to the left must be smaller than the root node
All values to the right must be greater than the root node
You will always traverse to the left first, then the right

Recursion -- call the same method inside of the method
    - similar to a while loop
    - recursion should always be moving towards the base case ie: self.value = target
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)         # recursion! called insert inside of insert
            else:
                self.left = BSTNode(value)      # if there is no node to the left, create a new instance of the class with the value
        else:
            if self.right:                      # if there is a node to the right
                self.right.insert(value)        # insert the node with the value
            else:
                self.right = BSTNode(value)     # if there is no node to the right, create a new instance of the class with the value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:                        # if the value is equal to the target, return true
            return True
        elif target < self.value:                       # if the target is less than the value, go to the left of the tree -- we always start by going to the left
            if self.left is None:                       # go down left side of tree to see if target exists, if it does not return False
                return False
            else:
                return self.left.contains(target)       # if there is a node we recurse and run contains again (starting at line 156)
                # this will not always be the last line of code
        else:
            if self.right is None:                      # go down right side of tree to see if target exists, if it does not return false
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree -- recursion version
    # def get_max(self):
    #     max_value = self.value
    #     if max_value is not None:                       # make sure there is actually a value there
    #         if self.right is None:                      # if there is nothing to the right, the starting value (max value) is the greatest number
    #             return max_value
    #         else:
    #             return self.right.get_max()
    #     else:
    #         return None



    # Return the maximum value found in the tree -- while loop version
    def get_max(self):
        # max_value = None                                # accounts for if the tree is empty
        # if max_value < self.value:                      # if None is < self.value
        #     max_value = self.value                      # reset max_value to self.value

        current_node = self                                 # store the node we are on into a variable so we can track
        if current_node is None:                            # if there is nothing at current node stop the function and return None
            return None
        while current_node.right:
            current_node = current_node.right               # the node to the right of our current node will always be larger than our current node -- when there is not a node to the right, we break out of the while loop
        max_value = current_node.value                      # assign the node we stopped in in the while loop to the max value and return it 
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):                                 # function is being passed in as a parameter
        if not self:
            return                                          # if there no node in BST, return
        fn(self.value)                                      # we want to pass self.value into fn -- runs the function on the value of each node
        if self.left:
            self.left.for_each(fn)                          # pass in fn because for_each requires fn as an argument
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):                               # Going to be similar to for each method
        if self is None:
            return

        if self.left:                                       # If there is a left - go down left side of BST and recurse to keep going down the left
            self.left.in_order_print()
        print(self.value)                                   # print current node - only want to print the values to the left because that is how they are going to print in order
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,          
    # in an iterative breadth first traversal
    def bft_print(self):                                    # breadth first is going down by levels - use a queue (shopping line)
        q = Queue()
        q.enqueue(self)                                     # going to add the current node into the queue
        while q.size != 0:
            current = q.dequeue()
            print(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)            

    # Print the value of every node, starting with the given node,         
    # in an iterative depth first traversal
    # if we wanted to print the nodes out in a different order we would reverse the if statements
    def dft_print(self):
        s = Stack()                                         # think of stack of pancakes
        s.push(self)
        while s.size != 0:
            current = s.pop()                               # overwrote pop in our Stack class
            print(current.value)                            # depending on where you put this print statement, it is going to print it in a different order
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):                                # before it checks left and right it is going to print -- as soon as it finds the node it will print it 
        if self:                                            # [1, 2, 4, 5, 3, 6, 7]
            print(self.value)
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):                               # the print statement will go at the bottom
        if self:
            if self.left:                                   # [4, 5, 2, 6, 7, 3, 1] - because of where we chose to print the list comes out different
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            print(self.value)
        

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
