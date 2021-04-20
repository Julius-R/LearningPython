bufferer = "--------------------------------"
def displayItems(items):
    for x in items:
        print(x)
        
def multiplyNums(num, amount):
    return num * amount


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numsMultipliedByFour = [multiplyNums(i, 4) for i in numbers ]


displayItems(numbers)
print(bufferer)
displayItems(numsMultipliedByFour)

myTuple = ('apple', 'cherry', 'orange', 'peach', 'grape', 'mango')
searchValue = input('What fruit are you looking for? : ')
if searchValue in myTuple:
    print(searchValue + " exists within the tuple")
else:
    print(searchValue + " does not exist")