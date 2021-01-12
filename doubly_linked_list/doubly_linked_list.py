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
            self.length == 0
            self.head = None
            self.tail = None
            return                          # exit out of function 

        new_head = self.head.next           
        self.head = new_head                # assigning new head to the node next of the old head
        self.head.prev = None
        self.length -= 1
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
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass