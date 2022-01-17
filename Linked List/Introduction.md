There are three linked list
    Single linked list
    Double linked list
    Circular Linked list
Every linked list consist of nodes. and every node has 2 components.
    Data
    Next
The data component allows node in the linked list to store an element of data that can be of type string, haracter,number or any other type of object.
The next component in every node is a pointer that points from one node to another.
The start of the linked list is referred to as the head.head is a pointer that points to the beginning of the linked list, so if we want to traverse the linked list to obtain or access an element of the linked list we'll start from the head.
The last component of a singly linked list is a notion of null. This null terminates the linked list . In python we call this None. The last node in a singly linked list points to a null object and that tells its the end of list.

# Insertion And Deletion
The insertion and deletion in arrays is O(n) operation. Lets assume in a given array if we want to insert an element in the first all the elements have to shift to left to make the room for the element to enter.Due to shifting of elements the time complexity is O(n). The same goes for the deletion as all the arrays have to be shifted to fill the gap in the array.

Inserting a node at the head in the linked list given the head node is a constant-time operation need to change the orientation of few pointers. If given the exact pointer after which we have to insert another node ,it will be a constant-time operation . O(1)

# Accessing Elements
Accessing any element given an index in arrays is better than accessing nth elements in linked lists. It is a constant time O(1) operation to access elements in arrays. If given an array and an index, it can immediately give you the element at which the entry is stored. This is because arrays are contiguous.

Accessing an nth element in a linked list is an O(n) operation given that you have access to the head node of the linked list. If we want to access an element, we need to start from the head pointer and traverse the entire linked list before we can get to it.

# Contiguos Memory
Arrays are contiguous in memory which allows the access time to be constant, whereas, in linked lists, you do not have the luxury of contiguous memory.