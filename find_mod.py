def find_mod(numbers:list):
    if not numbers:
        return None
    mode = None
    max_count = 0
    for i in range(len(numbers)):
        current = numbers[i]
        count = 0
        for j in range(len(numbers)):
            if numbers[j] == current:
                count += 1
        if count > max_count:
            max_count = count
            mode = current
    return mode
print(find_mod([1,1,1,2,3,3,3,4,4,4,4,5,5,4,3]))
