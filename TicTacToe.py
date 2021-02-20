# Tic-Tac-Toe with minimax algorithm
# Jeffrey Lin

import pygame
import random
import time
import math

# Preset colours for the GUI of the game
white = (255, 255, 255)
blue = (230, 230, 255)
grey = (192, 192, 192)
black = (0, 0, 0)
red = (192, 0, 0)
orange = (255, 230, 230)
green = (230, 255, 230)

# Pygame and variable initialization
pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Tic Tac Toe")
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.display.set_icon(pygame.image.load('tic-tac-toe.png'))
font = pygame.font.SysFont('text.ttf', 65)
fontSmall = pygame.font.SysFont('text.ttf', 35)
fontMed = pygame.font.SysFont('text.ttf', 45)
p1Score = 0
p2Score = 0
outcomes = 0
mode = 1
playerTurn = ''
mouseClick = 100000


# Redraws the screen everytime a new game is started
def newGame():
    global playerTurn
    global movesMade
    global board
    global mouseClick
    global mode
    global font
    global outcomes
    global p1Score
    global p2Score
    screen.fill(grey)
    pygame.draw.rect(screen, green, (0, 650, 300, 50))
    pygame.draw.rect(screen, white, (0, 0, 600, 50))
    pygame.draw.rect(screen, orange, (300, 650, 300, 50))
    pygame.draw.line(screen, white, (200, 50), (200, 650), 5)
    pygame.draw.line(screen, white, (400, 50), (400, 650), 5)
    pygame.draw.line(screen, white, (0, 250), (600, 250), 5)
    pygame.draw.line(screen, white, (0, 450), (600, 450), 5)
    pygame.draw.line(screen, white, (0, 50), (600, 50), 5)
    pygame.draw.line(screen, white, (0, 650), (600, 650), 5)
    pygame.draw.line(screen, white, (300, 650), (300, 700), 5)
    resetText = font.render('RESET', True, black)
    p1ScoreText = fontSmall.render('Player 1: ' + str(p1Score), True, black)
    p2ScoreText = fontSmall.render('Player 2: ' + str(p2Score), True, black)
    screen.blit(resetText, (375, 657))
    gameMode()
    screen.blit(p1ScoreText, (0, 1))
    screen.blit(p2ScoreText, (0, 26))
    # Randomly chooses a player to go first
    randomNum = random.randint(0, 1)
    outcomes = 0
    if randomNum == 0:
        playerTurn = 'x'
        firstPlayer = fontMed.render('Player 1 goes first!', True, black)
        screen.blit(firstPlayer, (220, 15))
        mouseClick = 1
    else:
        if mode == 1:
            firstPlayer = fontMed.render('Computer goes first!', True, black)
            mouseClick = 1000000
        else:
            firstPlayer = fontMed.render('Player 2 goes first!', True, black)
            mouseClick = 1
        screen.blit(firstPlayer, (220, 15))
        playerTurn = 'y'
    movesMade = 0
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    pygame.display.update()


# Checks if a player wins, return x for P1, y for P2, t for tie, and n for no one
def checkWin(board, realGame):
    global movesMade
    global red

    for i in range(3):
        if board[0][i] == board[1][i] and board[2][i] == board[1][i] and not board[1][i] == '':
            if realGame == True:
                pygame.draw.line(screen, red, (30, 150 + (200 * i)), (570, 150 + (200 * i)), 7)
            return board[1][i]
        elif board[i][0] == board[i][1] and board[i][2] == board[i][1] and not board[i][1] == '':
            if realGame == True:
                pygame.draw.line(screen, red, (100 + (i * 200), 80), (100 + (i * 200), 620), 7)
            return board[i][1]
    if board[0][0] == board[1][1] and board[2][2] == board[1][1] and not board[1][1] == '':
        if realGame == True:
            pygame.draw.line(screen, red, (30, 80), (570, 620), 7)
        return board[1][1]
    elif board[2][0] == board[1][1] and board[0][2] == board[1][1] and not board[1][1] == '':
        if realGame == True:
            pygame.draw.line(screen, red, (570, 80), (30, 620), 7)
        return board[1][1]
    elif movesMade == 9:
        return 't'

    flag = True;
    for i in range(3):
        for k in range(3):
            if board[i][k] == '':
                flag = False
    if flag == True:
        return 't'
    return 'n'


# Updates score and starts new game
def gameOver(winner):
    global p1Score
    global p2Score
    if winner == 'x':
        p1Score += 1
    elif winner == 'y':
        p2Score += 1
    pygame.display.update()
    time.sleep(2)
    newGame()


# Draws the X's and O's to screen
def drawShape(x, y):
    global playerTurn
    global movesMade
    global board
    if (playerTurn == 'x' and board[x][y] == ''):
        playerTurn = 'y'
        pygame.draw.line(screen, black, (33 + (200 * x), 83 + (200 * y)), (167 + (200 * x), 217 + (200 * y)), 3)
        pygame.draw.line(screen, black, (167 + (200 * x), 83 + (200 * y)), (33 + (200 * x), 217 + (200 * y)), 3)
        board[x][y] = 'x'
        movesMade += 1
    elif board[x][y] == '':
        playerTurn = 'x'
        pygame.draw.circle(screen, black, (100 + (200 * x), 150 + (200 * y)), 68, 2)
        board[x][y] = 'y'
        movesMade += 1
    winner = checkWin(board, True)
    if winner == 'x' or winner == 'y' or winner == 't':
        gameOver(winner)


# Controls what happens when parts of the screen are clicked
def clickButton(x, y):
    global mode
    global mouseClick
    if (y > 50 and mouseClick == 1):
        if x < 200 and y > 50 and y < 250:
            drawShape(0, 0)
        if x < 200 and y > 250 and y < 450:
            drawShape(0, 1)
        if x < 200 and y > 450 and y < 650:
            drawShape(0, 2)
        if x > 200 and x < 400 and y > 50 and y < 250:
            drawShape(1, 0)
        if x > 200 and x < 400 and y > 250 and y < 450:
            drawShape(1, 1)
        if x > 200 and x < 400 and y > 450 and y < 650:
            drawShape(1, 2)
        if x > 400 and x < 600 and y > 50 and y < 250:
            drawShape(2, 0)
        if x > 400 and x < 600 and y > 250 and y < 450:
            drawShape(2, 1)
        if x > 400 and x < 600 and y > 450 and y < 650:
            drawShape(2, 2)
    if x < 300 and y > 650:
        if mode == 1:
            mode = 2
        else:
            mode = 1
        gameMode()
    if x > 300 and y > 650:
        reset()


# Changes game mode from PvP to Player vs AI
def gameMode():
    global mode
    pygame.draw.rect(screen, green, (0, 650, 300, 50))
    pygame.draw.line(screen, white, (0, 650), (600, 650), 5)
    pygame.draw.line(screen, white, (300, 650), (300, 700), 5)
    if mode == 1:
        gameModeText = font.render('PvE', True, black)
    else:
        gameModeText = font.render('PvP', True, black)
    screen.blit(gameModeText, (110, 657))


# Ressts the scores and the game
def reset():
    global p1Score
    global p2Score
    p1Score = 0
    p2Score = 0
    newGame()


# This recursive function finds the best move of the current board by calculating all outcomes
# Optimized with alpha beta pruning that decreases the number of nodes the minimax algorithm needs to search
def minimax(board, depth, alpha, beta, player):
    global outcomes
    # Checks if game has been won
    winner = checkWin(board, False)
    if winner == 'x':
        outcomes += 1
        return [(-10 + depth), 0, 0]
    if winner == 'y':
        outcomes += 1
        return [(10 - depth), 0, 0]
    if winner == 't':
        outcomes += 1
        return [0, 0, 0]
    # Goes through all moves for the computer
    if player == 'y':
        value = [-math.inf, 0, 0]
        for i in range(3):
            for k in range(3):
                if board[i][k] == '':
                    board[i][k] = 'y'
                    bestMove = minimax(board, depth + 1, alpha, beta, 'x')
                    board[i][k] = ''
                    bestMove[1] = i
                    bestMove[2] = k
                    if bestMove[0] > value[0]:
                        value[0] = bestMove[0]
                        value[1] = bestMove[1]
                        value[2] = bestMove[2]
                    alpha = max(alpha, bestMove[0])
                    if beta <= alpha:
                        break
        return value
    # Goes through all moves for the player
    else:
        value = [math.inf, 0, 0]
        for i in range(3):
            for k in range(3):
                if board[i][k] == '':
                    board[i][k] = 'x'
                    bestMove = minimax(board, depth + 1, alpha, beta, 'y')
                    board[i][k] = ''
                    bestMove[1] = i
                    bestMove[2] = k
                    if bestMove[0] < value[0]:
                        value[0] = bestMove[0]
                        value[1] = bestMove[1]
                        value[2] = bestMove[2]
                    beta = min(beta, bestMove[0])
                    if beta <= alpha:
                        break
        return value


running = True
newGame()

# Main game loop
# Checks for input
while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                clickButton(mouseX, mouseY)
            # Goes through each move on the board and minimaxes that move
    # I did it seperately in case there were too many recursive calls if I did it in one go
    if mode == 1 and playerTurn == 'y':
        value = [-math.inf, 0, 0]
        for i in range(3):
            for k in range(3):
                if board[i][k] == '':
                    board[i][k] = 'y'
                    bestScore = minimax(board, 0, -math.inf, math.inf, 'x')
                    board[i][k] = ''
                    bestScore[1] = i
                    bestScore[2] = k
                    if bestScore[0] > value[0]:
                        value[0] = bestScore[0]
                        value[1] = bestScore[1]
                        value[2] = bestScore[2]
        # Uncomment the line below to see how many outcomes are calculated per move by the algorithm
        # print('Calculated: ' + str(outcomes) + ' outcomes.')
        clickButton(1 + (value[1] * 200), 51 + (value[2] * 200))
        mouseClick = 1
        outcomes = 0
    pygame.display.update()
