# They're immutable
tup = (1, 2, 3)
print(tup[0])
#tup[0] = 3 # TypeError: 'tuple' object does not support item assignment

# tuple of length = 1 must have a comma at the end, other lengths don't
type((1)) # int
type((1,)) # tuple
type(()) # tuple

print(len(tup))
tup + (4, 5, 6)
print(tup)
print(tup[:2]) # (1, 2)
print(2 in tup) # True

# unpacking into variables (can be done as well with lists)
a, b, c = (1, 2, 3) # a = 1, b = 2, c = 3
a, *b, c = (1, 2, 3, 4) # a = 1, b = [2, 3], c = 4
d, e, f = 4, 5, 6 # tuple is created by default without typing parentheses
# d = 4, e = 5, f = 6
e, d = d, e # e = 4, d = 5
