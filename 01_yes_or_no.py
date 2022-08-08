# ask user if they played before
show_instructions = input("Have you played this game before? ").lower()
# if the say yes , out 'program continues'
if show_instructions == "yes":
    print("program continues")

elif show_instructions == "y":
    print("program continues")
# display instructions if answer is no
elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

else:
    print("please answer yes / no")

print("you chose {}".format(show_instructions))


