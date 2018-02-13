known_users = ["Alex", "Nisse", "Fred", "Harry", "Bob"]

while True:
    print("Hi, I'm Jeeves the bot")

    your_name = input("What's your name?: ").strip().capitalize()
    if your_name in known_users:
        print("Access granted, Welcome {}".format(your_name))
        remove = input("Should I delete you from the system? (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(your_name)
        elif remove == "n":
            print("I'm glad you decided to stay {}".format(your_name))

    else:
        print("Access denied, name NOT recognized")
        add_me = input("Would you like to be added to the system? (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(your_name.capitalize())
            print("The system is updated. Welcome {}".format(your_name))
        elif add_me == "n":
            print("No worries, I didn't want you in the system anyway!")
    break
