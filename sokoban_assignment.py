import copy

###GEAROID CONWAY 16306906###
###SOKOBAN PROJECT###


levels= [
            {
                'board': [["#","#","#","#","#","#","#","#"], #0     #level 1

                        ["#"," "," "," ","#"," "," ","#"], #1

                        ["#"," ","#"," ","#"," "," ","#"], #2

                        ["#"," "," "," "," "," "," ","#"], #3

                        ["#"," ","#"," ","#"," "," ","#"], #4

                        ["#"," "," "," ","#"," "," ","#"], #5

                        ["#","#","#","#","#"," "," ","#"], #6

                        [" "," "," "," ","#","#","#","#"] ], #7,

                'state':#objects on the board
                    {
                        'player':[6,5],
                        'goals': [[2,6],[3,6],[4,6]],
                        'boxes': [[2,5],[3,5],[4,5]]
                    }
            },

            {
                'board': [[" "," "," "," "," "," ","#","#","#","#","#"], #0         #level 2

                        [" "," "," "," "," "," ","#"," "," "," ","#"], #1

                        [" "," "," "," "," "," ","#"," ","#"," ","#"], #2

                        ["#","#","#","#","#","#","#"," ","#"," ","#"], #3

                        ["#"," "," "," "," "," "," "," "," "," ","#"], #4

                        ["#"," ","#"," ","#"," ","#"," ","#","#","#"], #5

                        ["#"," "," "," "," "," "," "," ","#"," "," "], #6

                        ["#","#","#","#","#","#","#","#","#"," "," "] ], #7

                'state':
                    {
                        'player':[4,2],
                        'goals': [[1,7],[2,7],[3,7]],
                        'boxes':[[4,4],[4,6],[4,8]]
                    }
            }


        ]

direction = "" #assigned in the move function and used in the moveCheck as a reference to undo valid moves
currentGo = 0 #used to increment levels list item to change level

level = levels[currentGo]['board']              #assign key placeholder values to reduce complexting of move and check functions
positions = levels[currentGo]['state']
player = levels[currentGo]['state']['player']
boxPos = levels[currentGo]['state']['boxes']
goalPos = levels[currentGo]['state']['goals']


def printBoard():      #prints the board to the screen


    tempBoard = copy.deepcopy(level)#creates a tempboard


    tempBoard[player[0]][player[1]] = "@" #places player on the board



    for i in range(len(goalPos)):
        tempBoard[goalPos[i][0]][goalPos[i][1]] = "."  # iterate through the board placing goals

    for i in range(len(boxPos)):
        tempBoard[boxPos[i][0]][boxPos[i][1]] = "$" #iterate through the board placing boxes

    matchList = [x for x in boxPos if x in goalPos] #creates a list of coordinates for boxes on goals

    for i in range(len(matchList)):
        tempBoard[matchList[i][0]][matchList[i][1]] = "*"  #uses these values to turn the symbol to the star on the board


    if tempBoard[player[0]][player[1]] == ".": #checks if player is on a goal square and chnages it to +
        tempBoard[player[0]][player[1]] = "+"

    x = 0
    for i in tempBoard:
        print(" ".join(tempBoard[x]))  #formats and prints the board
        x += 1

##########################################################################################



def moveMaker():


    global direction
    direction = (input("Please make a move using (a,s,w,d): "))  # user input

    if direction=="a":

        levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1]-1 #move up

    if direction=="w":

        levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0]-1    #move left

    if direction=="d":

        levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] + 1 #move right

    if direction=="s":

        levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] + 1 #move down


##############################################################################################################################


def moveCheck(): #checks if move was valid

    if direction == "a":
        potentialMove = [player[0], player[1] - 1] #one step ahead placeholder

        if levels[currentGo]['board'][player[0]][player[1]]=="#":
            levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] + 1 #INVALID wall.

        elif levels[currentGo]['board'][player[0]][player[1]-1] == "#":  #INVALID box to wall
            if player in boxPos:
                levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] + 1

        elif player in boxPos and potentialMove in boxPos:# INVALID box to Box
            levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] + 1#undo

        elif player in boxPos:#box to space
            x = boxPos.index(player)
            boxPos[x][1] = boxPos[x][1]-1


    if direction == "d":
        potentialMove = [player[0], player[1]+1] #one step ahead placeholder


        if levels[currentGo]['board'][player[0]][player[1]]=="#":
            levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] - 1 #INVALID wall.

        elif levels[currentGo]['board'][player[0]][player[1]+1] == "#":  #INVALID box to wall
            if player in boxPos:
                levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] - 1

        elif player in boxPos and potentialMove in boxPos:# INVALID box to Box
            levels[currentGo]['state']['player'][1] = levels[currentGo]['state']['player'][1] - 1#undo

        elif player in boxPos:#box to space
            x = boxPos.index(player)
            boxPos[x][1] = boxPos[x][1]+1  #needs to be changed for other moves


    if direction == "w":
        potentialMove = [player[0]-1,player[1]] #one step ahead

        if levels[currentGo]['board'][player[0]][player[1]] == "#":
            levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] + 1  # INVALID wall

        elif levels[currentGo]['board'][player[0]-1][player[1]] == "#":
            if player in boxPos:
                levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] + 1

        elif player in boxPos and potentialMove in boxPos:                                        #INVALID box to Box
            levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] + 1

        elif player in boxPos:  # box to space
            x = boxPos.index(player)
            boxPos[x][0] = boxPos[x][0] - 1


    if direction == "s":
        potentialMove = [player[0] + 1, player[1]] #one step ahead


        if levels[currentGo]['board'][player[0]][player[1]] == "#":
            print("line 1")
            levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] - 1 #INVALID into a wall

        elif levels[currentGo]['board'][player[0] + 1][player[1]] == "#":  #box to wall
            print("line 2")
            if player in boxPos:
                levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] - 1

        elif player in boxPos and potentialMove in boxPos: #box to box
            print("line 3")
            levels[currentGo]['state']['player'][0] = levels[currentGo]['state']['player'][0] - 1 #INVALID box to box

        elif player in boxPos:  #VALID box to space
            print("line 4")
            x = boxPos.index(player)
            boxPos[x][0] = boxPos[x][0] + 1  #needs to be changed for other moves


def champCheck():#checks if level is complete
    global currentGo
    global goalPos
    global boxPos
    global player
    global positions ##### change  ####
    global level
    global play


    if sorted(boxPos) == sorted(goalPos):                               #checksif goal and box coordinates match
        print("Congratulations you have completed the level.")
        currentGo += 1                                  #increments to the next level
        level = levels[currentGo]['board']              #updates the placeholder vlaues
        positions = levels[currentGo]['state']
        player = levels[currentGo]['state']['player']
        boxPos = levels[currentGo]['state']['boxes']
        goalPos = levels[currentGo]['state']['goals']
        if currentGo == 2:          #if level 2 is completed play will be set to false ending the game
            play = False



play = True


while play:

    printBoard()
    moveMaker()
    moveCheck()
    champCheck()



