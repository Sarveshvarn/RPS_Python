import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:

    player = None
    # Computer Choice
    computer = random.choice(options)

    # User Choice
    while player not in options:
        player = input("Enter a Choice (Rock, Paper, Scissors): ")
    
    #Printing the choices
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Results
    # TIE
    if player == computer:
        print("Its a TIE!")

    # PLAYER WINNING
    if player == "Rock" and computer == "Scissors":
        print("Player wins!")
    elif player == "Paper" and computer == "Rock":
        print("Player wins!")
    elif player == "Scissors" and computer == "Paper":
        print("Player wins!")

    # COMPUTER WINNING
    if player == "Scissors" and computer == "Rock":
        print("Computer wins!")
    elif player == "Rock" and computer == "Paper":
        print("Computer wins!")
    elif player == "Paper" and computer == "Scissors":
        print("Computer wins!")

    a = input("Play Again? (y/n): ")
    if not a.lower() == "y":
        running = False

print("Thank for playing")