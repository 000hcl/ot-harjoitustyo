import pygame
from card import Card
import random

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((1000,800))

class Level:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.deck = self.createCards()
        self.firstCard = None
        self.secondCard = None
        self.pairs = 0
        self.loop()
    
    def createCards(self):
        #INCOMPLETE
        max_num = self.height*self.width//2 + 1
        nums = []
        for num in range(1,max_num):
            nums.append(num)
            nums.append(num)
        random.shuffle(nums)
        deck = []

        counter = 0
        for i in range(self.width):
            for j in range(self.height):
                deck.append(Card(nums[counter],100+100*i,100+120*j))
                counter += 1

        return deck
    
    def renderCards(self):
        for card in self.deck:
            window.blit(card.getCard(),card.getPos())

    def findClickedCard(self, x: int, y: int):
        for card in self.deck:
            c_x1 = card.x
            c_x2 = card.x2
            c_y = card.y
            c_y2 = card.y2
            if x >= c_x1 and x<=c_x2 and y>=c_y and y<=c_y2:
                return card
        return None
    
    def flipOrDeletePair(self):
        if self.firstCard != None and self.secondCard != None:
            if self.firstCard.nr != self.secondCard.nr:
                self.firstCard.flip()
                self.secondCard.flip()
                self.resetPair()
            else:
                self.deck.remove(self.firstCard)
                self.deck.remove(self.secondCard)
                self.resetPair
    
    def checkIfMatching(self, card: Card):
        
        
        if self.firstCard == None:
            self.firstCard = card
        elif self.secondCard == None:
            self.secondCard = card
        else:
            self.firstCard = card
            self.secondCard = None
        if self.firstCard != None and self.secondCard != None:
            if self.firstCard.nr == self.secondCard.nr:
                self.pairs += 1
    
    def resetPair(self):
        self.firstCard = None
        self.secondCard = None
            
    def gameEnded(self):
        end = True
        for card in self.deck:
            if card.shown == False:
                end = False
        return end

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    card = self.findClickedCard(mousePos[0],mousePos[1])
                    if card != None and card.shown == False:
                        self.flipOrDeletePair()
                        card.flip()
                        self.checkIfMatching(card)
            if self.gameEnded():
                exit()
            

            
            window.fill((190,200,200))
            self.renderCards()
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    Level(4,5)
    


