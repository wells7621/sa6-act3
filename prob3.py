def find_max_num(numbers, compare):
    max = numbers[0]

    for num in numbers:
        if compare(max, num) <= num:
            max = num

    return max



numbers = [23, 4, 55, 12]

max_num = find_max_num(numbers, lambda x, y: x if x > y else y)

print(max_num)