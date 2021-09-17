import random

count = 0;
print("Welcome to the number gussing game!")
print("Guess a number from 0 to ")
upper_limit = input("Type a number: ")

if upper_limit.isdigit():
    upper_limit = int(upper_limit)
else:
    print("Please enter a number next time")
    exit()

number = random.randint(0, upper_limit+1)

while True:
    guess = input("Make a guess :")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a number next time")
        exit()
    
    if guess == number:
        print("Correct!")
        count += 1
        print("you took a total of", count, "tries")
        break
    elif guess>number:
        print("You were above the number")
        count += 1
    else:
        print("You were below the number")
        count += 1

exit()





