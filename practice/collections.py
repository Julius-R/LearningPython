bufferer = "--------------------------------"
def display_items(items):
    for x in items:
        print(x)
        
def multiply_nums(num, amount):
    return num * amount


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_multiplied_by_four = [multiply_nums(i, 4) for i in numbers ]


display_items(numbers)
print(bufferer)
display_items(nums_multiplied_by_four)

myTuple = ('apple', 'cherry', 'orange', 'peach', 'grape', 'mango')
search_values = list()

def get_input_from_user():
    num_vals_to_add = input('How many values to add?')
    count = 0
    while count < int(num_vals_to_add):
        value = input('What would you like to add to the array? : ')
        search_values.append(value)
        count += 1
    
def does_val_exist(arr):
    val_exists = False
    for val in arr:
        if val in myTuple:
            val_exists = True
            break
        else:
            val_exists = False
    return val_exists

get_input_from_user()
display_items(search_values)
print(does_val_exist(search_values))