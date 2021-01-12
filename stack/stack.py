# import is weird because files are in different directories
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

Think of a stack as a stack of pancakes - you add a pancake to the top of the stack and take the pancakes off the top of the stack
"""

# using a linked list
# class Stack:
    # def __init__(self):
    #     self.size = 0
    #     self.storage = LinkedList() # this is the actual stack

    # def __len__(self):
    #     return self.size

    # def push(self, value): # increment size by one
    #     self.size += 1
    #     return self.storage.add_to_head(value) # returning for testing purposes

    # def pop(self): # decrement size by one
    #     if self.size == 0: # check to see if size is 0 because there will be nothing to remove 
    #         return

    #     self.size -= 1
    #     return self.storage.remove_head() # don't pass value in for remove


# using an array
class Stack:    
    def __init__(self):
        self.size = 0
        self.storage = [] # this is the actual stack

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1

        # add to the head
        # return self.storage.insert(0, value) # head is at 0 so we insert head there

        # add to the tail
        return self.storage.append(value) 

    def pop(self):
        if len(self.storage) == 0:
            return
            
        self.size -= 1

        # remove from the head
        # remove_item = self.storage[0]
        # del self.storage[0] # have to use del because pop method is overwritten in this program
        # return remove_item

        # remove from the tail
        remove_item = self.storage[-1]
        del self.storage[-1]
        return remove_item
