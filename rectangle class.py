import pygame
pygame.init()
playing = True
screen = pygame.display.set_mode((800,800))
class Rect():
    def __init__(self,color,dimensions):
        self.c = color
        self.d = dimensions
        self.s = screen
    def draw(self):
        pygame.draw.rect(self.s,self.c,self.d)
rect1 = Rect('white', (0, 0, 100, 100))

while playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    screen.fill("black")
    x = 0
    x2 = 100
    x3 = 0
    x4 = 100
    x5 = 0
    x6 = 100
    x7 = 0
    x8 = 100
    

    for i in range (4):
        rect = Rect("white", (x,0,100,100))
        x = x+200
        rect.draw()
    for i in range (4):
        rect1 = Rect("white", (x2,100,100,100))
        x2 = x2+200
        rect1.draw()
    for i in range (4):
        rect2 = Rect("white", (x3,200,100,100))
        x3 = x3+200
        rect2.draw()
    for i in range (4):
        rect3 = Rect("white", (x4,300,100,100))
        x4 = x4+200
        rect3.draw()
    for i in range (4):
        rect4 = Rect("white", (x5,400,100,100))
        x5 = x5+200
        rect4.draw()
    for i in range (4):
        rect5 = Rect("white", (x6,500,100,100))
        x6 = x6+200
        rect5.draw()
    for i in range (4):
        rect6 = Rect("white", (x7,600,100,100))
        x7 = x7+200
        rect6.draw()
    for i in range (4):
        rect7 = Rect("white", (x8,700,100,100))
        x8 = x8+200
        rect7.draw()
    
    pygame.display.update()

