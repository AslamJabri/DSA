from stack import Stack

def convert_dec_to_binary(dec_num):

    if dec_num == 0:
        return 0

    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        print(remainder)
        s.push(remainder)
        dec_num = dec_num // 2
        #print(dec_num)

    bit_num = ""
    while not s.is_empty():
        bit_num += str(s.pop())

    return bit_num

print(convert_dec_to_binary(56))