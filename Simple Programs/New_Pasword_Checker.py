#If password not combo of alphabet,numbers,1 special charecter

pwd = input('Enter Password:\n')
a = 0
n = 0
s = 0
sp = 0
for x in pwd:
    if x.isalpha():
        a = True
    elif x.isdigit():
        n = True
    elif x.isspace():
        sp = True
    else:
        s = True
        

def pwdc():
    assert a==True ,'Oops you did not include Alphabet'
    assert n==True ,'Oops you did not include Number'
    assert s==True ,'Oops you did not include Special Charecter'
    assert sp==False,'Oops you included space'
pwdc()
