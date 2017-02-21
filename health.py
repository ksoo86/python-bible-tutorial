import random

name = "Keru"
health = random.randint(1,50)
difficulty = 3

#int converts float to int
potion_health = int(random.randint(25,50) / difficulty)

#string manupulation examples
print("Player " + str(name) + " has " + str(health) + "hp at difficulty " + str(difficulty) + ".")
health = health + potion_health
print(str(name) + " drinks potion.")
print(str(name) + " gains " +str(potion_health)+" health.")

print("Player " + str(name) + " has " + str(health) + ".")
