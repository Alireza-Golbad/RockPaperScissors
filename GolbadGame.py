import random
print("rock")
print("paper")
print("scissors")
print("----------------")

randomNumber = random.randint(0, 2)
computerMove = "rock"
if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
else:
    computerMove = "scissors"
player1_wins = 0
computer_wins = 0
winningScore = 4

while player1_wins < winningScore and computer_wins < winningScore:
    print(f"player1 : {player1_wins} and computer : {computer_wins}")
    player1_move = input("player1 please make your move ").lower()
    if player1_move == "q" or player1_move == "quit":
        break
    print(f"player1 move: {player1_move}")
    print(f"computer move: {computerMove}")
    if player1_move == computerMove:
        print("that's a tie...")
    elif player1_move == "rock":
        if computerMove == "paper":
            print("computer wins")
            computer_wins += 1
        elif computerMove == "scissors":
            print("player1 wins")
            player1_wins += 1
    elif player1_move == "paper":
        if computerMove == "scissors":
            print("computer wins")
            computer_wins += 1
        elif computerMove == "rock":
            print("player1 wins")
            player1_wins += 1
    elif player1_move == "scissors":
        if computerMove == "rock":
            print("computer wins")
            computer_wins += 1
        elif computerMove == "paper":
            print("player1 wins")
            player1_wins += 1
    else:
        print("something went wrong")
print(f"Final score** player1 : {player1_wins} | computer : {computer_wins}")
