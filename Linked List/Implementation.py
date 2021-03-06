class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#PRINTING METHOD for the linked list
#There you go! We initialize cur_node equal to the head of the linked list.
# Then we use a while loop which keeps running and printing the data if cur_node is not equal to None.
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

#EMPTY LIST       
#Append method will insert an element at the end of the linked list
#We define a new_node using our Node class on line 11. It consists of the data and the next field. 
# We pass in data to the append method, and the data field in new_node has the entry of data that we passed to the append method.
#For the Empty List    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
#In the above code, we check if the linked list is empty by checking the head of the linked list.
#If the self.head is None on line 16, it implies that it’s an empty linked list and there’s nothing there.
#The head pointer doesn’t point to anything at all, and therefore there is no node in the linked list. 
#If there is no node in the linked list, we set the head pointer to the new_node that we created on line 17. 
#In the next line, we simply return. 
#The case of an empty linked list is relatively easy to handle.

#For NON-EMPTY List:
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
#On line 27, we define last_node which is initially equal to the head. This implies we’re at the start of the linked list.
#We have named the variable we defined on line 27 last_node​ because that’s what it will eventually point to. 
#It will start at the beginning of the linked list and move through the linked list as long as the last_node.next doesn’t point to None. 
#We keep moving from node to node on line 29 until we get to the last_node where last_node.next will point to None and will terminate the while loop on line 28.
#After the while loop concludes, last_node points to the last node. On line 30, we input our new_node into the linked list by setting the next of last_node to new_node which has its own next pointing to None.

#PREPEND METHOD
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
#We create a method called prepend. This also takes self and data since we need to tell it what to prepend to the linked list. We create a node based on the data passed into the method.
# Next, on line 29, we point the next of the new_node to the current head of the linked list, and then we set the head of the linked list equal to new_node on line 50. 
# We have now prepended E to llist in the code above which previously only contained A, B, and C. 
# You can play around and verify the prepend method for yourself!

#INSERT AFTER NODE
    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

#deleting the node by value
    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.next == key:
            self.head = cur_node.next
            cur_node = None
            return
#The class method delete_node takes key as an input parameter.  we’ll declare cur_node as self.head to have a starting point to traverse the linked list.
#To handle the case of deleting the head, we’ll check if cur_node is not None and if the data in cur_node is equal to key on.
#Note that cur_node is pointing to the head of the linked list at this point. If key matches cur_node.data, we’ll update the head of the linked list (self.head) to cur_node.next, i.e., the next node of the previous head node . 
#Once we have updated the head of the linked list, we’ll set the node to be deleted (cur_node) to None  and return from the method.
        prev = None
        while cur_node and cur_node.data != key:
            prev= cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

#deletion by position
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None
#The delete_node_at_pos takes in pos as one of the input parameters.
#First of all, we check on line 90 if the linked list is an empty list or not. We only proceed to line 91 if self.head is not None.
#As we discussed before, we need to handle the case where pos will equal 0. If pos equals 0, it essentially means that we want to delete the head node.
#On line 91, cur_node is initialized to the head node. Next, we check if pos is 0 or not. If it is, we update the head node to the next node of cur_node, set cur_node to None, and return from the method (lines 94-96). 
# On the other hand, if we are deleting a node at a position other than the head node, we will proceed to line 98. 
# We declare prev and set it to None and on line 99, we initialize count to 0. 
# Now we traverse the linked list by updating prev and cur_node (lines 101-102) and increment count by 1 on line 103.
# The while loop will terminate if cur_node becomes None or count becomes equal to pos which will imply that cur_node will be the node that we want to delete.
#The code on lines 105-109 is precisely the same as in the delete_node class method.

#Calculating Length of a Linked List
    def len_iterative(self):
        count = 0
        cur_node =self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
#recursion Implementation for calculating node
    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+ self.len_recursive(node.next)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node(llist.head.next,"F")
llist.delete_node("B")


print(llist.len_iterative())
print(llist.len_recursive(llist.head))
llist.print_list()
