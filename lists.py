# Lists are collections of items in an order
names = ['jason', 'hagrid', 'marik']
print(names[1].title()) #being fancy ;)

# Adding items to a list
# At the end
names.append('nessa')
print(names)

# inserting values at specified location
names.insert(2, 'eren')
print(names)

# Removing items
# using del
del names[1]
print(names)

# using the pop method
removedName = names.pop()
firstName = names.pop(0)
print(names)

# using the remove method
names.remove('eren')
print(names)
# Special note, remove only removes the FIRST instance in the list

#  List organization
names = ['jason', 'hagrid', 'marik'] # reinitalization for sorting
print("Unsorted list of names: " + str(names))
# sorted method, allows for sorting temporarily
print(sorted(names))

# sort method, permanately sorts the list
names.sort()
names.sort(reverse = True) # allows sort in reverse alphabetical order
print(names)

# reverse method, allows you to reverse a list's order
print(names.reverse()) # note, it reverses the ORDER of the list, not alphabetically

print(len(names)) # prints the length of the list

# looping through a list
userInput = ['jotaro', 'amelia', 'ryo']
for name in userInput:
    names.append(name)
    print(name.title() + ", welcome to the team!")

print(names)

# dealing with lists of numbers in python
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
