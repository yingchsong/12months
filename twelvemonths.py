import random
from collections import deque
class Twelvemonths:
    def __init__(self):
        self.cards=[i for i in range(12)]*4 # all 48 cards
        self.records={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0} # record the number of cards that are choosed
        self.order_of_stack=0 # which stack is being used
        self.outer=-1 # the card that is taken

    def shuffle(self):
        random.shuffle(self.cards)
        # give a random order for cards
        # you need to do it before playing games
        

    def split(self): # split the list into a nested list which shape is (12,4)
        tmp=self.cards
        self.cards=[]
        for i in range(12):
            self.cards+=[deque(tmp[i*4:i*4+4])] # there I use deque to control 

    def move(self): # move one card in the bottom of one stack to the stack it belongs
        self.outer=self.cards[self.order_of_stack][-1]
        self.cards[self.order_of_stack].pop()
        self.records[self.outer]+=1
        self.order_of_stack=self.outer
        self.cards[self.order_of_stack].appendleft(self.outer)


tm=Twelvemonths()
tm.shuffle()
tm.split()  

while 1:
    if len(tm.cards[0])==4 and list(tm.cards[0])==[0,0,0,0]: # before we found all 0 cards we need find all other cards
        break
    tm.move()


flag=0
for i in range(12):
    if tm.records[i]==4:
        flag+=1
if flag==12:
    print("VICTORY")
else:
    print("FAIL")

# the possibility to win of this game is about 0.08!

'''
nums=0
for i in range(1000):
    tm=Twelvemonths()
    tm.shuffle()
    tm.split()
    while 1:
        if len(tm.cards[0])==4 and list(tm.cards[0])==[0,0,0,0]:
            break
        tm.move()
    flag=0
    for i in range(12):
        if tm.records[i]==4:
            flag+=1
    if flag==12:
        nums+=1
print(nums)
print(nums/1000)
        
'''