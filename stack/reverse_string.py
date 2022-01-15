from stack import Stack
def reverse_string(stuck,input_string):
    for i in range(len(input_string)):
        stuck.push(input_string[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stuck.pop()
    
    return rev_str

stack = Stack()
input_string = "Hello"
print(reverse_string(stack,input_string))
    