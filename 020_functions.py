def add(x, y):
    print(f"x is {x} and y is {y}")
    return x + y

print(add(2, 3))
print(add(y=2, x=3))

# not defined number of arguments
def varargs(*args):
    return args

print(varargs([1], 2, 3))

# variable number of keyword arguments
def keyword_args(**kwargs):
    return kwargs

print(keyword_args(big="foot", loch="ness"))

# both at once
def all_args(*args, **kwargs):
    print(args)
    print(kwargs)

all_args(1, 2, a=3, b=4)

# you can use * and ** also to unpack args and kwargs
print(   varargs(*(2, 3, 4))    )
print(  keyword_args(**{'a': 3, 'b': 4})    )

# first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3)) # -> 13

# anonymous function LAMBDA
print(  (lambda x: x > 2)(3)    ) # True
print(  (lambda x, y: x ** 2 + y ** 2)(2, 1)    ) # -> 5

# There are lots of buld-in higher order functions

# we ca use list comprehensions for nice maps and filters
print(  [add_10(i) for i in [1, 2, 3]]  ) # -> [11, 12, 13]

print(  [x for x in [3, 4, 5, 6, 7] if x > 5]) # -> [6, 7]

print(  {x for x in 'abcddeef' if x not in 'abc'}) # -> {'d', 'e', 'f'}

print(  {x: x**2 for x in range(5)}) # -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

dict_1 = {x: x**2 for x in range(5)}
dict_1 = {x: x**2 for x in range(3,6)} # overwrite, use update() instead
print(dict_1)
