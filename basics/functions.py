# functions work the same as in most other languages, here are some differences I found
# Arbitrary Arguments - *args
def say_names(*names):
    print(names[1])
    
say_names('Jake', 'Miles')

# keyword arguments provide a way to have arguments provided out of order
def keyword_args(name1, name3, name2,):
    print(name3)
    
keyword_args(name2 = 'Jake', name1 = 'Janice', name3 = 'Paul')

# Arbitrary keyword args **kwargs
def arbitrary(**args):
    print(args['name'])
    
arbitrary(name = 'Jane', lname = 'Pike')

# Pass - used in a function since functions can not be empty
def rando_func():
    pass

# lambdas
# A lambda is an anonymous function that can take numerous args and only one expression
# Syntax - lambda arguments : expression
x = lambda a : a + 10
print(x(4))

def my_lambda(n):
    return lambda a : a * n

my_tripler = my_lambda(3)
my_doubler = my_lambda(2)
print(my_doubler(5))
print(my_tripler(5))





