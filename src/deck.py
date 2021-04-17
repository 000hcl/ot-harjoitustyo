import random
from card import Card

class Deck:
    def __init__(self,mode):
        #easy mode
        if mode == 1:
            self.__height=3
            self.__width=4
        #normal mode
        elif mode==2:
            self.__height=4
            self.__width=5
        else:
            #hard mode
            self.__height = 5
            self.__width=6

        self.__deck = self.__create_deck(self.__height,self.__width)

    def __create_deck(self,height,width):
        max_num = height*width//2 + 1
        nums = []
        for num in range(1,max_num):
            nums.append(num)
            nums.append(num)
        random.shuffle(nums)
        deck = []

        counter = 0
        for i in range(width):
            for j in range(height):
                deck.append(Card(nums[counter],100+100*i,100+120*j))
                counter += 1
        return deck

    @property
    def deck(self):
        return self.__deck



