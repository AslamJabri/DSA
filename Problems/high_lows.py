num_list = [20, 9, 51, 81, 50, 42, 77]

def count_low_high(num_list):
    high = list(filter(lambda n : n > 50 or n %3 == 0 , num_list))
    low = list(filter(lambda n: n <= 50 and not n % 3 == 0 , num_list ))
    return [len(high) , len(low)]

print(count_low_high(num_list))

#ALternate
def count_low_high(num_list):
    if (len(num_list)==0):
        return None
    high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
    low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
    return [low_list, high_list]


num_list = [20, 9, 51, 81, 50, 42, 77]

print(count_low_high(num_list))