import sys

from threading import *

import pygame
import time

pygame.font.init()
pygame.display.set_caption("Speed Reader")
screen = pygame.display.set_mode((1000, 600))
background = (0, 0, 255)
screen.fill(background)
myFont = pygame.font.Font(None, 90)
# fn = open("read.txt","w")
# fn.close()
f = open("read.txt", "r")

a = 'gajendra'

class A(Thread):
    def run(self):
        for line in f:
            for word in line.split():
                text = myFont.render(word, True, (255, 255, 0))
                screen.blit(text, (300, 300))
                pygame.display.update()
                time.sleep(0.2)
                screen.fill(background)
                pygame.display.update()
                if a in line:
                    sys.exit(0)
                    pygame.display.quit()

t3 = A()
t3.start()
