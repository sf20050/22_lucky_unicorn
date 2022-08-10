# functions go here
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

# main routine goes here
how_much = num_check("How much would you like to play with? ", 0, 10)
print("You have asked to play with ${}".format(how_much))
