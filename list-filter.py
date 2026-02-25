def list_filter(numbers:list):
    bigger = []
    avg = sum(numbers) / len(numbers)
    for number in numbers:
        if number >= avg:
            bigger.append(number)

    return bigger , round(avg, 3)

the_list , average = list_filter([2,13,4,5,7,15,22])
print(f'Average is: {average}')
print(f'the number above average is: {the_list}')