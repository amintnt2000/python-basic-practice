def split_even_odd(numbers:list):
    result = {'even':[], 'odd':[]}
    for number in numbers:
        if number % 2 == 0:
            result['even'].append(number)
        else:
            result['odd'].append(number)
    return result
print(split_even_odd([2,3,5,13,42,11,7,16,22,4]))