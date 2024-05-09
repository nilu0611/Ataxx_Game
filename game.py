import math
import random
import sys
from hashlib import new
from string import printable
from textwrap import fill

import numpy as np
import pygame
from pygame.locals import *

# define rgb codes of the used colors
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
yellow = (255,255,0)
purple = (128,0,128)
lblue = (173,216,230)
orange = (255,165,0)


def select_mode(): 
    pygame.draw.rect(screen,lblue,(0,0,0,0))
    label= myfont.render("Choose game mode",1,purple)
    screen.blit(label,(150,10))

    pygame.draw.rect(screen,orange,(0,250,600,200))

    label= myfont.render("Human vs Computer",1,purple)
    screen.blit(label,(195,350))
    
    pygame.display.update()
    a = 1
    while a > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] <50:
                    a = 1
                else:
                    posy = event.pos[1]
                    line = (posy-50)//200 
                    a = -1
                    mode = line +1 
                    pygame.draw.rect(screen,black,(0,0,600,650))
                    return mode



def difficulty(mode):    
    
    
    if mode == 2:
        pygame.draw.rect(screen,black,(0,0,600,650))
        pygame.draw.rect(screen,lblue,(0,0,600,650))
        label= myfont.render("Choose difficulty",1,purple)
        screen.blit(label,(150,10))
        pygame.draw.rect(screen,green,(0,50,600,200))
        pygame.draw.rect(screen,yellow,(0,250,600,200))
        pygame.draw.rect(screen,red,(0,450,600,200))
        label= myfont.render("Easy",1,black)
        screen.blit(label,(265,150))
        label= myfont.render("Medium",1,black)
        screen.blit(label,(242,350))
        label= myfont.render("Hard",1,black)
        screen.blit(label,(265,550))
        pygame.display.update()
        a = 1
        while a > 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] <50:
                        a = 1
                    else:
                        posy = event.pos[1]
                        line = (posy-50)//200 
                        a = -1
                        difficulty = line +1 
                        pygame.draw.rect(screen,black,(0,0,600,650))
                        return difficulty,0
    

def board():            #Choose one of the boards on the screen with a click
    pygame.draw.rect(screen,lblue,(0,0,600,50))
    label= myfont.render("Choose your board",1,purple)
    screen.blit(label,(150,10))
    b1 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b1.png')
    b1 = pygame.transform.scale(b1,(197,197))
    b2 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b2.png')
    b2 = pygame.transform.scale(b2,(197,197))
    b3 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b3.png')
    b3 = pygame.transform.scale(b3,(197,197))
    b4 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b4.png')
    b4 = pygame.transform.scale(b4,(197,197))
    b5 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b5.png')
    b5 = pygame.transform.scale(b5,(197,197))
    b6 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b6.png')
    b6 = pygame.transform.scale(b6,(197,197))
    b7 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b7.png')
    b7 = pygame.transform.scale(b7,(197,197))
    b8 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b8.png')
    b8 = pygame.transform.scale(b8,(197,197))
    b9 = pygame.image.load(r'C:\Users\NiluBB\Documents\AI_project_1\AI_project\b9.png')
    b9 = pygame.transform.scale(b9,(197,197))
    screen.blit(b1,(0,50))
    screen.blit(b2,(200,50))
    screen.blit(b3,(400,50))
    screen.blit(b4,(0,250))
    screen.blit(b5,(200,250))
    screen.blit(b6,(400,250))
    screen.blit(b7,(0,450))
    screen.blit(b8,(200,450))
    screen.blit(b9,(400,450))
    pygame.draw.rect(screen,green,(197,50,3,600))
    pygame.draw.rect(screen,green,(397,50,3,600))
    pygame.draw.rect(screen,green,(0,247,600,3))
    pygame.draw.rect(screen,green,(0,447,600,3))
    pygame.display.update()
    a = 1
    while a > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] <50:
                    a = 1
                else:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = posx//200
                    lin = (posy-50)//200
                    a = -1
                    r = 3*lin + col +1
                    return r



def characteristics(nboard):     #for each of the predefined boards, return the associated characteristics
    if nboard==1:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,0,0,0,2],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,0,0,0,0,0,1]])
    elif nboard==2:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[3,1,0,0,0,0,3],[0,3,0,0,0,3,2],[0,0,3,0,3,0,0],[0,0,0,3,0,0,0],[0,0,3,0,3,0,0],[2,3,0,0,0,3,0],[3,0,0,0,0,1,3]])
    elif nboard ==3:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[3,1,0,0,0,0,3],[0,0,0,0,3,0,2],[0,3,3,0,3,0,0],[0,0,0,0,0,0,0],[0,0,3,0,3,3,0],[2,0,3,0,0,0,0],[3,0,0,0,0,1,3]])
    elif nboard == 4:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,0,0,0,2],[0,3,3,0,3,3,0],[0,3,0,0,0,3,0],[0,0,0,0,0,0,0],[0,3,0,0,0,3,0],[0,3,3,0,3,3,0],[2,0,0,0,0,0,1]])
    elif nboard ==5:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,3,0,0,0,3,2],[0,3,0,0,0,3,0],[0,0,0,0,0,0,0],[0,0,0,3,0,0,0],[0,0,0,0,0,0,0],[0,3,0,0,0,3,0],[2,3,0,0,0,3,1]])
    elif nboard ==6:
        line,col = 10,10
        squaresize = 600/10
        board = np.array([[1,0,3,0,2,1,0,3,0,2],[0,0,3,0,0,0,0,3,0,0],[0,0,3,3,3,3,3,3,0,0],[0,0,3,0,0,0,0,3,0,0],[2,0,3,0,1,2,0,3,0,1],[1,0,3,0,2,1,0,3,0,2],[0,0,3,0,0,0,0,3,0,0],[0,0,3,3,3,3,3,3,0,0],[0,0,3,0,0,0,0,3,0,0],[2,0,3,0,1,2,0,3,0,1]])
    elif nboard == 7:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,3,0,0,2],[0,0,3,0,3,0,0],[0,3,0,0,0,3,0],[0,0,3,0,3,0,0],[0,3,0,0,0,3,0],[0,0,3,0,3,0,0],[2,0,0,3,0,0,1]])
    elif nboard == 8:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,0,0,0,2],[0,0,0,0,0,0,0],[3,3,0,0,0,3,3],[0,0,0,0,0,0,0],[3,3,0,0,0,3,3],[0,0,0,0,0,0,0],[2,0,0,0,0,0,1]])
    elif nboard == 9:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,3,3,3,0,2],[0,0,0,0,0,0,0],[0,0,3,3,3,0,0],[0,0,0,0,0,0,0],[0,0,3,3,3,0,0],[0,0,0,0,0,0,0],[2,0,3,3,3,0,1]])
    return line,col,squaresize,board



def draw_board(board):         #receives a representative matrix of the board and transforms it into an image
    a = 0
    v = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] != 3:     #paints the square white if it is playable, and depending on what is there, paints (or not) a circle of that color 
                pygame.draw.rect(screen,white,(c * squaresize,(l) * squaresize+50,squaresize-1,squaresize-1))
                if board[l,c] == 1:
                    pygame.draw.circle(screen,blue,(int(c * squaresize + squaresize/2),int((l) * squaresize+ 50 + squaresize/2)),squaresize/2-10)
                    a += 1
                if board[l,c] == 2:
                    pygame.draw.circle(screen,red,(int(c * squaresize + squaresize/2),int((l) * squaresize +50 + squaresize/2)),squaresize/2-10)
                    v +=1
    a = str(a)
    v = str(v)
    #creates the piece counters
    pygame.draw.rect(screen,lblue,(0,0,130,50))
    pygame.draw.rect(screen,lblue,(500,0,100,50))
    label1 = myfont.render(a,1,blue)
    screen.blit(label1,(10,15))
    label2 = myfont.render(v,1,red)
    screen.blit(label2,(550,15))
    pygame.draw.circle(screen,blue,(60,30),12)
    pygame.draw.circle(screen,red,(530,30),12)
    pygame.display.update()


def action(board,player,line,col):          #receives clicks until they form a valid move
    b = 1   
    while b > 0:  #receives a pair of clicks that define a move and accepts it if it is valid
        a = 1
        while a > 0:    #receives the first click and accepts it if it is a piece belonging to the player
            for l in range(line):
                for c in range(col):
                    if board[l,c] == 0:
                        pygame.draw.rect(screen,white,(c * squaresize,(l) * squaresize+50,squaresize-1,squaresize-1))
                        pygame.display.update()
            x1,y1 = selection()
            if board[x1-1,y1-1] == player:
                a = -1
        c = 0
        
        
        for i in range(x1-2,x1+3):
            for k in range(y1-2,y1+3):
                if valid_move(board,x1,y1,i,k,line,col,player):
                    pygame.draw.rect(screen,green,((k-1) * squaresize + squaresize/5,(i-1) * squaresize + squaresize/5+50 ,3*squaresize/5,3*squaresize/5))
                    pygame.draw.rect(screen,white,((k-1) * squaresize + squaresize/4,(i-1) * squaresize + squaresize/4 +50 ,squaresize/2,squaresize/2))
                    pygame.draw.rect(screen,white,((k-1) * squaresize + 4*squaresize/10,(i-1) * squaresize+50,squaresize/5,squaresize-1))
                    pygame.draw.rect(screen,white,((k-1) * squaresize,(i-1) * squaresize+ 4*squaresize/10 +50,squaresize-1,squaresize/5))
                    pygame.display.update()               
                    c = 1
        if c == 1:      #if the selected piece can be moved
            x2,y2 = selection()
            if valid_move(board,x1,y1,x2,y2,line,col,player):
                b = -1
    return x1,y1,x2,y2


def selection():       #transforms a click into its respective position on the board
    a = 1
    while a > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                x1 = int((posy-50)//squaresize +1)
                y1 = int(posx//squaresize + 1)
                a = -1
    return(x1,y1)


def valid_move(board,x1,y1,x2,y2,line,col,player):              #checks if the move is valid
    if x1<1 or x1>line or y1<1 or y1>col or x2<1 or x2>line or y2<1 or y2>col:   # if the position belongs to the board
        return False
    if board[x1-1,y1-1] != player:   #if the piece belongs to the player
        return False
    if board[x2-1,y2-1] != 0:   #if the square we are going to move the piece to is empty
        return False
    if x2==x1 and y2==y1:    #if the move does not move the piece
        return False
    if abs(x2-x1)>2 or abs(y2-y1)>2:   #if the move moves the piece more than it should
        return False
    if abs(x2-x1) + abs(y2-y1) == 3:
        return False
    return True


def move(board,x1,y1,x2,y2,line,col,player):            #executes the desired move if it is valid        
    if valid_move(board,x1,y1,x2,y2,line,col,player):                                 
        if abs(x2-x1)>1 or abs(y2-y1)>1:            
            board[x1-1,y1-1] = player  #if the move is a jump move
            board[x2-1,y2-1] = player
        else:                                     #if the move is an expansion move
            board[x2-1,y2-1] = player
    return board



def capture(board,x2,y2,line,col,player):             #After a move, check if it captures pieces from the opponent
    for k in range (x2-2,x2+1):
        if k >= 0 and k <= line-1:
            for l in range(y2-2,y2+1):
                if l >= 0 and l <= col-1:
                    if board[k,l] == 3-player:
                        board[k,l] = player
    return board

def available_moves(board,player,line,col):             #Check if the player has valid moves
    for i in range(1,line+1):
        for j in range(1,col+1):
            if board[i-1,j-1]==int(player):
                for k in range(i-2,i+3):
                    for l in range(j-2,j+3):
                        if valid_move(board,i,j,k,l,line,col,player):
                            return True
    return False

def fill_board(board,line,col,player,actual_board):  #Fills the empty spaces with pieces belonging to the player
    if actual_board:
        pygame.draw.rect(screen,lblue,(0,0,600,50))
        if player == 1:
            label1 = myfont.render("Player 2 has no valid moves",1,black)
            label = myfont.render("Player 1's turn",1,blue)
        else:
            label1 = myfont.render("Player 1 has no valid moves",1,black)
            label = myfont.render("Player 2's turn",1,red)
        screen.blit(label1,(65,10))
        pygame.display.update()
        pygame.time.wait(1500)
        pygame.draw.rect(screen,lblue,(0,0,600,50))
        screen.blit(label,(165,10))
        pygame.display.update()
    for l in range(line):
        for c in range(col):
            if board[l,c] == 0:
                board[l,c] = player
                if actual_board:
                    draw_board(board)
                    pygame.time.wait(250)
    return board

def count_pieces(board,line,col):  #Counts the number of pieces on the board
    count = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == 1 or board[l,c] == 2:
                count += 1
    return count

def force_game_over(board,line,col):  #Determines a winner even if the game state is not final, by choosing the player with the most pieces
    a = 0
    v = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == 1:
                a += 1
            if board[l,c] == 2:
                v += 1
    if a > v:
        return 1
    if a < v:
        return 2
    if a == v:
        return 0

def game_over(board,line,col,actual_board):              #Checks if the game has ended, and in that case, returns the winner
    winner = -1
    if not available_moves(board,1,line,col) and available_moves(board,2,line,col):#The victory condition for Player 1
        board = fill_board(board,line,col,2,actual_board)
        winner = force_game_over(board,line,col)
    elif not available_moves(board,2,line,col) and available_moves(board,1,line,col):#The victory condition for Player 2
        board = fill_board(board,line,col,1,actual_board)
        winner = force_game_over(board,line,col)
    elif not available_moves(board,1,line,col) and not available_moves(board,2,line,col):  # The draw condition
        c1 = 0
        c2 = 0
        for i in range(line):
            for j in range(col):
                if board[i,j] == 1:
                    c1 += 1
                elif board[i,j] == 2:
                    c2 += 1
        if c1 == c2:
            winner = 0
        elif c1 > c2:
            winner = 1
        else:
            winner = 2
    return winner


def heuristic(board,line,col,player):       #Evaluates the game state for the player
    otherplayer = 3 - player
    points = 0   #Difference between the number of pieces of the player and the opponent
    if game_over(board,line,col,False) == player:         #If the game has been won
        return 500
    elif game_over(board,line,col,False) == otherplayer:  #If the game has been lost
        return -500
    elif game_over(board,line,col,False) == 0:            #If the game ended in a tie.
        return 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == player:
                points += 1
            elif board[l,c] == otherplayer:
                points -= 1
            
    return points


def every_move(board,line,col,player):   #Returns all available moves for the player
    moves = []
    for l in range(1,line+1):
            for c in range(1,col+1):
                if board[l-1,c-1] == player:
                    for i in range(l-2,l+3):
                        for k in range(c-2,c+3):                                
                            if valid_move(board,l,c,i,k,line,col,player):
                                moves.append([l,c,i,k])
    return moves

def random_move(board,line,col,player):     #Returns a random move from the available moves
    moves = every_move(board,line,col,player)
    r = random.randint(0,len(moves)-1)
    acting= moves[r]
    return acting

def best_move(board,line,col,player):   #Implementation of the greedy algorithm, where among all possible moves, it returns the one with the best evaluation after its execution
    
    moves = every_move(board,line,col,player)
    b_move = moves[random.randint(0,len(moves)-1)]  #To make the AI less predictable
    tempboard = board.copy()
    max_score = heuristic(move(tempboard,b_move[0],b_move[1],b_move[2],b_move[3],line,col,player),line,col,player) 
    for a in range(len(moves)):
        tempboard = board.copy()
        x1,y1,x2,y2 = moves[a][0],moves[a][1],moves[a][2],moves[a][3]
        tempboard = move(tempboard,x1,y1,x2,y2,line,col,player)
        tempboard = capture(tempboard,x2,y2,line,col,player)
        if heuristic(tempboard,line,col,player) > max_score:
            b_move = moves[a]       
            max_score = heuristic(tempboard,line,col,player)
    return b_move


def minimax(board,depth,alpha,beta,maximizingplayer,player):  #Implementation of the minimax algorithm with alpha-beta pruning, where it returns the move that ensures a better position within a depth of plays
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
    if (player == 2 and maximizingplayer) or (player == 1 and not maximizingplayer): #If it is Player 2's turn to play
        valid_moves = every_move(board,line,col,2)
    else:                                                                            #If it is Player 1's turn to play
        valid_moves = every_move(board,line,col,1)
    if depth == 0 or game_over(board,line,col,False) != -1:
        if game_over(board,line,col,False) != -1:
            if game_over(board,line,col,False) == player:         #If we win the game
                return (None,10000000)
            elif game_over(board,line,col,False) == 3-player:     #If we lose the game
                return (None,-10000000)
            else:                                          #If we tie the game
                return (None,0)
        else:                                                #If we reach the desired depth
            return (None,heuristic(board,line,col,player))
    if maximizingplayer:      #If it is 'max' (maximizing player) to play
        value = -math.inf
        for movement in valid_moves:
            board_copy = board.copy()
            x1,y1,x2,y2 = movement[0],movement[1],movement[2],movement[3]
            board_copy = move(board_copy,x1,y1,x2,y2,line,col,player)
            board_copy = capture(board_copy,movement[2],movement[3],line,col,player)
            new_value = minimax(board_copy,depth-1,alpha,beta,False,player)[1]      #Until we reach a final state or the desired depth
            if new_value > value:               #If we obtain a 'better' move
                value = new_value
                mov = movement
            if value >= beta:    #If it is impossible to obtain a 'better' move
                break
            alpha = max(alpha,value)
        return mov,value
    else:                     #if it is 'min' (minimizing player) to play
        value = math.inf
        for movement in valid_moves:
            board_copy = board.copy()
            x1,y1,x2,y2 = movement[0],movement[1],movement[2],movement[3]
            board_copy = move(board_copy,x1,y1,x2,y2,line,col,3-player)
            board_copy = capture(board_copy,movement[2],movement[3],line,col,3-player)
            new_value = minimax(board_copy,depth-1,alpha,beta,True,player)[1]   #Until we reach a final state or the desired depth
            if new_value < value:   #If we obtain a 'better' move
                value = new_value
                mov = movement
            if value <= alpha:      #If it is impossible to obtain a 'better' move.
                break
            beta = min(beta,value)
        return mov,value




def main_game(board,line,col,mode,difficulty1,difficulty2): #Runs the game until it finishes, based on the game mode, the chosen board, and (possibly) the difficulty of the AI
    winner = game_over(board,line,col,True)
    player = int(random.randint(1,2))       #Randomly determines the first player
    current = 0                               #Number of pieces on the current board
    lnpieces = 0                            #Number of pieces on the board before the last move
    
    if mode == 2:
        while winner == -1:   #Game loop
            pygame.draw.rect(screen,lblue,(0,0,600,50))
            if player == 1:
                label = myfont.render("Player 1's turn",1,blue)
                screen.blit(label,(165,10))
                draw_board(board)       
                pygame.display.update()
                x1,y1,x2,y2 = action(board,player,line,col)                             
                board = move(board,x1,y1,x2,y2,line,col,player)
                board = capture(board,x2,y2,line,col,player)
                draw_board(board)
                pygame.display.update()
            elif player == 2:
                label = myfont.render("Computer's turn",1,red)
                screen.blit(label,(250,10))
                draw_board(board)
                pygame.display.update()
                pygame.time.wait(500) 
                if difficulty1 == 1:
                        act= random_move(board,line,col,player) 
                        pygame.time.wait(500)
                elif difficulty1 == 2:
                        act= best_move(board,line,col,player) 
                        pygame.time.wait(500)
                elif difficulty1 == 3:
                    if nboard == 6:
                        act= minimax(board,2,-math.inf,math.inf,True,player)[0]
                    else:
                        act= minimax(board,3,-math.inf,math.inf,True,player)[0]
                #Move determined based on the difficulty of the AI
                x1,y1,x2,y2 = act[0],act[1],act[2],act[3]
                board = move(board,x1,y1,x2,y2,line,col,player)
                board = capture(board,x2,y2,line,col,player)
                pygame.display.update()   
            npieces = count_pieces(board,line,col)
            if npieces == lnpieces:
                current += 1
            else:
                current = 0
            lnpieces = npieces 
            if current >= 30:   
                winner = force_game_over(board,line,col)           
            draw_board(board)
            pygame.display.update()
            winner = game_over(board,line,col,True)
            player = 3 - player 
        pygame.draw.rect(screen,lblue,(0,0,600,50))
    
    #After the game has ended, check who won
    if winner == 0:
        label = myfont.render("Draw",1,green)
        screen.blit(label,(260,10))
    elif winner == 1:
        label = myfont.render("Player 1 won!",1,blue)
        screen.blit(label,(165,10))
    elif winner == 2:
        label = myfont.render("Player 2 won!",1,red)
        screen.blit(label,(165,10))
    a = 0
    v = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == 1:
                a +=1
            elif board[l,c] == 2:
                v += 1
    a = str(a)
    v = str(v)
    label1 = myfont.render(a,1,blue)
    screen.blit(label1,(10,15))
    label2 = myfont.render(v,1,red)
    screen.blit(label2,(550,15))
    pygame.draw.circle(screen,blue,(60,30),12)
    pygame.draw.circle(screen,red,(530,30),12)
    pygame.display.update()
    pygame.time.wait(5000)


pygame.init()
size = (600,650)
screen = pygame.display.set_mode(size)  #Creates the game window
myfont = pygame.font.SysFont("monospace", 30)  #Sets the font type
mode = select_mode()  #Selects the game mode
difficulty1,difficulty2 = difficulty(mode)#Chooses the difficulty level
nboard = board()  #Chooses the game board
line,col,squaresize,board = characteristics(nboard)

pygame.draw.rect(screen,black,(0,0,600,700))
main_game(board,line,col,mode,difficulty1,difficulty2)  #Runs the game