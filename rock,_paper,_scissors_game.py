# Importing random module
import random
# Initializing user_score and computer_score.
# Taking the input for number of rounds to play.
user_score, computer_score, n = 0, 0, int(input("Please Enter Numerical (Integer) only\nNumber of rounds to play: "))
# For loop to play number of rounds....
for i in range(n):
  # Displays round number everytime user play
  print(f"\nRound {i+1} of {n} \n")
  # Game parameters --> R -- Rock, P -- Paper, S -- Scissors.
  game_parameters = ["R", "P", "S"]
  # Computer chooses automatically and randomly among (R/P/S) choices.
  computer = random.choice(game_parameters).upper()
  # While loop is to check whether user entering right choice or not....
  while (True):
    user_parameter = str(input("Please Choose among: 'R/r'/'P/p'/'S/s': ")).upper()
    if (user_parameter == "R" or user_parameter == "P" or user_parameter == "S"):
      break
    else:
      print("Choose the right paramter\n") 
  # if user and computer chooses same, it is a tie....
  if (user_parameter == computer):
    print(f"Computer {computer} and user {user_parameter} have choosen same, It's a Tie \n")
  elif ((user_parameter == 'S' and computer == 'R') or (user_parameter == 'P' and computer == 'S') or (user_parameter == 'R' and computer == 'P') ):
    print(f"Computer choosen {computer} and user choosen {user_parameter}, Computer Won this round \n")
    computer_score += 1
  else:
    print(f"Computer choosen {computer} and user choosen {user_parameter}, User Won this round \n")
    user_score += 1

# Displaying the scores of computer and user after number of rounds...
print(f"\nScore of computer after {n} rounds of the game: ", computer_score, f"\nScore of User after {n} rounds of the game: ", user_score)
# Deciding the winner based on score in the rounds...
score = [print("\nUser won the Game") if (user_score > computer_score) else (print("\nComputer score and User score are same, So total game is Drawn")) if (user_score == computer_score) else print("\nComputer won the game")]
