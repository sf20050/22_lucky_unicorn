# ask user if played before
show_instructions = ""
while show_instructions != "xxx":
    show_instructions = input("Have you played this game before? ").lower()

    # set up loop to force valid input

    # if answer is yes program continues
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    # display instructions if answer is no
    elif show_instructions == "no" or show_instructions == "y":
        print("display instructions")

    else:
        print("please answer yes / no")

    print("you chose {}".format(show_instructions))


