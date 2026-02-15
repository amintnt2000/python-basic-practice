def sum_of_products(numbers:list):
    total = 0
    count = 0
    flat = []
    for number in numbers:
        if isinstance(number, int):
            total += number
            count += 1
            flat.append(number)
        else:
            s,c,f = sum_of_products(number)
            total += s
            count += c
            flat.extend(f)
    return total, count, flat
total, count, flat = sum_of_products([1,2,3,4,5,[[6,7],8,9]])
print('taotal is:',total)
print(count)
print(flat)
