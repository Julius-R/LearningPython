# Sets are used to store multiple values in a single variable, similar to a tuple
# The difference is that sets are unordered and unindexed and can not have duplicate values
demo_set = {'apple', 'mango','cherry'}

# You can not access values in a set aside from looping or using the in keyword to check if a value is present
print("apple" in demo_set)
for val in demo_set:
    print(val)
    
# Adding a value to the set
demo_set.add('bananas')
print(demo_set)

# Adding another set
second_set = {'kiwi', 'peach'}
demo_set.update(second_set)
print(demo_set)

# note: update method can be used on any iterable

# You can delete an item from a set using either remove or discard
# remove will throw an error if item does not exist whereas discard will not
demo_set.remove('apple')
demo_set.discard('kiwi')

# clear will empty a set and del will delete the set entirely
demo_set.clear()
print(demo_set)
del demo_set
# print('set is: ' + demo_set) Will throw error since set does not exist

