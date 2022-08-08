# functions go here
def yes_no(question):
    valid = False
    while not valid:
        # ask user if they played before
        response = input(question).lower()
        # if yes output 'program continues'
        if response == 'yes' or response == 'y':
            response = "yes"
            return response
        # if no output 'display instructions'
        elif response == 'no' or response == 'n':
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# main route
show_instructions = yes_no("Have you play this game before? ")
print("you chose {}".format(show_instructions))
having_fun = yes_no("Are you having fun? ")
print("you said {} to having fun".format(having_fun))
