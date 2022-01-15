'''stack data structure'''

#defining a class variable name stack
class stack():
    def __init__(self):
        #assiging it to the empty list
        self.items  = []

    #lets create the push method
    def push(self,item):
        self.items.append(item)

    #pop method
    def pop(self):
        return self.items.pop()
    
    #to cheak weather the list is empty
    def is_empty(self):
        return self.items == []

    # peek operation on the stack
    def _peek(self):
        if not self.is_empty ():
            return self.items[-1]

    def get_stack(self):
        return self.items

#myStack = stack()
#myStack.push("A")
#myStack.push("B")
#myStack.push("C")
## we are using push method to stack the items
#print(myStack.get_stack()) # ['A','B','C']
#myStack.pop()# runs the pop function and the c item is removed
#print(myStack.get_stack())  # ['A','B']
#print(myStack.is_empty())# this will tell weather the stack is empty or not in bool
#print(myStack._peek()) # this will give us the top element in the stack.