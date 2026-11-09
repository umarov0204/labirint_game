import pygame
from config import *


class Persbody:
    def __init__(self, x, y, perx, pery, percolor):
        self.rect = pygame.Rect(x, y, perx, pery)
        self.direction = "RIGHT"
        self.speed = 10
        self.color = percolor



    # personajni yurgizish qismi

    def change_direction(self, direction):

        # teskari yo'nalishni bloklash
        if self.direction == "RIGHT" and direction == "LEFT":
            return
        if self.direction == "LEFT" and direction == "RIGHT":
            return
        if self.direction == "UP" and direction == "DOWN":
            return
        if self.direction == "DOWN" and direction == "UP":
            return

        self.direction = direction


    def move(self):

        # harakat
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed




    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=4)

        # screen.blit(self)



        
