# Tuples are used to store multiple items in a single variable
# They are ordered, immutable, and ALLOW duplicates
myTuple = ('apple', 'cherry', 'orange', 'peach', 'grape', 'mango')

# Accesing items in a tuple are
print(myTuple[1])

# Negative Indexing
print(myTuple[-1])
print(myTuple[-2])

# Range of indexes
print(myTuple[2:5])

# Check if item exists in Tuple
searchValue = "peach"
if searchValue in myTuple:
    print(searchValue + " exists within the tuple")
else:
    print(searchValue + " does not exist")
    
# Unpacking a tuple - works similar to destructuring in JS
# Any items not unpacked must be turned into a list using *
(tasty, yuck, yum, *remainderItems) = myTuple
print(yum)
print(remainderItems)

# Join tuples
myNewTuple = myTuple + myTuple
print(myNewTuple)

# Multiply tuples
myMulTuple = myTuple * 4
print(myMulTuple)

print(myMulTuple.count(searchValue)) 

print(myTuple.index("apple"))