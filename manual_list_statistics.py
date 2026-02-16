def manual_lists_statistics(numbers:list):
    if not numbers:
        return None
    total = 0
    count = 0
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers:
        if isinstance(number , (int , float)):
            if number > maximum:
                maximum = number
            elif number < minimum:
                minimum = number
            total += number
            count += 1
    avg = total / count
    return avg , maximum , minimum
average , maximum , minimum = manual_lists_statistics([1,2,3,4,5,6,7,8,'9','10'])
print(average)
print(maximum)
print(minimum)