import random

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def playgame():
    user_score = 0
    computer_score = 0

    while True:
        user_input = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user_input == "exit":
            break

        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(computer_choices)

        result = winner(user_input, computer_choice)
        print(f"User's Choice: {user_input.capitalize()} | Computer's Choice: {computer_choice.capitalize()} | {result}")

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Scores - User: {user_score} | Computer: {computer_score}\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    playgame()
