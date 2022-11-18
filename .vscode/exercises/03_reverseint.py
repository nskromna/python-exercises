def reverse_int(x):
    int_str = str(x)

    if x < 0:
        return (-1) * int(int_str[:0:-1])
    return int(int_str[::-1])


print(reverse_int(-9262))