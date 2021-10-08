from random import *

player_score = 0
computer_score = 0
colors = ['red','blue','green','black','white']

while player_score < 100 and computer_score < 100:
    number = int(input('Enter Number Between 1-10\n'))
    alpha = input('Enter Capital Alphabet \n')
    color = input('Enter Color  \n')

    cnum = randint(0,10)
    calpha = chr(randint(65,90))
    ccolor = colors[randint(-1,4)]

    print(cnum,calpha,ccolor)
    
    if number == cnum:
        player_score += 5
    else:
        computer_score += 5

    if alpha == calpha :
        player_score += 5
    else:
        computer_score += 5

    if color == ccolor:    
        player_score += 5
    else:
        computer_score += 5

    print('Computer Score:',computer_score)
    print('Player Score:',player_score)

if computer_score>player_score:
    print('Computer Won')
else:
    print('Player Won')
    
