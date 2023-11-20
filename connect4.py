import random
import math


board = [
    [" ", "A", "B", "C", "D", "E", "F", "G"],
    ["1", " ", " ", " ", " ", " ", " ", " "],
    ["2", " ", " ", " ", " ", " ", " ", " "],
    ["3", " ", " ", " ", " ", " ", " ", " "],
    ["4", " ", " ", " ", " ", " ", " ", " "],
    ["5", " ", " ", " ", " ", " ", " ", " "],
    ["6", " ", " ", " ", " ", " ", " ", " "]
]
def checkForWinner(board, marker):
    # Check rows
    for row in board[1:]:
        counter = 0
        for mark in row[1:]:
            if mark == marker:
                counter += 1
            else:
                counter = 0
            
            if counter >= 4:
                return True

    # Check columns
    for col in range(1, 8): 
        counter = 0
        for i in range(1, 7):  
            if board[i][col] == marker:
                counter += 1
            else:
                counter = 0
            
            if counter >= 4:
                return True


# Check diagonals
    for i in range(1, 4):
        for j in range(1, 5):
            # Check diagonal /
            if (
                board[i][j] == marker
                and board[i + 1][j + 1] == marker
                and board[i + 2][j + 2] == marker
                and board[i + 3][j + 3] == marker
            ):
                return True

            # Check diagonal \
            if (
                board[i][j + 3] == marker
                and board[i + 1][j + 2] == marker
                and board[i + 2][j + 1] == marker
                and board[i + 3][j] == marker
            ):
                return True

    return False



#AI player methods:
def get_empty_cells(board):
    return [(i, j) for i in range(1, 7) for j in range(1, 8) if board[i][j] == " "]



#Checking if the board is full
def isBoardFull(board):
    for row in board[1:]:
        for cell in row[1:]:
            if cell == " ":
                return False
    return True




    
    
    

#Prints the current Board
def printGame():       
    for row in board:
        for element in row:
            print(element, end=' ')
        print()  
        

#Main game, repeats for each possible turn    
def startGame():
    welcome = '''
    Welcome to Ryan's Connect 4

    The game is simple. Each player will have a turn placing either an X or O in a location of their choosing.
    The goal of the game is to get 4 of your markers either up, down, or diagonal.
    '''
    print(welcome)

    for turn in range(1, 43):
        printGame()

        if turn % 2 == 1:
            # Player's turn
            placeBoard, marker = getInput(turn % 2 + 1)
            updateBoard(placeBoard, marker, turn % 2 + 1)
        else:
            # AI's turn
            print("Computer is thinking...")
            move = findBestMove(board)

            if move is not None:
                placement = f"{chr(move[1] + ord('A') - 1)}{move[0]}"
                updateBoard(placement, "O", 2)
            else:
                print("AI couldn't find a valid move. Ending the game.")
                break

        if turn >= 4:
            if checkForWinner(board, marker):
                printGame()
                print(f"Game over. Player {turn % 2 + 1} ({marker}) wins!")
                return

    print("Game over. It's a tie!")


#Gets and validates the users input
def getInput(player):
    if player == 2:
        marker = "X"
        placement = input(F"Player {player} place a piece ({marker}): ")   


    else: 
        marker = "O"
        print("Computer is thinking...")
        move = findBestMove(board)
        placement = f"{chr(move[1] + ord('A') - 1)}{move[0]}"
        
    
    if len(placement) == 1 and placement[0].isalpha():
        col = ord(placement[0].upper()) - ord("A") + 1        
        if 1 <= col <= 7:
            return placement, marker
    print("Invalid input. Try again.")
    return getInput(player)

   
#updates the board    
def updateBoard(userInput, marker, player):
    upperCol = userInput.upper()
    col = ord(upperCol) - ord("A") + 1  
    row = 6 

    while row >= 1 and board[row][col] != " ":  
        row -= 1

    if row >= 1:  
        board[row][col] = marker
    else:
        print("Invalid move. Column is full. Try again.")
        printGame()
        placeBoard, marker = getInput(player)
        updateBoard(placeBoard, marker, player)

        
        

    


startGame()
