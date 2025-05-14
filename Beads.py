from random import randint
#red = 0 black = 1 yellow = 2
redwin = 0
blackwin = 0
yellowwin = 0

 
rep = 1000000
y = 0
while y < rep:
    array = []
    redc = 0
    blackc = 0
    yellowc = 0
     
    while redc < 30:
        array.append(0)
        redc += 1
     
    blackgen = randint(0,60)
    while blackc < blackgen:
        array.append(1)
        blackc += 1
     
    while yellowc < (60-blackgen):
        array.append(2)
        yellowc += 1
        
    x = 0
    x = randint(0,89)
    if array[x] == 0:
        redwin += 1
    if array[x] == 1:
        blackwin += 1
    if array[x] == 2:
        yellowwin += 1
    
    y += 1

print (redwin)
print (blackwin)
print (yellowwin)
    
print ((redwin/rep)*100)
print ((blackwin/rep)*100)
print ((yellowwin/rep)*100)