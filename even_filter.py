def even_filter(numbers:list):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number*2)
    return even_numbers
print(even_filter([3, 8, 11, 20, 7, 14]))