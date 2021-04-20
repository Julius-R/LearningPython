# Variables
message = "Welcome, humans"
player_name = "tom riddle"
userName = "  JR403W3-G005   " #Adding whitespace
age = 35

print(player_name.title())
print(userName.strip()) # Stripping whitespace
print(player_name.title() + " is " + str(age)) #str converts int to string

# Casting
x = int(43)
price = round(float((age * 345) / x), 2)

def displayTotal():
    total = "Your total is: " + str(price)
    return total

print(displayTotal())
