# There are three wats to define a module in Python: in Python, in C, and using built in modules

# To access contents, use the import keyword
import mod

print(mod.s)
mod.hello('Jason')
j = mod.Person('James')
j.sayName()

# When the interoreter executes an imoprt statement it searches for the mod.py in a list of directories that are curated from the following sources: The directory the script was called in, the list of directories from the PYTHONPATH env variable set in the os, an installation-dependent list configured at the time Python was installed

# If you only want to import certain things from a file, use the following code
# from <module_name> imort <name(s)?

# import pkg.mod1, pkg.mod2
# pkg.mod1.speak()

# Package initialization
from pkg import *
mod1.speak()
mod2.talk()