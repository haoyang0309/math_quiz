import random
keep_going = ""
while keep_going == "":
    x = 0
    y = 0
    def intcheck(question, low=None, high=None):

        # sets up error messages
        if low is not None and high is not None:
            error = "please enter + - (1) or  × / (2) or random(3)".format(low, high)
        elif low is not None and high is None:
            error = "please enter an integer that is more than or " \
                    "equal to {}".format(low)
        elif low is None and high is not None:
            error = "please enter an integer that is less than or " \
                    "equal to {}".format(high)
        else:
            error = "please enter an integer"

        while True:

            try:
                response = int(input(question))

                # Checks response is not too low
                if low is not None and response < low:
                    print(error)
                    continue

                if high is not None and response > high:
                    print(error)
                    continue

                return response

            except ValueError:
                print(error)
                continue


    # Main routine
    algorithm1 = ["+", "-"]
    algorithm2 = ["*", "/"]
    algorithm3 = ["+", "-", "*", "/"]
    lowest = intcheck("what's the smallest number you want to choice?: ", )
    highest = intcheck("what's the largest number you want to choice? ", lowest + 1)
    algorithm = intcheck("what's the algorithm you want to choice?"
                         "[ + - (1)   x / (2)   random(3) ", 1, 3)
    b = 1
    games = ""
    counter = 0
    while games != b:
        try:
            games = int(input("How many games would you like to play?"))
            print("")

            if games >= b:
                break
            elif games < b:
                print("please enter an integer more than 0")
            else:
                print("please enter an integer more than 0")

        except ValueError:
            print("please enter an integer more than 0")
            continue

    answer = ""
    while counter <= games - 1:
        print("Round {} of {} ".format(counter + 1, games))
        if algorithm == 1:
            algorithm_random = random.choice(algorithm1)
        elif algorithm == 2:
            algorithm_random = random.choice(algorithm2)
        elif algorithm == 3:
            algorithm_random = random.choice(algorithm3)
        num_1 = int(random.randint(lowest, highest))
        num_2 = int(random.randint(lowest, highest))
        if algorithm_random == "+":
            A = num_1 + num_2
        elif algorithm_random == "-":
            A = num_1 - num_2
        elif algorithm_random == "*":
            A = num_1 * num_2
        elif algorithm_random == "/":
            A = num_1 / num_2
        a = round(A)
        while answer != a:
            try:
                answer = int(input("{} {} {} = ".format(num_1, algorithm_random, num_2)))

                if answer == a:
                    print("Correct, well done")
                    print("")
                    counter += 1
                    x += 1
                    continue
                elif answer < a:
                    print("Answer wrong, the correct answer is {}".format(a))
                    print("")
                    counter += 1
                    y += 1
                    break
                elif answer > a:
                    print("Answer wrong, the correct answer is {}".format(a))
                    print("")
                    counter += 1
                    y += 1
                    break
                else:
                    print("please enter an integer")

            except ValueError:
                print("please enter an integer")
                continue
    print("")
    print("***** End Game Summary *****")
    print(" Correct: {}  |   Wrong: {} ".format(x, y))
    print("****************************")
    print("")
    keep_going = input("Press <enter> to play again or any key to quit: ")
print("Thank you for playing.  Good bye")