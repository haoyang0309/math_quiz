#loop game
keep_going = ""
while keep_going == "":
    # How many games want to play
    b = 1
    games = ""
    counter = 0
    while games != b:
        try:
            games = int(input("How many games would you like to play?"))

            if games >= b:
                break
            # sets up error messages
            elif games < b:
                print("please enter an integer more than 0")
            else:
                print("please enter an integer more than 0")

        except ValueError:
            print("please enter an integer more than 0")
            continue
    c = 1
    user_answer = ""
    #set question
    while counter <= games - 1:
        print("Round {} of {} ".format(counter + 1, games))
        try:
            user_answer = int(input("your answer: "))

            if user_answer >= c:
                counter += 1
            # sets up error messages
            elif user_answer < c:
                print("please enter an integer more than 0")
            else:
                print("please enter an integer more than 0")

        except ValueError:
            print("please enter an integer more than 0")
            continue
    keep_going = input("Press <enter> to play again or any key to quit: ")
print("Thank you for playing.  Good bye")