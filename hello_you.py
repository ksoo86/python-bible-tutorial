# Ask user for name
name = input('What is your name?: ')

# Ask user for age
age = input("What is your age?: ")

# Ask user for city
city = input("What city are you from?: ")

# Ask user what they enjoy
love = input(" What do you enjoy doing?: ")

# Create output text
#Manual  method of outputting string
print( str(name) + " " + str(age) + " " + str(city) + " " + str(love))

#Formatted method of outputting string
string = "Your name is {0} and you are {1} years old. You live in {2} and you love {3}."
output = string.format(name,age,city,love)


# Print output to screen
print(output)
