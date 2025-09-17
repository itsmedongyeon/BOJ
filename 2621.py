def function1(deck):
    deck=sorted(deck,key=lambda x: x[1])
    for i in range(4):
        if deck[i][0]==deck[i+1][0] and deck[i][1]+1==deck[i+1][1]: 
            #check whether color is same and number is continuous
            continue
        else:
            return 0
    return 900+deck[4][1]
    
def function2(deck):
    deck=sorted(deck,key=lambda x: x[1])
  
    if deck[0][1]!=deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]==deck[4][1]:
        return 800+deck[1][1]
    if deck[0][1]==deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]!=deck[4][1]:
        return 800+deck[1][1]
    else:
        return 0

def function3(deck):
    deck=sorted(deck,key=lambda x: x[1])
    if deck[0][1]==deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]==deck[4][1]:
        return 10*deck[0][1]+deck[4][1]+700
    if deck[0][1]==deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]==deck[4][1]:
        return deck[0][1]+10*deck[4][1]+700
    return 0    
def function4(deck):
    deck=sorted(deck,key=lambda x: x[1])
    for i in range(4):
        if deck[i][0]==deck[i+1][0]: #check whether color is same
            continue
        else:
            return 0
    return 600+deck[4][1]

def function5(deck):
    deck=sorted(deck,key=lambda x: x[1])
    for i in range(4):
        if deck[i][1]+1==deck[i+1][1]: #check whether number is continuous
            continue
        else:
            return 0
    return 500+deck[4][1]

def function6(deck):
    deck=sorted(deck,key=lambda x: x[1])
    if deck[0][1]==deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]!=deck[4][1]:
            return 400+deck[0][1]
    if deck[0][1]!=deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]!=deck[4][1]:
            return 400+deck[1][1]
    if deck[0][1]!=deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]==deck[4][1]:
            return 400+deck[4][1]
    return 0

def function7(deck):
    deck=sorted(deck,key=lambda x: x[1])
    if deck[0][1]==deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]!=deck[4][1]:
            return 300+10*deck[2][1]+deck[0][1]
    if deck[0][1]!=deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]==deck[4][1]:
            return 300+10*deck[3][1]+deck[1][1]
    if deck[0][1]==deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]==deck[4][1]:
            return 300+10*deck[4][1]+deck[0][1]
    return 0

def function8(deck):
    deck=sorted(deck,key=lambda x: x[1])
    if deck[0][1]==deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]!=deck[4][1]:
            return 200+deck[0][1]
    if deck[0][1]!=deck[1][1] and deck[1][1]==deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]!=deck[4][1]:
            return 200+deck[1][1]
    if deck[0][1]!=deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]==deck[3][1] and deck[3][1]!=deck[4][1]:
            return 200+deck[2][1]
    if deck[0][1]!=deck[1][1] and deck[1][1]!=deck[2][1] and deck[2][1]!=deck[3][1] and deck[3][1]==deck[4][1]:
            return 200+deck[3][1]
    return 0
def function9(deck):
    deck=sorted(deck,key=lambda x: x[1])
    return 100+deck[4][1]


        
deck=list()
for i in range(5):
    card=input()
    temp=card.split()
    temp[1]=int(temp[1])
    deck.append(temp)
answer=0
if answer==0:
    answer=function1(deck)

if answer==0:
    answer=function2(deck)
    
if answer==0:
    answer=function3(deck)
    
if answer==0:
    answer=function4(deck)
    
if answer==0:
    answer=function5(deck)

if answer==0:
    answer=function6(deck)

if answer==0:
    answer=function7(deck)

if answer==0:
    answer=function8(deck)

if answer==0:
    answer=function9(deck)

print(answer)
    