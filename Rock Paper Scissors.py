import.random
options = ("rock", "paper", "scissors")

print(computer_choice)
while True:
    user_choice = input("choose rock, paper, scissors ")
    computer_choice = random.choice(options)
    
if user_choice == "quit":
    print("End of the game")
    break

if user_choice == "":
    print("thats not allowed")
   
if user_choice == computer_choice
    print("its a tie")
    
elif((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock")):
    print("you won")
    
else:
    print("you lose")
    

    

