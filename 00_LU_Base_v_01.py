# aFunctions go here
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


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))
            # if the amount is too low / too high to give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# main route
played_before = yes_no("Have you play this game before? ")

if played_before == "no":
    instructions()

print("program continues")

# ask how much they want to play with

how_much = num_check("How much would you like to play with? ", 0, 10)
print("You have asked to play with ${}".format(how_much))
