import random


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
lowest = intcheck("what's the smallest number you want to choice?: ", )
highest = intcheck("what's the largest number you want to choice? ", lowest + 1)

num_1 = int(random.randint(lowest, highest))
num_2 = int(random.randint(lowest, highest))
a = num_1 + num_2
answer = ""
#set question
while answer != a:
    try:
        answer = int(input("{} + {} = ".format(num_1, num_2)))

        if answer == a:
            print("Correct, well done")
            continue
        elif answer < a:
            print("Answer wrong, the correct answer is {}".format(a))
            break
        elif answer > a:
            print("Answer wrong, the correct answer is {}".format(a))
            break
        # sets up error messages
        else:
            print("please enter an integer")

    except ValueError:
        print("please enter an integer")
        continue

