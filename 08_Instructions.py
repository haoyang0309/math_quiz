Instructions = ""
YN = ["yes", "no"]
while Instructions != YN:
  Instructions = input("Would you like to read the instructions? ")
  try:
    if Instructions == "yes":
      print("")
      print("Enter the maximum number, minimum number and arithmetic.")
      print("The system will randomize the number between the maximum and minimum numbers you choose and the arithmetic you choose.")
      print("Enter the number of rounds you want to play and you can start your game.") 
      print("Score mechanics will be displayed at the end of the game. ")
      print("If you want to play again, you can press the <Enter> at the end of the game to loop the game.")
      print("")
      print("(If the arithmetic you choose is division, just enter the result and round to the nearest integer.)")
      print("")
      print("Have fun!")
      print("")      
      break
    elif Instructions == "no":
      print("")
      print("Let's start the game, have fun!")
      print("")
      break
    else:
      print("please enter 'yes' or 'no'")
  except ValueError:
    print("please enter 'yes' or 'no'")

