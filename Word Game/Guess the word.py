from random import randint
from pickle import *

def add():
    with open('game.dat','ab') as f:
        word = (input('Enter Word:\n')).lower()
        clue = []
        for _ in range(5):
            c = input('Enter Clue:\n')
            clue.append(c)
        
        data = {word : clue}
        dump(data,f)
        print('Added Successfully')

def readCounter():
    c = 0
    with open('game.dat','rb') as f:
        while 1:
            try:
                x = load(f)
                c+=1
            except EOFError:
                break
        return c

def generator():
    f = open('game.dat','rb')
    s = 5
    c = 0
    n = readCounter()
    y = randint(1,n)
    for _ in range(y):
        d = load(f)
        for a in d:
            for i in range(5):
                print(d[a][i])
                choice = (input('Guess The Word:\n')).lower()
                if choice == a:
                    print(f'Correct!\nYour Score is {s}')
                    break
                else:
                    s-=1
                if s == 0:
                    print (f'the word was {a}')
    f.close()

while True:
    choice = int(input('1.Input a Word and Clues\n2.Return number of records\n3.Play\n4.Exit\n'))
    if choice == 1:
        add()
    elif choice ==2:
        print(readCounter())
    elif choice == 3:
        generator()
    else:
        break
    
        
