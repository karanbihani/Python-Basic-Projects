#Battleship

#REMOVE PRINT COORDINATES

import random
board1 = [[' 1  ','2  ','3  ','4  ','5  ','6  ','7  ','8  ','9  '],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "]]
board2 = [[' 1  ','2  ','3  ','4  ','5  ','6  ','7  ','8  ','9  '],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "],[" - "," - "," - "," - "," - "," - "," - "," - "," - "]]

def bdprint(board):
    for gt in board:
        for element in gt:
            print(element,end="  ")
        print("\n")
bdprint(board1)
man=input('DO you want basic instructions on how o play this game:Y/N:')
if man.upper()=='Y':
    print("There are 3 ships of length 4 coordinate so you choose 1 and is vertical or horizontal (its a 10*10 grid game) so total you have 12 positions and so does your enenmy now you just guess so if you hit on one you know one more position is top bottom left or right .To win the game hit all the enenmy's positions (12 or less)")
    print("For further instructions :","https://www.youtube.com/watch?v=RY4nAyRgkLo")
else:
    pass

print('Single player or Muliplayer Mde - S/M')
op=input('single or multi player')

if op.lower()=='s':
        c=[]
        for i in range(3):
            x=random.randint(0,11)
            y=random.randint(0,11)
            m=[x,y]
            r=random.randrange(0,2)
            if r==1 :
                for i in range(4):
                    N=[x,y]
                    x+=1
                    if N in c:
                        continue
                    c.append(N)
            else:
                for i in range(4):
                    N=[x,y]
                    y+=1
                    if N in c:
                        continue
                    c.append(N) 
            print(c)
        l=[]
        h=0
        while h<=40:
            bdprint(board1)
            h+=1
            
       
            n=input("location coordinates to blow it UP")

            x=int(n[0])
            y=int(n[2])

            if n in l:
                print("Sorry you already tried this location,you lose a chance")
            
            if n in c:
                    print("That's a HIT")
                    c.remove(n)
                    print ("No. of locations where ships are still present:",len(c))
                    board1[y][x-1]=' X '
                    if len(c)==0:
                        print("You WIN")
                        break
                    else:
                        pass
            
            if n==[69,420]:
                    c=[]
                    print("Cheats have been activated")
                    for i in range(0,10):
                            print (i,end='   ')
                    print('\n')
                    for i in range (1,10):
                        print (i,end='   ')
                        print(print('   '.join(['X'] * 10)),end='\n\n')
                    if len(c)==0:
                        print("You WON")
                        break
            else:
                    print ("No ship was present there")
                    board1[y][x-1]=' * '
            print('No. of enemy ships locations left:',len(c))
            l.append(n)
            print("Chances: ",h,"/40",sep='')
            
        
         
else:
    P1=input("Name of player 1")
    P2=input("Name of player 2")
    p1=[]
    p2=[]

    '''stores the coordinates of the ships'''

    print(P1,"please input the location of your ships")
    for abcdefg in range(3):
    
        a=(input("enter coordinates WHOLE NO. (between 1-10) form for the ship it is a 10*10 grid ,FOR VERTICAL 1-9,1-6 ,FOR HORIZONTAL 1-6,1-9\n"))
        p=input("H-Horizontal or V-vertical")
        
        x=int(a[0])
        y=int(a[2])
        
        if p =="H" or p=='h' :
            if x<1 or y<1 or x>5:
                print ("Input invalid for wrong input you lose 1 ship")
            for i in range(4):
                n=[x,y]
                x+=1
                if n in p1:
                    continue
                p1.append(n)
            
        x=int(a[0])
        y=int(a[2])
    
        if p =="V" or p=='v' :
            if y<1 or x<1 or y>5:
                print ("Input invalid for wrong input you lose 1 ship")
            for i2 in range(4):
                n=[x,y]
                y+=1
                if n in p1:
                    continue
                p1.append(n)
            
        if p not in 'HhVv':
            print("Input for H or V was invalid please try again")

    '''this will make the p1 have the coordinates in bunches of 2'''

    print(P2,"please input the location of your ships")
    for abcdefg in range(3):
    
        a=(input("enter coordinates WHOLE NO. (between 1-10) for the ship it is a 10*10 grid ,FOR VERTICAL 1-9,1-6 ,FOR HORIZONTAL 1-6,1-9\n"))
        p=input("H-Horizontal or V-vertical")

        x=int(a[0])
        y=int(a[2])

        if p =="H" or p=='h' :
            if x<1 or y<1 or x>6:
                print ("Input invalid for wrong input you lose 1 ship")
            for i in range(4):
                n=[x,y]
                x+=1
                if n in p2:
                    continue
                p2.append(n)
            
        x=int(a[0])
        y=int(a[2])
    
        if p =="V" or p=='v' :
            if y<1 or x<1 or y>6:
                print ("Input invalid for wrong input you lose 1 ship")
            for i2 in range(4):
                n=[x,y]
                y+=1
                if n in p2:
                    continue
                p2.append(n)
            
        if p not in 'HhVv':
            print("Input for H or V was invalid please try again")

    '''This concludes the pregame desicion'''

    '''The gameplay'''

    '''l is a list of all locations already hit'''

    l1=[]
    l2=[]
    P2ua=p2
    P1ua=p1
    while True:

        print(P1,"it's your chance")

        print("Locations already tried:")
        for i in range(len(l1)):
                print (l1[i])
    
        n=input("location coordinates to blow it UP")

        x=int(n[0])
        y=int(n[2])
        
        n=[x,y]
        
        if n in l1:
            print("Sorry you already tried this location,you lose a chance")

        else:
            l1.append(n)
            
            if n in p2:
                print("that's a HIT")
                p2.remove(n)
                board1[y][x-1]=' X '
                
                if len(p2)==0:
                    print(P1,"WINS")
                    break
                
            elif n=='69,420':
                p1=[]
                print("Cheats have been activated")
                if len(p1)==0:
                    print(P1," WINS")
                    break
            else:
                print ("No ship was present there")
                print ("No. of locations where enemy ships are still present:",len(p2))
                board1[y][x-1]=' * '
            print ("No. of locations where enemy ships are still present:",len(p2))
        bdprint(board1)            
            
        print(P2,"it's your chance")

        print("Locations already tried:")
        for i in range(len(l2)):
                print (l2[i])

        m=input("location coordinates(LIST) to blow it UP")
        x=int(m[0])
        y=int(m[2])
        m=[x,y]

        if m in l2:
            print("Sorry you already tried this location,you lose a chance")
            pass
        
        else:
            l2.append(m)
            
        if m in p1:
                print("that's a HIT")
                p1.remove(m)
                board2[y][x-1]=' X '
                
                if len(p1)==0:
                    print(P2," WINS")
                    break

        elif m==[69,420]:
                p1=[]
                print("Cheats have been activated")
                
                if len(p1)==0:
                    print(P2," WINS")
                    break
            
        else:
            print ("No ship was present there")
            board2[y][x-1]=' * '
            
        print ("No. of locations where enemy ships are still present:",len(p1))    
        bdprint(board2)
