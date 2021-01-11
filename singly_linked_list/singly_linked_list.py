# A singly linked list is similar to a list but nothing has an index
# A singly linked list is made up of a node
# A node has two attributes: a value and its next
# A value is the value a node holds (ie: 15)
# The next points to the next node in the list (the next memory location)
# Nodes are not stored next to each other they are just pointing to the one next to each other

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

        previous_head = self.head # create a new pointer for old head to keep track of it
        self.head = new_node # assigned the new node to self.head
        self.head.next = previous_head # pointed the next to the old head

    def remove_head(self):
        if self.head is None:
            return # if the list is empty stop the function and don't do anything
        
        data = self.head.get_value() # method is on the Node -- use dot notation to call it

        if self.head.next is None:
            self.head = None
            self.tail = None
            return data
        
        self.head = self.head.next # reassign head
        return data # return value of head

    def remove_tail(self):
        if self.head is None:
            return

        pointer = self.head
        data = self.tail.get_value()

        if self.head.next is None:
            self.head = None
            self.tail = None
            return data

        while pointer.next.next is not None: # while loop continues checking until the pointer is none. when the pointer is none, the pointer is pointing at the tail
            pointer = pointer.next

        self.tail = pointer
        self.tail.next = None # delete the last Node
        return data 

# this prints the memory location of the node
x = Node(15)
print(x)

# this prints the actual value of the node
print(x.value)

# this prints None 
# print(x.next.value)