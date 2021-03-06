# could use this import in the stack file
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList 

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

Think of a queue like a shopping queue - you enter at the end and leave at the front of the line

**import deck from collections for queues**
"""

# using a linked list
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size 

#     def enqueue(self, value): # add it to the queue at the end
#         self.size += 1 # self.size = self.size + 1
#         return self.storage.add_to_tail(value)

#     def dequeue(self): # remove it from to the beginning of the queue
#         if self.size == 0:
#             return

#         self.size -= 1
        # return self.storage.remove_head()

# using an array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size 
        # this works too -- return len(self.storage)

    def enqueue(self, value): # add it to the queue at the end
        self.size += 1
        return self.storage.append(value)

    def dequeue(self): # remove it from to the beginning of the queue
        if self.size == 0:
            return

        self.size -= 1
        return self.storage.pop(0)