# doubly linked lists point in both directions

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):  # value does not have a default value so you have to pass it in everytime you are making an instance of the ListNode
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0  

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)          # create an instance of a new node
        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
                                            # can combine lines 40 and 41 to be -- new_node.next = self.head
        old_head = self.head                # this doesn't change structure -- just for readability
        new_node.next = old_head            # this makes our new node the new head of the list
        old_head.previous = new_node        # or -- self.head.previous = new_node
        self.head = new_node                # reassign head to new node 
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return

        removed_value = self.head.value

        if self.length == 1:                # could also do -- if self.head.next == 1
            self.length = 0
            self.head = None                # the list is empty now
            self.tail = None                # the list is empty now
            return removed_value            # exit out of function 

        new_head = self.head.next           
        self.head = new_head                # assigning new head to the node next of the old head
        self.head.prev = None               # get rid of the pointer to the old head
        self.length -= 1                    # decrease the length
        return removed_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.length == 0:
            self.length = 1                 # adding a single node so length will be 1
            self.head = new_node
            self.tail = new_node
            return

        self.length += 1
        self.tail.next = new_node           # creating pointer to point to the new node
        new_node.prev = self.tail           # creating point to point from the new node to the previous node
        self.tail = new_node                # reassigning newly added node to the tail

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return

        removed_value = self.tail.value     # storing removed value to return later

        if self.length == 1:                # if there is only one node we are going to remove that single node and self.head and self.tail will be None
            self.length = 0                 # removing the single node so length will be 0
            self.head = None
            self.tail = None
            return removed_value

        self.length -= 1
        self.tail = self.tail.prev          # moved tail to the previous node
        self.tail.next = None               # removed arrow pointing to the old tail
        return removed_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return

        if self.head is node:               # if the node is already at the head end the function
            return

        if self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
            self.add_to_head(node.value)
            return

        node.prev.next = node.next          # Connect the node's next and previous nodes with each other
        node.next.prev = node.prev          # Connect the node's next and previous nodes with each other
        self.length -= 1                    # decrement the length because add to  head increments but we want the length to stay the same
        self.add_to_head(node.value)        # add to head creates a new node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return

        if self.tail is node:
            return

        if self.head is node:
            self.head = node.next
            self.head.prev = None
            self.add_to_tail(node.value)
            self.length -= 1
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_tail(node.value)
        self.length -= 1

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        self.length -= 1                # decrements for our main case and the two edge cases below

        if self.head is node:
            self.head = node.next
            self.head.prev = None
            return

        if self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value         # holds whatever the the largest value we have currently found when comparing -- don't use zero because list could be negative
        pointer = self.head                 # create a pointer to keep track of where we are

        while pointer is not None:          # as long as we haven't gone past our tail
            if max_value < pointer.value:
                max_value = pointer.value   # if we find a greater value reassign it to pointer.value
            pointer = pointer.next          # moves us to next node

        return max_value
