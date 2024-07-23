import random
import sys
cpoints = 0
ppoints = 0
tt = int(input("What is the Winning score: \n"))
while(cpoints<tt and ppoints<tt):
    print(f"Comp Score: {cpoints}  Your Score: {ppoints}\n")
    print("Enter 1 for Rock \U0001F44A ,\n2 for Paper \U0001F4DC or\n3 for Scissors ✂️")
    player = input("\nEnter your choice:\n")
    player = int(player)
    
    if(player>3 or player<1): 
        sys.exit("Invalid")
    computer = random.choice("123")
    computer = int(computer)

    choices = {1: "Rock \U0001F44A", 2: "Paper \U0001F4DC", 3: "Scissors ✂️ "}
    player_choice = choices[player]
    computer_choice = choices[computer]

    print(f"{player_choice} X {computer_choice}")

    if player == computer:
        print("\nTie Match!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("\nYou Won!")
        ppoints+=1
    else:
        print("\nComputer Wins!")
        cpoints+=1
