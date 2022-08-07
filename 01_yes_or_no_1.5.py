show_instructions = ""
while show_instructions != "xxx":
    show_instructions = input("Have you played this game before? ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    elif show_instructions == "no" or show_instructions == "y":
        print("display instructions")

    else:
        print("please answer yes / no")

    print("you chose {}".format(show_instructions))


