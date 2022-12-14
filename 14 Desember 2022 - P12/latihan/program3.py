def pascal(n):
    tree = [[1]]  # first row is always just 1
    for x in range(1, n):  # for every other row:
        m = [1]  # it always starts with 1
        for y in range(1, x):  # for all the others:
            # work out what the number is
            m.append(tree[x - 1][y - 1] + tree[x - 1][y])
        m.append(1)  # it always ends in 1
        tree.append(m)  # add the row on
    return tree


x = int(input('Input angka : '))
for v in pascal(x):
    print(v)
