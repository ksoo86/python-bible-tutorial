#Travis is a security bot which stores a list of users and adds users if they are not on the list


known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry","Alice"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        #strip and lower is just best practice for string input detection
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        
        if remove == "y":
            #remove() - Removes first occurrence of the name
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyways!")
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add_me == "y":
            #append() - Adds to list
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")

            
        
    
