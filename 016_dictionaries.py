# dictionaries store mapping from keys to values
empty_dict = {}
dict_1 = {"one": 1, "two": 2, "three": 3}
print(dict_1)
# "one", "two", "three" are keys - they have to be immutable: int, float, string or tuple

# invalid_dixt = {[1, 2, 3]: "123"}
valid_dict = {(1, 2, 3): [1, 2, 3]} # values can be any type
print(valid_dict)

print(dict_1["one"]) # -> 1

# we can get all the keys in ITERABLE 
print(  list(dict_1.keys())     )

# as well as values
print(  list(dict_1.values())   ) #we can also wrap both with tuple

print("one" in dict_1) # True
print( 1 in dict_1) # False

# dict_1["four"] -> non-existing Error
# we can avoid it with get()
print(  dict_1.get("one")   ) # -> 1
print(  dict_1.get("four")   ) # -> None

# we can add default argument if the value is missing
print(  dict_1.get("one", 4)   ) # -> 1
print(  dict_1.get("four", 4)   ) # -> 4

# setdefault() inserts into a dictionary only if the key isn't present
dict_1.setdefault("four", 4)
dict_1.setdefault("three", 5)
print(dict_1)

# adding and overwriting to dictionary
dict_1.update({"five": 5})
print(dict_1)
dict_1.update({"five": 6})
print(dict_1)

del dict_1["one"]

# additional unpacking options
print(  {'a': 1, **{'b': 2}}    ) # {'a': 1, 'b': 2}
print(  {'a': 1, **{'a': 2}}    ) # {'a': 2}