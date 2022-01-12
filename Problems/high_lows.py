num_list = [20, 9, 51, 81, 50, 42, 77]

def count_low_high(num_list):
    high = list(filter(lambda n : n > 50 or n %3 == 0 , num_list))
    low = list(filter(lambda n: n <= 50 and not n % 3 == 0 , num_list ))
    return [len(high) , len(low)]

print(count_low_high(num_list))

