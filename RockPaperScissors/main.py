import random

choices = [
    "rock",
    "paper",
    "scissors"
]

def play():
    computer = None
    player = None
    playerScore = 0
    computerScore = 0
    
    while playerScore < 3 and computerScore < 3:
        computer = random.choice(choices).lower()
        player = None
        
        while player not in choices:
            player = input("Please choose your weapon rock, paper or scissors ").lower()
        if(player == computer):
            print("Computer's choice is " + computer.upper() + ". It's a tie")
            print("\n")
        elif(player == "rock" and computer == "scissors"):
            playerScore += 1
            print("Computer's choice is " + computer.upper() + ". You won the round.\nYour score: "+ str(playerScore) + " Computer's scoore: " + str(computerScore))
            print("\n")
        elif(player == "paper" and computer == "rock"):
            playerScore += 1
            print("Computer's choice is " + computer.upper() + ". You won the round.\nYour score: "+ str(playerScore) + " Computer's scoore: " + str(computerScore))
            print("\n")
        elif(player == "scissors" and computer == "paper"):
            playerScore += 1
            print("Computer's choice is " + computer.upper() + ". You won the round.\nYour score: "+ str(playerScore) + " Computer's scoore: " + str(computerScore))
            print("\n")
        else:
            computerScore += 1
            print("Computer's choice is " + computer.upper() + ". Computer won the round.\nYour score: "+ str(playerScore) + " Computer's scoore: " + str(computerScore))
            print("\n")
            
    

    if playerScore == 3:
        print("Congrats!! You win the game.")
    else:
        print("Sorry you lost.")

if __name__ == "__main__":
    play()
