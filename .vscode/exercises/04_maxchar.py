def max_char(str):
    char_map = {}
    for letter in str:
        if letter in char_map:
            char_map[letter] += 1
        else:
            char_map.update({letter: 1})
    # Sol. 1
    # char_map_vals = list(char_map.values())
    # max_count = max(char_map_vals)
    # max_count_idx = char_map_vals.index(max_count)
    # char_max = list(char_map.keys())[max_count_idx]

    # Sol. 2
    char_max = max(char_map, key = char_map.get)

    return char_max

print(max_char('ab1c1d1e1f1g1'))
