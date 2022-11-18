def anagrams(str_A, str_B):

    if len(str_A.replace(" ", "")) != len(str_B.replace(" ", "")):
        return False

    x = list(str_A.lower())
    y = list(str_B.lower())
    x.sort()
    y.sort()
    if x == y:
        return True
    return False

print(anagrams('Whoa! Hi!','Hi! Whoa!'))


# str_A = "Whoa! Hi!"

# x = list(str_A) # -> ['a', 'p', 'p', 'l', 'e']
# x.sort() # -> ['a', 'e', 'l', 'p', 'p']
# print(x)

# y = list(str_A).sort() # -> None
# print(y)

