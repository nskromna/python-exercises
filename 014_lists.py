# lists store sequences
li = []
other_li = [1, 2, 3]

# adding elements at the end
li.append(4)
li.append(5)
li.append(6)
li.append(3)

print(li)

# removing last item
li.pop()
print(li)
li.append(3)

print(li[0]) # first element
print(li[-1]) # last element
# print(li[4]) # index error - list index out of range

print(li[1:]) # from 2nd to the end
print(li[:2]) # from the start to the 3rd element (excluding)
print(li[1:3]) # form the second to the fourth (excluding)
print(li[1::2]) # from all with step = 2 starting with index = 1
print(li[::-1]) # step -1 starting from last index (reverse order)

del li[1] # delete item
print(li)
li += [3, 4, 6, 3, 2] # concatenating two lists
li.extend([2, 2]) # ocncatenating with different method
print(li)

li.remove(3) # removes the first found element
print(li)
# li.remove(1) # ValueError -> 1 is not on the list

li2 = li[:]
print(li2 == li) # True
print(li2 is li) # False

print(1 in li) # False
print(2 in li) # True

print(len(li)) # length
