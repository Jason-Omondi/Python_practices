def hint_password(name):
    name = len(name)
    if name <= 5:
        print("Weak passcode!!")
    elif name > 5:
        print("You are good to go!!")
    else:
        print("Invalid input!")

hint_password("bl")
hint_password("inclusive")
