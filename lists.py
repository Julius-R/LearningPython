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