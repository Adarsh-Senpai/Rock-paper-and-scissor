import random

# Step 1: Define the choices and initialize scores
choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

# Step 2: Display instructions
def display_instructions():
    print("\n--- Welcome to Rock, Paper, Scissors Game ---")
    print("Instructions:")
    print("1. Choose either 'rock', 'paper', or 'scissors'.")
    print("2. The computer will randomly choose one as well.")
    print("3. Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("4. You will be informed whether you win, lose, or it's a tie.")
    print("5. Scores will be tracked, and you can play multiple rounds.\n")

# Step 3: Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

# Step 4: Main game loop with user-friendly interface
def play_game():
    display_instructions()  # Display the instructions at the start
    
    while True:
        print(f"\nYour Score: {user_score} | Computer Score: {computer_score}")
        
        # Step 5: User input
        user_choice = input("Please enter your choice (rock, paper, or scissors): ").lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        # Step 6: Computer choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Step 7: Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Step 8: Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n--- Final Score ---")
            print(f"Your Score: {user_score} | Computer Score: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
