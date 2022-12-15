def find_max(*numbers):
    m = numbers[0]
    for n in numbers[1:]:
        if (n > m):
            m = n

    return m


largest_number = find_max(1, 5, 2, 6, 9, 1, 44, 12, 77)
print(largest_number)
