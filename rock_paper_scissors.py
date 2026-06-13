import random

print("===== ROCK PAPER SCISSORS =====")

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()

computer = random.choice(choices)

print("\nYour Choice:", user)
print("Computer Choice:", computer)

if user == computer:
    print("It's a Tie!")

elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("You Win!")

elif user in choices:
    print("Computer Wins!")

else:
    print("Invalid Input")