# Checks user input (either full word or first letter of word)
def string_checker(question, to_check):

valid = False
while not valid:
  # ask user question and change response to lowercase
  response = input(question).lower()

  if response == "xxx":
    return response

  # check response is in list OR that it's the first letter of an item in the list
  for item in to_check:
    if response == item:
      return response
    elif response == item[0]:
      return item

  # if item not in list, print error
  print("please enter 'yes' or 'no'")

# the instructions
def instructions():

instructions = string_checker("Would you like to read the instructions? ", ["yes", "no"])
# Users don’t want to read instructions
if instructions == "no":
  print("")
  print("Let's start the game, have fun!")
  print("")
# User wants to read instructions
else:
  print("")
  print("Enter the maximum number, minimum number and arithmetic.")
  print("The system will randomize the number between the maximum and minimum numbers you choose and the arithmetic you choose.")
  print("Enter the number of rounds you want to play and you can start your game.") 
  print("Score mechanics will be displayed at the end of the game. ")
  print("If you want to play again, you can press the <Enter> at the end of the game to loop the game.")
  print("")
  print("(If the algorithm is division, the quotient and divisor will be the number between the minimum and maximum selected by you.)")
  print("")
  print("Have fun!")
  print("")  
instructions()