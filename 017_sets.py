empty_set = set()

set_1 = {1, 1, 2, 2, 3, 4} # {1, 2, 3, 4}

# SETS DO NOT HAVE DUPLICATE ELEMENTS!

# elements of a set have to be immutable
# invalid_set = {[1], 1} # TypeError -> unhshable type "list"
valid_set = {(1,), 1}

set_2 = set_1

# adding elements
set_2.add(5) # {1, 2, 3, 4, 5}
set_2.add(5) # the same as above

set_3 = {3, 4, 5, 6}
print(set_2)
print(set_3)
print(  set_2 & set_3   ) # -> intersection {3, 4, 5}
print(  set_2 | set_3   ) # -> union {1, 2, 3, 4, 5, 6}
print(  set_2 - set_3   ) # -> differnce {1, 2}
print(  set_2 ^ set_3   ) # -> symmetric difference {1, 2, 6}

print(  {1, 2} >= {1, 2, 3}     ) # False
print(  {1, 2} <= {1, 2, 3}     ) # True

print(  2 in set_2  ) # True

set_2 = set_1.copy()
print(set_2 is set_1) # False