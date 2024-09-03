print("This is a new file")
import random
while True:
    T_number = random.randint(1,10)
    INVALID = 10
    guess = input(" ")
    if int(guess) < T_number:
        print("Your guess is too low")
        if int(guess) > T_number:
            print ("Your guess is too high")
            if int(guess) == T_number:
                print ("Your guess is correct")
                if int(guess) > INVALID:
                    print("I dont know what youre talking about")
               