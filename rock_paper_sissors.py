import random

computer_point = 0
player_point = 0

print("Welcome to the rock, paper, sissors game!")
choices = ["rock", "paper", "sissors"]

while True:
    user_input = input("Choose your option(rock, paper, sissors, quit): ")

    if user_input == 'quit':
        break

    computer = random.randint(0,2)
    #0- rock, 1- paper, 2- sissors
    computer_choice = choices[computer]

    print("Computer chose", computer_choice)
    if user_input == 'rock' and computer_choice == 'sissors':
        print("you won!")
        player_point += 1

    elif user_input == 'paper' and computer_choice == 'rock':
        print("you won!")
        player_point += 1

    elif user_input == 'sissors' and computer_choice == 'paper':
        print("you won!")
        player_point += 1
    
    elif user_input == computer_choice:
        print("It was a draw!")
    
    else:
        print("you lost!")
        computer_point += 1


print("computer scored: ",computer_point)
print("Player scored: ", player_point)
quit()
