import random
def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif(user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
def play_game():
    user_score = 0
    computer_score = 0
    print("\n Welcome to Rock, Paper, Scissors Game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\n You choose: {user_choice.capitalize()}")
        print(f"\n computer choose: {computer_choice.capitalize()}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("i'ts a tie!")
        elif winner == "user":
            print("You win this round!")
            user_Score += 1
        else:
            print("computer wins this round!")
            computer_score += 1
        print(f"\n Score -> You: {user_score} | Computer: {computer_score}")
        play_again = input("\n Do you want to play again? (yes\no):").lower()
        if play_again != "yes":
            print("\n Thanks for playing!")
            break
# Start the game
play_game()                   