films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    
    choice = input("What film would you like to watch? :").strip().title()
    
    if choice in films:
        age = int(input("How old are you?: ").strip())

        # Check user age
        if age >= films[choice][0]:

            num_seats = films[choice][1]
            # check enough seats
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = num_seats - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to watch that film")                
    else:
        print("we don't have that film")
