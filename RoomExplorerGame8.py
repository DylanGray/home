#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a simple text based adventure game

import colorama
from colorama import Fore, Back, Style, init
init(convert=True)

class Vdirs:
    #valid directions of travel for a room and the connecting room
    
    def __init__(self, n,e,s,w):
        #a tuple of the room codes as STRs
        self.n = n 
        self.e = e
        self.s = s 
        self.w = w 


class Room(Vdirs):
    #defined by name, code with desc for flavour
    #contains lists of npcs and items and Vdirs for movement
    
    def __init__(self, name, code, desc, Vdirs, npcs, itms):
        self.name = name
        self.code = code
        self.desc = desc
        self.Vdirs = Vdirs
        self.npcs = npcs
        self.itms = itms
        
    def del_npc(self, n):
        self.npcs.remove(n)
        
    def del_itm(self, x):
        self.itms.remove(x)
        

class Player(Room):
    #player information
    
    def __init__(self, name, current_room):
        self. name = name
        self.current_room = current_room
        self.npclist = []
        self.itmlist = []
        
    def change_room(self, a):
        if type(a) == Room:
            self.current_room = a
        else:
            print('Error: Must move to a valid Room')
            
    def add_npc(self, a):
        self.npclist.append(a)
    
    
    def add_itm(self, b):
        self.itmlist.append(b) 
    
    
#to colour text/SO    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[37m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''    
    

itm1 = 'Bucket of gold'
itm2 = 'Signet ring'
itm3 = 'Small green pants'
itm4 = 'Small buckled shoes'
itm5 = 'Potatoes'

allitms = [itm1,itm2,itm3,itm4,itm5]

npc1 = 'Passed out partier'
npc2 = 'Cowering insurance agent'
npc2a = 'An animated skeleton dancing and playing the saxophone'
npc3 = 'King Louie'
npc4 = 'Terrible Script Writer'
npc5 = 'Neil Breen'
npcBOSS = 'Warwick Davis'

allnpcs = [npc1,npc2,npc2a,npc3,npc4,npc5,npcBOSS]
alldirs = ['north','east','south','west']

st = Room('Plain Room', 'ST', 'A boring room. There is a familar pile of puke on the floor. There are doors to the north, east, south, and west.', ('S1','S3','S4','S2'), [], []
         )

s1 = Room('Dance Hall', 'S1','It is a large hall for dancing. The floor is wood. There are doors to the east, south, and west.', (0, 'C2', 'ST', 'C1'), [npc1], []
         )
s2 = Room('Dining Room','S2', 'It is a fancy dining room. There are doors to the north, east, and south.', ('C1', 'ST', 'C3', 0), [npc5], []
         )
s3 = Room('Bathroom','S3', 'It is a bathroom with a solid gold toliet. There are doors to the north and west.', ('C2', 0, 0, 'ST'), [], [itm2]
         )
s4 = Room('Chamber','S4', 'It is a small room lacking anything interesting. There are doors to the north, east, and west.', ('ST', 'E1', 0, 'C3'), [], []
         )

c1 = Room('Kitchen', 'C1' , 'It is a kitchen filled with dust. There are doors to the south and east.', (0, 'S1', 'S2', 0), [npc2a], []
         )
c2 = Room('Bedroom', 'C2', 'It is a lavish bedroom littered with old rose petals and empty whiskey bottles. There are doors to the south and west.', (0, 0, 'S3', 'S1'), [npc3], [itm3,]
         )
c3 = Room('Pantry', 'C3', 'It is a pantry for food. There is nothing except potatoes. Alot of potatoes. There are doors to the north and east.', ('S2', 'S4', 0, 0), [], [itm5]
         )

e1 = Room('Poorly Named Room', 'E1', 'It is a spooky altar room. Blood and nasty stuff is all over the place. There are doors to the east and west.', (0, 'E2', 0, 'S4'), [npc4], [itm1]
         )
e2 = Room('Hallway', 'E2', 'It is a creepy hallway covered in old movie posters. There are doors to the east and west.', (0, 'E3', 0, 'E1'), [], [itm4]
         )
e3 = Room('Leprechaun Den', 'E3', 'It is a very scary room, like where a boss would be fought. There are no exit doors!', (0,0,0,0), [npcBOSS], []
         )

allrooms = [st, s1, s2, s3, s4, c1, c2, c3, e1, e2, e3]
allroomscodes = ['ST','S1','S2','S3','S4','C1','C2','C3','E1','E2','E3']

l_npc = len(allnpcs)
l_itm = len(allitms)

intro = 'Intructions: Type the Direction (north, east, west, south) you want to move. ' + '\n'+         'Type the name of characters / items to interact with them. '+ '\n' +         'Type stop to stop the game. Report bigs and spelling mistakes at email@gmail.com'

secret = 'The Secret is a 2006 self-help book by Rhonda Byrne, based on the earlier film of the same name. ' + '\n'+          'It is based on the belief of the law of attraction, which claims that thoughts can change a person''s life directly. ' + '\n' +          'The book has sold 30 million copies worldwide and has been translated into 50 languages. '

def player_action(s, P):
    #takes a string as an input and resolves the action.
    if s in alldirs:
        tmpd = alldirs.index(s)
        if P.current_room.Vdirs[tmpd] != 0:
            print(f"{bcolors.WARNING}You move {s}...{bcolors.ENDC}")
            td = allroomscodes.index(P.current_room.Vdirs[tmpd])
            P.change_room(allrooms[td])
            return room_desc(P)
        else:
            print(f"{bcolors.WARNING}Cannot move in that direction!{bcolors.ENDC}")
        return room_desc(P)
    
    elif s in allnpcs:
        if s != npcBOSS:
            P.add_npc(s)
            P.current_room.del_npc(s)
            allnpcs.remove(s)
            print(f"{bcolors.OKBLUE}You talk with {s} and they join your adventure.{bcolors.ENDC}")
            return room_desc(P)
        else:
            P.add_npc(s)
            P.current_room.del_npc(s)
            allnpcs.remove(s)
            print(f"{bcolors.OKBLUE}You match wits with {s} for a few hours in an epic conclusion. A boss fight, if you will.{bcolors.ENDC}")
            return game_end(P)
      
    elif s in allitms:
        P.add_itm(s)
        P.current_room.del_itm(s)
        allitms.remove(s)
        print(f"{bcolors.OKBLUE}You pick up the {s} thinking it might be useful later.{bcolors.ENDC}")
        return room_desc(P)
    
    elif s == 'secret':
        print(Fore.YELLOW + Back.BLUE + 'You found a secret!')
        print(Style.RESET_ALL)
        print(Fore.YELLOW + secret)
        print(Style.RESET_ALL)
        return room_desc(P)
    
    elif s == 'stop':
        return game_end(P)
    
    else:
        print(f"{bcolors.FAIL}Command invalid!{bcolors.ENDC}")
        return room_desc(P)

def room_desc(P):
    #describes the current room the Player is in and waits for input 
    print(f"{bcolors.OKGREEN}You are in a {P.current_room.name}{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}{P.current_room.desc}{bcolors.ENDC}")
    if len(P.current_room.npcs) != 0:
        print(f"{bcolors.OKBLUE}Someone is here...{bcolors.ENDC}")
        ln = len(P.current_room.npcs)
        i = 0
        while i < ln:
            tmp = P.current_room.npcs[i]
            i = i + 1
            print(f"{bcolors.OKBLUE}        {tmp}{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}No one else is here.{bcolors.ENDC}")
        
    if len(P.current_room.itms) != 0:
        print(f"{bcolors.OKBLUE}There are items on the floor...{bcolors.ENDC}")
        lt = len(P.current_room.itms)
        k = 0
        while k  < lt:
            tmp2 = P.current_room.itms[k]
            k = k + 1
            print(f"{bcolors.OKBLUE}        {tmp2}{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}Literally nothing else is here.{bcolors.ENDC}")
        
    print(f"{bcolors.HEADER}What do you do now {P.name}?{bcolors.ENDC}")
    ac = input()
    print('')
    return player_action(ac, P)
    
def game_end(P):
    #ends the game
    print(f"{bcolors.OKGREEN}You really explorered those rooms so well and found your way out. Maybe?{bcolors.ENDC}")
    print(f"{bcolors.FAIL}You earned 100 gold to spend in shops that don't exist.{bcolors.ENDC}")
    t_npc = str(len(P.npclist))
    t_itm = str(len(P.itmlist))
    print(Fore.YELLOW + 'You met '+ t_npc +' of '+ str(l_npc) +' possible characters. You remember their distinct personalities.')   
    print('You found '+ t_itm +' of '+ str(l_itm) +' items. They were very useful.')
    print('You found X of 1 secrets....')
    print(f"{bcolors.FAIL}Thanks for playing.{bcolors.ENDC}")
    input("Press Enter to Exit Room Explorer V7")
   
    
def game_initialize():
    #starts the game  
    print(Fore.RED + 'Welcome to Room Explorer V7')
    print(f"{intro}")
    print('')
    print(Fore.CYAN + Style.BRIGHT + 'CURRENTLY CASE SENSITIVE!!!!')
    print('')
    print(Fore.RED + Style.NORMAL + 'Enter player name:')
    print(Style.RESET_ALL)
    nm = input()
    user = Player(nm, st)
    print(f"{bcolors.OKGREEN}Okay,  {user.name}! You awaken in a room after a night of something strange on the town.{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}'You are not sure where you are or how you got here.{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}Try to find the exit.{bcolors.ENDC}")
    print(Fore.CYAN + 'Type start to ''start'' ')
    print('')
    print(Style.RESET_ALL)

    stt = input()
    if stt == 'start':
        room_desc(user)
    else:
        print('Well, you messed that up.')
        print('Again CASE SENSITIVE. Type ''start'' to start!')
        tt = input()
        if tt == 'start':
            print('Okay then, here we go!')
            room_desc(user)
        else:
            print('This game may be too hard without basic typing skills....')
    

print('Game Initialized.')

game_initialize()


# In[ ]:




