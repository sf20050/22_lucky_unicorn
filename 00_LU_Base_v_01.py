import random


# a Functions go here
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
    statement_generator("How to play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10")
    print()
    print("Then press <enter> to play. you will either get a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1)")
    print()
    print("Can you avoid the donkeys, get the unicorns and walk home with the money??")
    print()
    print("Hint: to quit while your ahead, type 'xxx' instead of pressing <enter>")
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


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{}  {}  {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# main route
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
played_before = yes_no("Have you play this game before? ")

if played_before == "no":
    instructions()

print("program continues")

# ask how much they want to play with
print()
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You have asked to play with ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play... ").lower()
print()
statement_generator("Let's get Started...", "-")
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print rounds played

    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5
    # user gets unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets donkey (subtract $1 to balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even set what user chosen to horse
        if chosen_num % 2 == 0:
            prize_decoration = "H"
            chosen = "horse"

        # otherwise set it to zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "you got a {}. Your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
statement_generator("Results", "=")
print()
print("Final balance", balance)
print("Thank you for playing")
