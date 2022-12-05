
#When checking for a win, my checks for horizontal and vertical work very differently to my checks for / and \ 
#This is because i came up with a more effecient method but was too lazy to change it for horizontal and vertical checks






import numpy as np     #Useful for arrays
import time            #So i can choose how long to wait before executing the next line
from random import randint #for generating a pseudorandom number
import sys #so i can call sys.exit() which ends the program
from matplotlib import pyplot as plt


def main():
    print ('How many rows and columns would you like the gameboard to have? (Must be greater or equal to 4 for both') 
    c = True
    while c == True:
        n = int(input('Rows: ')) #stores the number of rows
        m = int(input('Columns: ')) #stores the number of columns
        if n >= 4 and m >= 4:
            c = False
        else:
            print("Rows and Columns must be 4 or greater")
    windetected = 0
    board = np.zeros((n,m)) #creates the board to the dimensions selected by the user
    print (board)
    print ('''      ^  This is the starting board
      ¦  ''')
    print ("Your pieces will be denoted by 1's throughout the game and O on the final plot, the computer will be 2's and X")
    a = True
    while a == True:   
        movefirst = input('Do you want to make the starting move? Y/N ')
        if movefirst == 'Y' or movefirst == 'y':
            time.sleep(1)
            move(board)
            print (board)
            while windetected == 0:
                time.sleep(1)
                print ("It's now the computers turn")
                time.sleep(1)
                compmove(board)
                print (board)
                checkwin(board,2)
                time.sleep(1)
                print ("It's now your turn")
                time.sleep(1)
                move(board)
                print (board)
                checkwin(board,1)
        elif movefirst == 'N' or movefirst == 'n':
            time.sleep(1)
            compmove(board)
            print (board)
            while windetected == 0:
                time.sleep(1)
                print ("It's now your turn")
                time.sleep(1)
                move(board)
                print (board)
                checkwin(board,1)
                time.sleep(1)
                print ("It's now the computers turn")
                time.sleep(1)
                compmove(board)
                print (board)
                checkwin(board,2)         
        else:
            print ("Please enter a valid input, which is either Y or N")
    

def move(b):
    a = True
    while a == True: #if the users inputs are invalid this makes sure to run through the function again
        col = int(input('Which column do you want place your counter: '))
        l = len(b[0]) #finds the length of the columns
        r = len(b) #finds the length of the rows
        count = 1 #will be used later to count how many rows we've checked, when count = r we know that the column is empty and so a counter is placed at the bottom of the column
        p = 0 #keeps count of the index of the row we're on so that i can place a counter in the correct row
        if col <= l and col >= 1: #checking whether the user has entered a suitable input
            for i in b: #iterates through all rows
                if (i[col-1] == 1 and count != 1) or (i[col-1] == 2 and count != 1): #if there is a counter here, it will add a counter above it and end the loop
                    b[p-1, col-1] = 1
                    a = False
                    break
                if count == r and i[col-1] == 0: #if you reach the bottom and encounter no counters a counter will be placed at the bottom and the loop will end
                    b[r-1, col-1] = 1
                    a = False
                    break
                if count == 1 and i[col-1] != 0: #if the top row has a counter, the user will be asked to choose a different row
                    print ('That column is full! please choose another... ')
                    break
                p += 1
                count += 1
        else:
            print ("that isn't a column on the gameboard, please choose another")
    return (b)


def compmove(b): #pretty much just does what the function move() does but a move is randomly generated
    a = True
    while a == True: 
        l = len(b[0])
        r = len(b)
        c = randint(0,l-1)
        count = 1
        p = 0
        for i in b:
            if (i[c] == 1 or i[c] == 2) and count != 1: #if there is a counter here, it will add a counter above it and end the loop
                b[p-1, c] = 2
                a = False
                break
            if count == r and i[c] == 0: #if you reach the bottom and encounter no counters a counter will be placed at the bottom and the loop will end
                b[r-1, c] = 2
                a = False
                break
            if count == 1 and i[c] != 0: #if the top row has a counter, the computer will be asked to choose a different row
                break
            p += 1
            count += 1
    return (b)


def checkwin(b,player):
    l = len(b[0])
    r = len(b)
    
     #We are going to search for a 4 in a row in all rows first 
     
    for i in b:
        count = 0
        d = 0 #To keep track of the index of the column
        while count < 4 and d != l:
            d += 1
            for x in i:
                if x == player:
                    count += 1
                    if count == 4:
                        print ("Player",player,"Won!")
                        plotboard(b)
                        time.sleep(3)
                        sys.exit()
                else:
                    count = 0
        
    #Checking for vertical 4 in a rows
    
    counter = 0 #tells us what column we're on
    while counter < l:
        count = 0
        p = 0 #To keep track of what row we're on
        while count < 4 and p != r:
             p += 1
             for i in b:
                 if i[counter] == player:
                     count += 1
                     if count == 4:
                         print ("Player",player,"Won!")
                         plotboard(b)
                         time.sleep(3)
                         sys.exit()
                 else:
                     count = 0
        counter += 1

    #Checking for \ diagonal wins
    
    for y in range(r-3):
        for x in range(l-3):
            if b[y][x] == player and b[y+1][x+1] == player and b[y+2][x+2] == player and b[y+3][x+3] == player:
                print ("Player",player,"Won!")
                plotboard(b)
                time.sleep(3)
                sys.exit()
    
    #checking for / diagonal wins
    
    for y in range(3, r):
        for x in range(l-3):
            if b[y][x] == player and b[y-1][x+1] == player and b[y-2][x+2] == player and b[y-3][x+3] == player:
                print ("Player",player,"Won!")
                plotboard(b)
                time.sleep(3)
                sys.exit()
            
    #checking if board is full (Draw)
    
    totb = 0
    for y in b:
        for x in y:
            if x != 0:
                totb += 1
    totp = l*r
    if totb == totp:
        print ("It's a Draw")
        plotboard(b)
        time.sleep(3)
        sys.exit()


def plotboard(b):
    
    #This adds the respective x and y components of player 1 and player 2's to lists
    
    list1x = []
    list1y = []
    list2x = []
    list2y = []
    y = len(b)
    for i in b:
        x = 1
        for j in i:
            if j == 1:
                list1x.append(x)
                list1y.append(y)
            if j == 2:
                list2x.append(x)
                list2y.append(y)
            x += 1
        y -= 1
    
    plt.plot(list1x, list1y, color = "red", marker = "o", markersize = 15, linestyle = "")
    plt.plot(list2x, list2y, color = "blue", marker = "x", markersize = 15, linestyle = "")
    plt.show()

main()









