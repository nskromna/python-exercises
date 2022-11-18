# print('Guess the name:')
# name = input()

# if name == 'Arya Stark':
#     print('Valar Morghulis')
# elif name == 'Jon Snow':
#     print('You know nothing')
# else:
#     print('Carry on')

x = 1
print(x is 1) #x == 1 --> True
print(x is 0) #x == 0 --> False

# naturally false are False, empty object, empty string, None, zero

a = 1
a == 1 # True
a is 1 # True

a = [1, 2, 3]
b = [1, 2, 3]
a == b # True
a is b # False
#is checks if a and b has the same place in memory, 
# they HAVE to be the same object
# the exact same piece of memory

c = b
b is c # True
