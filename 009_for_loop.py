# FOR LOOP

# for char in "hello":
#     print(char)

# for num in [2, 6, 8, 10]:
#     print(num)

# for num in range(2, 13, 2): #start: 2, stop: 13 -> stops the loop
#     print(num)

for x in range(5, 0, -1):
    print(x * x)

animals = ["dog", "cat", "mouse"]
animals_2 = ["cow", "horse", "duck"]

for i, value in enumerate(animals):
    print(i, value)

    # Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))