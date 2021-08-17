# The program will run a memorizatio game that shows a 3 x 3 tiles interface. 
# Then the program will randomly choose a tile, in which the user has to choose it. 

import random
import time

# Asks user for their name 
def name():
    print('What is your name?')
    username = input()

    return username 

# Introduces the user to the game by making a story, then asking for them to play the game 
def intro(username):
    print('Welcome ' + username + ' to Tile Madness!')
    print('This game will test your memorization skills!')
    print('Do you have what it takes to beat me?')
    print('Are you smarter than a chimp?')
    print('Yes or No')
    start = input()
    while True:
        if start[0].lower() == 'y':
            print('We will see about that!')
            break
        elif start[0].lower() == 'n':
            print('Where\'s yo confidence!')
            print('Are you smarter than a chimp?')
            print('Yes or No')
            start = input()
        else:
            print('Wrong input, answer as yes or no!')
            start= input()

username = name()
intro(username)

    
# Set tiles to zero

tile1 = 0
tile2 = 0
tile3 = 0
tile4 = 0
tile5 = 0
tile6 = 0
tile7 = 0
tile8 = 0
tile9 = 0

tilelist = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9]


# Tile Format 

def tileformatexample(tile):
    # This function prints out the tile. The "tiles" are strings that the program chooses.
    
    tile1 = tile[0]
    tile2 = tile[1]
    tile3 = tile[2]
    tile4 = tile[3]
    tile5 = tile[4]
    tile6 = tile[5]
    tile7 = tile[6]
    tile8 = tile[7]
    tile9 = tile[8]
    

    # Shows example of what the tiles look like 
    print('This is the foramt!')
    print('   |   |')
    print(' ' + str(tile1) + ' | ' + str(tile2) + ' | ' + str(tile3))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(tile4) + ' | ' + str(tile5) + ' | ' + str(tile6))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(tile7) + ' | ' + str(tile8) + ' | ' + str(tile9))
    print('   |   |') 

# Starting the game ( ~ Beggining ~ )

# Time functions add after the example format

def gamestart(tile):
    
    print("The game will start now!")
    print("The game will revolve around this 3 by 3 tile")
 
    # Program chooses the one of the tiles
    
    choosenTile = random.choice(tilelist)
    choosenTile += 1
    
    print('   |   |')
    print(' ' + str(tile1) + ' | ' + str(tile2) + ' | ' + str(tile3))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(tile4) + ' | ' + str(tile5) + ' | ' + str(tile6))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + str(tile7) + ' | ' + str(tile8) + ' | ' + str(tile9))
    print('   |   |')    
     
    

tileformatexample(tilelist)
gamestart(tilelist)