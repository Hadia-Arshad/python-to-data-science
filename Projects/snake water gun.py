import random # to make random choices
choices = ['s', 'w', 'g'] # snake water gun

def check_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == 's' and computer == "w") or \
        (player == 'w' and computer =='g') or \
        (player == 'g' and computer == 's'):
        return "player"
    else:
        return "computer"
while True:
    player_choice = input("Enter your choice(s for Snake, w for Water, g for Gun):)").lower()
    while player_choice not in choices:
      print("invalid choice! Try again")
      player_choice = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    computer_choice = random.choice(choices)
    result = check_winner(player_choice, computer_choice)
    print(f"you chose: {player_choice}")
    print(f"computer chose: {computer_choice}")
    if result == "draw":
        print("it is a draw!")
    elif result == "player":
       print("you win!")
    else:
        print("computer win!")
    play_again = input("Do you want to play again? (yes/no):").lower()
    if play_again != "yes":
        print("thanks for playing")
        break