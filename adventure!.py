name = input('What is your name?: ')
print('\n\nWelcome to the mighty adventure young adventurer', name, "!!")
print('You would be given multiple choices and only one of them will lead you to your freedom')
print('\n\nYou woke up and realized you were in a middle of the jungle and are very scared, you look around you and its all trees and plants everywhere')
answer = input('''All of a sudden, you see a tiger coming towards you, so you 
decide you should pretend you are dead or start running for your life (pretend/run)\n''')
while True:
    if answer == 'run':
        print("\nYou are much slower than the tiger and the tiger caught up to you and ate you")
        break
    elif answer == 'pretend':
        print("\nThe tiger sniffed you for a couple of times and started to notice that you arn't a threat for him so he started becoming your friend")
        print('''\nYou were absolutely amazed by this and dedide to play along with the tiger. 
You realized that if you were at one spot doing nothing, you will eventually die so you start walking towards a gushing noise,
sounding like a river in order to find some life''')
        answer = input('now you are wondering if you should walk towards the river or continue to play with the tiger(play/walk)')
        if answer == 'play':
            print('''you continue to play with the tiger and now the tiger brings gets hungry and starts walking.
 You just realized that you had a compass and take a look at it.
 It was going north''')
            print('\nSoon you earnt your freedom. Good job young adventurer, hope to see you again!!!\n\n')
            exit()

        elif answer == 'walk':
            print("The tiger did not like that you wern't paying attention to it, so it ate you")
            break
            
            


print('Nice try, hope to see you again!')
exit()
