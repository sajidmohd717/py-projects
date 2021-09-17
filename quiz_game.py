point = 0
print("Welcome to my computer quiz!")
play = input("Do you want to play? (yes/no)")
if play == "yes":
    print("Okay! Let's play :D")
else:
    quit()

answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    point += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit" :
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory" :
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for?")
if answer.lower() == "read only memory" :
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

print("Congratulations you got " + str(point/4.0 * 100) + "% correct!")


