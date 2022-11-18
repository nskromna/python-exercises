# fundamental abstraction. An object that can be treated as a sequence. The object returned by range function is an iterable

dict_1 = {"one": 1, "two": 2, "three": 3}
iterable = dict_1.keys()

# we can loop over it
for i in iterable:
    print(i)

# print(iterable[1]) # TypeError object is not subscriptable

# creating iterator
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # raises a StopIteration exception  and stop the code

iterator = iter(iterable)
# we can loop also over iterator
for i in iterator:
    print(i)

# we can grab elements of iterabe by a list
print(  list(iterable)  )
# with iterator the content wil depends on it's state (which because of for loop is empty now)
print(  list(iterator)  )


