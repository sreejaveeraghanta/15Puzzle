import pygame
import random

pygame.init()
scrn_width = 415
scrn_height = 450
k = 10
screen = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("15Puzzle")

start = pygame.font.Font(pygame.font.get_default_font(), 30)
numbers = pygame.font.Font(pygame.font.get_default_font(), 20)
class button:
    def __init__(self, colour, x, y, text= ""):
        self.color = colour
        self.x = x
        self.y = y
        self.text = text
        self.clicked = False

    def draw(self, win):
        pygame.draw.rect(win, (250, 250, 250), (self.x, self.y,104, 104 ), 0, 5)
        pygame.draw.rect(win, self.color, (self.x+2, self.y+2, 100, 100), 0, 5)
        if self.text != "":
            font = numbers.render(self.text, True, (0,0,0))
            win.blit(font, (self.x + 45, self.y +45))

    def drawStart(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 100, 20), 0)
        theText = start.render(self.text, True, (250, 250, 250))
        screen.blit(theText, (self.x, self.y))

    def close(self, pos):
        if pos[0] > self.x and pos[0] < self.x + 100:
            if pos[1] > self.y and pos[1] < self.y + 100:
                return True
        return False

    def move(self, newPosX, newPosY):
        pygame.draw.rect(screen, self.color, (newPosX, newPosY, 104, 104), 0, 5)

    def adjacent(self, button):
        if ((blank.x == button.x + 105 or blank.x == button.x - 105) and blank.y == button.y):
            return True
        elif((blank.y == button.y + 105 or blank.y == button.y - 105) and blank.x == button.x):
            return True
        return False

def shuffle(board):
    for element in board:
        rand = random.choice(board)
        swap(element, rand)

def swap(button1, button2):
    tempX = button1.x
    tempY = button1.y
    button1.x = button2.x
    button1.y = button2.y
    button2.x = tempX
    button2.y = tempY
    button2.move(button2.x, button2.y)
    button1.move(button1.x, button1.y)


one = button((152, 245, 255), 0, 0, '1')
two = button((152, 245, 255), 105, 0, '2')
three = button((152, 245, 255), 210, 0, '3')
four = button((152, 245, 255), 315, 0, '4')
five = button((152, 245, 255), 0, 105, '5')
six = button((152, 245, 255), 105, 105, '6')
seven = button((152, 245, 255), 210, 105, '7')
eight = button((152, 245, 255), 315, 105, '8')
nine = button((152, 245, 255), 0, 210, '9')
ten = button((152, 245, 255), 105, 210, '10')
eleven = button((152, 245, 255), 210, 210, '11')
twelve = button((152, 245, 255), 315, 210, '12')
thirteen = button((152, 245, 255), 0, 315, '13')
fourteen = button((152, 245, 255), 105, 315, '14')
fifteen = button((152, 245, 255), 210, 315, '15')
blank = button((0, 0, 0), 315, 315, " ")

startButton = button((0, 0, 0), 300, 420, "Start")
gameBoard = [one, two, three, four, five,  six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen]

Finished = False
while not Finished:
    screen.fill((0,0,0))
    startButton.drawStart()

    for element in gameBoard:
        element.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finished = True
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if startButton.close(mousePos):
                startButton.text = "Reset"
                shuffle(gameBoard)
            for buttons in gameBoard:
                if buttons.close(mousePos):
                    if blank.adjacent(buttons):
                        swap(blank, buttons)

    pygame.display.update()
pygame.quit()

