#%%
   # Import packages
import random


#%%
def set_board(): #initialise a 8x8 board
    global com_sur_board  # visual elements for user and computer board are kept in a list variable
    global com_und_board
    global user_sur_board
    global user_und_board
    com_sur_board = []   # visual elements for user and computer board are kept in a list variable
    com_und_board = []
    user_sur_board =[]
    user_und_board =[]

    for i in range(1,9):
        com_und_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |"])
        com_sur_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |"])
        user_sur_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |"])
        user_und_board.append([str(i)," ","   |","   |","   |","   |","   |","   |","   |","   |"])    
    
def computer_board(): #Print our the board using list variables defined.
    print('The computer\'s board looks like this')
    print('   1   2   3   4   5   6   7   8 ')
    print('Surface')        
    for row in com_sur_board:
        print("".join(row))
        print("   -------------------------------")
    print('Underwater')
    for row in com_und_board:
        print("".join(row))
        print("   -------------------------------")
    print('   1   2   3   4   5   6   7   8 ')
def user_board():
    print('The user\'s board looks like this')
    print('   1   2   3   4   5   6   7   8 ')
    print('Surface')
    for row in user_sur_board:
        print("".join(row))
        print("   -------------------------------")    
    print('Underwater')
    for row in user_und_board:
        print("".join(row))
        print("   -------------------------------")   
    print('   1   2   3   4   5   6   7   8 ')
#%%
def invalid_ship(x): #error message for ships that is placed out of the board/overlaps
    print('Cannot place a '+ x +' there. \nPlease take a look at the board and try again')
    user_board
    input('Press Enter to continue')
   
#%%
def place_sub(): #user places a submarine
    global sur_sub_coor
    global und_sub_coor
    sur_sub_coor = []
    und_sub_coor = []
    while True:
        print('Welcome to Battleship+')
        print('Please Place your SUBMARINE')
        print('Please enter coordinates following this format (row,col,depth). E.g. 3,4,1 (row = 3, col = 4, and depth =1).')
        print('Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.')
        while True:
            try:
                srow, scol, sdepth = [int(x) for x in input("Enter coordinates for your submarine: ").split(",")]
                if not ((0<srow <9) and (0<scol <9)) :
                    print('Cannot place your submarine there. \nPlease take a look at the board and try again.')
                    user_board()
                    continue
                if not (0<= sdepth <2):
                    print('Please enter a valid value: 0 for subsea layer, 1 for surface level.')
                    continue
            except ValueError:
                print("Sorry, I didn't understand your coordinate input.")
                continue
            else:
                break
        while True:
            orientation = input('vertical or horizontal (v,h)? ')
            if orientation in ['v','h']:
                break
            else:
                print('I didn\'t understand your orientation input.')
                continue
        print()

        if orientation =='h':
            if scol<7:
                if sdepth ==1:
                    for x in range(srow,srow+1):
                        for y in range(scol,(scol+3)):
                            user_sur_board[x-1][y+1] = ' S |'
                            sur_sub_coor.append([x,y])
                if sdepth ==0:
                    for x in range(srow,srow+1):
                        for y in range(scol,(scol+3)):
                            user_und_board[x-1][y+1] = ' S |'
                            und_sub_coor.append([x,y])
                break
            else: 
                invalid_ship('submarine')
                continue

        else:
            if srow<7:
                if sdepth == 1:
                    for x in range(srow,srow+3):
                        for y in range(scol,scol+1):
                            user_sur_board[x-1][y+1] = ' S |'
                            sur_sub_coor.append([x,y])
                if sdepth == 0:
                    for x in range(srow,srow+3):
                        for y in range(scol,scol+1):
                            user_und_board[x-1][y+1] = ' S |'
                            und_sub_coor.append([x,y])
                break
            else:  
                invalid_ship('submarine')
                continue
            
# In[7]:
def place_des():    
    global des_coor 
    des_coor = []
    while True:
        print('Now it\'s time to place your Destroyer')
        print('Please enter coordinates following this format (row,col,depth). E.g. 3,4,1 (row = 3, col = 4, and depth =1). Destroyer can only be placed at surface level')
        print('Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.')
        while True:
            try:
                drow, dcol, ddepth = [int(x) for x in input("Enter coordinates for your destroyer: ").split(",")]
                if not ((0<drow <9) and (0<dcol <9)) :
                    print('Cannot place your destroyer there. \nPlease take a look at the board and try again.')
                    user_board()
                    continue
                if ddepth != 1:
                    print('Depth must be 1 for destroyer')
                    continue
            except ValueError:
                print("Sorry, I didn't understand your coordinate input.")
                continue
            else:
                break
        
        while True:
            orientation = input('vertical or horizontal (v,h)? ')
            if orientation in ['v','h']:
                break
            else:
                print('I didn\'t understand your orientation input.')
                continue                                   
            
        # following code deals with the validity of destroyer's coordinate and place the destroyer accordingky on the bvoard.
        if drow>6: 
            if orientation == 'h': #only if ship lies horizontally, are the coordinates accepted
                des_coor = [[x,y] for x in range(drow,drow+1) for y in range(dcol,dcol+3)]    
            else: 
                invalid_ship('destroyer')
                continue
        elif dcol>6:
            if orientation == 'v':
                des_coor = [[x,y] for x in range(drow,drow+3) for y in range(dcol,dcol+1)]
            else: 
                invalid_ship('destroyer')
                continue
        else: #ships that does not have their ends at the edge of the board
            if orientation == 'h': 
                des_coor = [[x,y] for x in range(drow,drow+1) for y in range(dcol,dcol+3)]  
            else:
                des_coor = [[x,y] for x in range(drow,drow+3) for y in range(dcol,dcol+1)]
                
        if any(x in des_coor for x in sur_sub_coor) == True:
            invalid_ship('destroyer')
            continue
        else:
            break
    #after checking that the coordinates are valid we print the destroyers on the board
    if orientation == 'h':
        for x in range(drow,drow+1):
            for y in range(dcol,dcol+3):    
                user_sur_board[x-1][y+1] = ' D |'
    else:
        for x in range(drow,drow+3):
            for y in range(dcol,dcol+1):    
                user_sur_board[x-1][y+1] = ' D |'
# In[11]:  
def com_place_sub(): #computer places a submarine   
    global com_sur_sub_coor
    global com_und_sub_coor
    com_sur_sub_coor = [] #computer surface submarine coordinates
    com_und_sub_coor = [] #computer underwater submarine coordinates
    
    print('Computer is placing a submarine.')      
    orientation = random.choice(['v','h'])    
    
    if orientation == 'h':
        cs_row, cs_col, cs_depth =random.randint(1,8), random.randint(1,6), random.randint(0,1)
        if cs_depth == 1:
            com_sur_sub_coor = [[x,y] for x in range(cs_row,cs_row+1) for y in range(cs_col,cs_col+3)]   
        elif cs_depth == 0:
            com_und_sub_coor = [[x,y] for x in range(cs_row,cs_row+1) for y in range(cs_col, cs_col+3)]                
    elif orientation == 'v':
        cs_row, cs_col, cs_depth =random.randint(1,6), random.randint(1,8), random.randint(0,1)
        if cs_depth == 1:
            com_sur_sub_coor = [[x,y] for x in range(cs_row,cs_row+3) for y in range(cs_col, cs_col+1)]
        elif cs_depth == 0:
            com_und_sub_coor = [[x,y] for x in range(cs_row,cs_row+3) for y in range(cs_col, cs_col+1)]

# In[12]:

def com_place_des(): #place the destroyer for computer
    print('Computer is placing a destroyer.')     
    while True:               
        global com_des_coor
        com_des_coor = []
        orientation2 = random.choice(['v','h'])
        if orientation2 == 'h':
            cd_row, cd_col = random.randint(1,8), random.randint(1,6) #can only place destroyer on the surface
            com_des_coor = [[x,y] for x in range(cd_row,cd_row+1) for y in range(cd_col,cd_col+3)]
        else:
            cd_row, cd_col = random.randint(1,6), random.randint(1,8) #can only place destroyer on the surface
            com_des_coor = [[x,y] for x in range(cd_row,cd_row+3) for y in range(cd_col,cd_col+1)]               
        
        if any(x in com_des_coor for x in com_sur_sub_coor):
            continue
        else: 
            break
    #%%
def hit_message(x): #so that the ship sunk message doesn't show every time a ship is hit
        global printed
        if printed == True:
            pass
        else:
            print('The '+ x +'\'s ship was hit at location','(',hrow, hcol, hdepth,')')
            printed = True
            #%%
def hit():
    global sur_hit_coor 
    global und_hit_coor
    global com_des_coor
    global com_und_sub_coor
    global com_sur_sub_coor
    global hrow #these 4 are for the hit_message()
    global hcol
    global hdepth
    global printed
    sur_hit_coor =[]
    und_hit_coor =[]
    print('It\'s USER\'s turn to hit computer\'s ships.')
    computer_board()           
    print('Please enter hit coordinates following this format (row,col,depth). E.g. 3,4,1 (row = 3, col = 4, and depth =1).')
    print('Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.')
    while True: #this block is to deal with error input
        try:
            hrow, hcol, hdepth = [int(x) for x in input("Enter your hit coordinates: ").split(",")]
            if not ((0<hrow <9) and (0<hcol <9)):
                 print('Input row and column must be an integer from 1 to 8.') 
                 continue
            else:
                if (hdepth in (0,1) == 'False'):
                    print('Depth must be 0 or 1.')  
                    continue
                else:
                    pass
        except ValueError:
            print('Invalid input. \nInput row and column must be an integer from 1 to 8.\
                  Depth must be 0 or 1')
        else:
            break
    printed = False
    #hitting strategy
    #we go through a 3x3 area around the hit area, if either row/column coordinate is smaller/larger than 0/9, we pass
    #if it is within 1 to 8, we print a * |
    #if the area of the hit coordinate is the same as ship's coordinate, we print a $

    for x in range(hrow-2,hrow+1):                                         
        for y in range(hcol,hcol+3):
            if not (x in range(0,8) and y in range(2,10)):
                pass
            else:
                if hdepth ==1:
                    sur_hit_coor.append([x+1,y-1])
                    if any(x in com_sur_sub_coor for x in sur_hit_coor):
                        com_sur_board[x][y] = ' $ |'
                        com_sur_sub_coor.remove([x+1,y-1])
                        hit_message('Computer')
                    elif any(x in sur_hit_coor for x in com_des_coor):
                        com_sur_board[x][y] = ' $ |'
                        com_des_coor.remove([x+1,y-1])
                        hit_message('Computer')
                    else:
                        if com_sur_board[x][y] == ' $ |':
                            pass
                        elif com_sur_board[x][y] != ' $ |':
                            com_sur_board[x][y]= ' * |'
                elif hdepth ==0:
                    und_hit_coor.append([x+1,y-1])
                    if any(x in und_hit_coor for x in com_und_sub_coor):
                        com_und_board[x][y] = ' $ |'
                        com_und_sub_coor.remove([x+1,y-1])
                        hit_message('Computer')
                            
                    else:
                        if com_und_board[x][y] == ' $ |':
                            pass
                        elif com_und_board[x][y] != ' $ |':
                            com_und_board[x][y]= ' * |'
    if printed == False:
        print("The hit at location",'(',hrow, hcol, hdepth,') was a total miss lol')
    computer_board()


#%%
def com_hit():
    print('Now it\'s computer\'s turn to hit user\'s ships.') 
    hrow, hcol, hdepth = random.randint(1,8),random.randint(1,8),random.randint(0,1) 
    global com_sur_hit_coor
    global com_und_hit_coor
    com_sur_hit_coor = []
    com_und_hit_coor = []
    global printed
    printed = 0
    
    for x in range(hrow-2,hrow+1): 
        for y in range(hcol,hcol+3):
            if not (x in range(0,8) and y in range(2,10)):
                pass
            else:
                if hdepth ==1:
                    com_sur_hit_coor.append([x+1,y-1])
                    if any (x in com_sur_hit_coor for x in sur_sub_coor):
                        hit_message('User')
                        user_sur_board[x][y] = ' $ |'
                        sur_sub_coor.remove([x+1,y-1])
                    elif any (x in com_sur_hit_coor for x in des_coor) :
                        user_sur_board[x][y] = ' $ |'
                        hit_message('User')
                        des_coor.remove([x+1,y-1])
                    else:
                        if user_sur_board[x][y] == ' $ |': #this is so it doesn't change the $ sign of the sunk ship
                            pass                           
                        elif user_sur_board[x][y] != ' $ |':
                            user_sur_board[x][y]= ' * |'
                elif hdepth ==0:
                    com_und_hit_coor.append([x+1,y-1])
                    if any (x in com_und_hit_coor for x in und_sub_coor):
                        user_und_board[x][y] = ' $ |'
                        hit_message('User')
                        und_sub_coor.remove([x+1,y-1])
                    else:
                        if user_und_board[x][y] == ' $ |':
                            pass 
                        elif user_und_board[x][y] != ' $ |':
                            user_und_board[x][y]= ' * |'
                        
    if printed == False:
        print("The hit at location",'(',hrow, hcol, hdepth,') was a total miss lol')
    user_board()                                

#%%    
# Run the whole program
while True:
    set_board()
    place_sub()          
    place_des()
    user_board()
    input('Your ships are palced on the board shown above. Press Enter for Computer to place ships.')
    print()
    com_place_sub()
    com_place_des()
    print('Computer placed ships shown below.')
    computer_board()
    input('Press Enter to start the game.')
    print('GAME START!! \n\n')
    
    user_sub_sunk = 0 #these 4 are for preventing repetition of the printing of ships sunk
    user_des_sunk = 0
    com_sub_sunk = 0
    com_des_sunk =0
    
    while True:
        hit()# User attack
        print('Look at your attack on the board')
        # Calculate result for computer
        if (com_sur_sub_coor == []) and (com_und_sub_coor ==[]):
            print('Computer\'s submarine sunk.')
            com_sub_sunk = 1
        if (com_des_coor == [] and com_des_sunk == 0):
            print('Computer\'s destroyer sunk.')
            com_des_sunk = 1
        if (com_sub_sunk == 1 and com_des_sunk == 1):
            print('User won! :)')
            break
        else:
            pass
        input('Press Enter to end your turn.')
        print()
        
        com_hit() # Computer attack
        input('Press Enter to end computer\'s turn.')
        print()
        # Calculate result for user
        if (sur_sub_coor == []) and (und_sub_coor ==[]):
            print('User\'s submarine sunk.')
            user_sub_sunk = 1
        if des_coor == [] and user_des_sunk == 0:
            print('User\'s destroyer sunk.')
            user_des_sunk = 1
        if user_sub_sunk == 1 and user_des_sunk == 1:
            print('Computer won! :)')
            break
        else: 
            continue
    
    while True: #asking user's choice to continue playing or not
        game = input('Do you want to play again? Enter Y for yes or N for no: ')
        if game in ('Y','N'):
            break
        else: 
            print('Sorry, I don\'t understand your instructions.\n')
            continue 
    if game == 'Y':
        continue
    else:
        print('Goodbye!')
        break
