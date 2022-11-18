def chunk(arr, size):
    new_arr = []
    if size >= len(arr):
        new_arr = [arr]
    else:
        sub_arr = []
        for el in arr:
            sub_arr.append(el)

            if len(sub_arr) == size or arr.index(el) == (len(arr) - 1):
                new_arr.append(sub_arr.copy())
                sub_arr.clear()

    return new_arr

print(chunk([1, 2, 3, 4, 5, 6, 7, 8], 10)) 
