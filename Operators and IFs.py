guess = input("guess a number bethween 1 and 10: ")
INVALID = 10
if int(guess) > 3:print("Your guess is too high")
if int(guess) == 3:print("You are right")
if int(guess) < 3:print("Your guess is too low")
if int(guess) > INVALID:print("I thought you were smarter, youre number is invalid")
 