# def reverse_string(str):
#     rev_str = str[::-1]
#     return ''.join(rev_str)

# LOOP

def reverse_string(str):
    rev_str = ''
    for idx, letter in enumerate(str):
        rev_str = str[idx] + rev_str
    return rev_str

print(  reverse_string('Hey you!') )