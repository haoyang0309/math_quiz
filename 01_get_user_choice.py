def intcheck(question, low = None, high = None):

    # sets up error messages
    if low is not None and high is not None:
        error = "please enter + - (1) or  × / (2) or random(3)".format(low,high)
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

lowest = intcheck("what's the smallest number you want to choice?: ",  )
highest = intcheck("what's the largest number you want to choice? ", lowest + 1)
algorithm = intcheck("what's the algorithm you want to choice?"
"[ + - (1)   x / (2)   random(3) ", 1,3)

