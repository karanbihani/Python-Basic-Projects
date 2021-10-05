import pickle as p
import os

def new():
    f = open('transaction_history_log.dat','ab')
    n = input('Name:\n')
    b = int(input('Balance:\n'))
    l = [n.lower(),b]
    p.dump(l,f)
    print('Account Added')

def tran():
    f = open('transaction_history_log.dat','rb')
    f1 = open('temp.dat','wb')
    f.seek(0,0)
    a = input('Name:\n').lower()
    t = input ('Transaction is Addition or Subtraction ?A\S\n')
    amt = int(input('Amount:\n'))
    l =[]
    while 1:
        try:
            d = p.load(f)
            if a == d[0]:
                if t.lower()=='a':
                    d[1]+=amt
                    p.dump(d,f1)
                    print('Transaction Succesful')
                else:
                    if d[1]-amt>-1:
                        d[1]-=amt
                        p.dump(d,f1)
                        print(f'Transaction Succesful\nBalance:{d[1]}')
                    else:
                        print(f'Insufficient Funds\nBalance:{d[1]}')
                        p.dump(d,f1)
                
            else:
                p.dump(d,f1)
            
        except EOFError:
            break

    f.close()
    f1.close()

    os.remove('transaction_history_log.dat')
    os.rename('temp.dat','transaction_history_log.dat')
    
def display():
    f = open('transaction_history_log.dat','rb')
    a = input('Name:\n').lower()
    while 1:
        try:
            d = p.load(f)
            if a == d[0]:
                print(d[1])
        except EOFError:
           break
    
def display_all():
    f = open('transaction_history_log.dat','rb')
    while 1:
        try:
            d = p.load(f)
            print(d[0],':',d[1])
            
        except EOFError:
            break
    
while True:
    c = int(input('1.New account\n2.Add or Subtract amount in account\n3.Display Balance\n4.Display All\n5.Exit\n'))
    if c == 1:
        new()
    elif c == 2:
        tran()
    elif c ==3:
        display()
    elif c == 4:
        display_all()
    else:
        break
                
