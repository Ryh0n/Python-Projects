
alicewins = 0
bobwins = 0

test = 0
while test < 100000:
    
    from random import randint
    list = []
    x = 0
    while x < 100:
        list.append(randint(0,1))
        x += 1
        
    count1 = 0
    a = 0
    while a < 100:
        if list[a] == 0:
            count1 = 0
            a += 1
        if list[a] == 1:
            count1 += 1
            a += 1
            if count1 == 2:
                #print ("Alice found 2 heads after: ", a)
                acount = a
                a = 100
    
    count2 = 0
    b = 0
    while b < 50:
        if list[b] == 0:
            count2 = 0
            b += 2
        if list[b] == 1:
            count2 += 1
            b += 2
            if count2 == 2:
                #print ("Bob found 2 heads after: ", int(b/2))
                bcount = b/2
                b = 50
       
    if acount < bcount:
        alicewins += 1
    if bcount < acount:
        bobwins += 1
    test += 1
    
print (alicewins)
print (bobwins)
percent = (((bobwins-alicewins)/alicewins)*100)
print (percent)
