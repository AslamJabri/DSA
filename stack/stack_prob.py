from stack import stack

def is_match(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False

def is_brac_bal(bal_string):
    s = stack()
    is_bal = True
    index = 0
    while index < len(bal_string) and is_bal:
        brac = bal_string[index]
        #print(brac)
        if brac in "({[":
            s.push(brac)
        else:
            if s.is_empty():
                is_bal = False
                break
            else:
                top = s.pop()
                if not is_match(top,brac):
                    is_bal = False
                    break
        index+=1
    if s.is_empty() and is_bal:
        return True
    else:
        return False



print("String : (((({})))) Balanced or not?")
print(is_brac_bal("h"))