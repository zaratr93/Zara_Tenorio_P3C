import random
options = ("rock", "paper", "scissors")

def stars(text):
    suga = "*"* 10
    V = "*"* 5
    print(f"{suga}{text}{V}")
    
    
while True:
    user_choice = input("choose rock, paper, scissors ")
    computer_choice = random.choice(options)
    stars(computer_choice)
    
    
    if user_choice == "quit":
        stars("End of the game")
        break

    if user_choice not in options:
        stars("thats not allowed")
        continue
   
    if user_choice == computer_choice:
        stars("its a tie")
    
    elif((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock")):
        stars("you won")
    
    else:
        stars("you lose")
    

    

