b = 1
games = ""
counter = 0
while games != b:
    try:
        games = int(input("How many games would you like to play?"))

        if games >= b:
            break
        elif games < b:
            print("please enter an integer more than 0")
        else:
            print("please enter an integer more than 0")

    except ValueError:
        print("please enter an integer more than 0")
        continue
c = 1
user_answer = ""
while counter <= games - 1:
    print("Round {} of {} ".format(counter + 1, games))
    try:
        user_answer = int(input("your answer: "))

        if user_answer >= c:
            counter += 1
        elif user_answer < c:
            print("please enter an integer more than 0")
        else:
            print("please enter an integer more than 0")

    except ValueError:
        print("please enter an integer more than 0")
        continue