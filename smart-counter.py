def smart_counter(numbers:list):
    odd = []
    even = []
    for number in numbers:
        if number % 2 == 0:
            for i in range(number+1):
                even.append(i)
        else:
            for i in range(number ,-1 ,-1):
                odd.append(i)
    return odd , even

print(smart_counter([2,5]))