#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#MOVIE WHEEL
#simple program to pick a random movie from a list
#can add movies (with random years) to the list
#list saves between sessions 


#FEATURES:
# selects a movie from a list
# basic menu implementation
# a simple animation
# add movie to list 
# imports and saves movies to a .csv file automatically.


#POTENTIAL FEATURES:
#self.YEARS not all random
#display ALL movies in the list 


# In[ ]:


import os
import random
import pandas as pd 
import pygame
import pygame.freetype 

from pygame.locals import(
    K_RETURN,
    K_SPACE,
    K_BACKSPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()
pygame.mixer.init()
pygame.freetype.init()

#infoObject = pygame.display.Info()
#SCRN_W = infoObject.current_w
#SCRN_H = infoObject.current_h

SCRN_W = 800
SCRN_H = 600

MID = (SCRN_W / 2 +150 , SCRN_H /2 )
POS2 = (100 , SCRN_H /2 )
M_UP = (SCRN_W / 2 +150, SCRN_H /2-100 )
M_DOWN = (SCRN_W / 2 +150, SCRN_H /2 +100)
M_RIGHT = (SCRN_W / 2+250 , SCRN_H /2 )
M_LEFT = (SCRN_W / 2+50 , SCRN_H /2 )

M_TOPLEFT = (SCRN_W / 2+50 , SCRN_H /2-100 )
M_TOPRIGHT = (SCRN_W / 2+250 , SCRN_H /2-100)
M_BOTLEFT = (SCRN_W / 2+50 , SCRN_H /2+100 )
M_BOTRIGHT = (SCRN_W / 2+250 , SCRN_H /2+100 )



black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
yellow = (255,255,0)

red = (205,0,0)
blue = (0,0,205)

n = 3
r = 75

px25 = 25
px15 = 15


###### CLASSES & FUNCTIONS ######


class Movie(pygame.sprite.Sprite):
    def __init__(self, name, year, pick):
        super(Movie, self).__init__()
        self.name = name
        self.year = year
        self.picked = pick
        self.image = pygame.Surface((r, r))
        
        self.image.fill(white)
        self.rect = self.image.get_rect(
            center=(
                random.randint(r, SCRN_W -r),
                random.randint(r + 50, SCRN_H -r),
            )
        )

    def update(self):
        self.picked = True
        self.rect = self.image.get_rect(
            center=(
                SCRN_W / 2 + 150,
                SCRN_H / 2),
            )
        
        
        
class Option:
    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        MENU_FONT.render_to(screen, self.pos, self.text, self.get_color())
        
    def set_rend(self):
        self.rend = MENU_FONT.render(self.text, True, black) 
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend[1]
        self.rect.topleft = self.pos
    

    
def rnd_movies(n, Group):
    #defines some random movies for testing
    i  = 0
    while i < n:
        rnd_n = str(random.randint(0,5000))
        rnd_yr = random.randint(1950,2018)
        p = False
        new_mov = Movie(rnd_n,rnd_yr,p)
        Group.add(new_mov)
        i = i+1     
    return Group

def add_movie(name):
    #adds a movie to the movies Group
    rnd_yr = random.randint(1950,2018)
    temp = Movie(name,rnd_yr,False)
    movies.add(temp)
    return 


def draw(Group):
    #draws a random movie from movies and returns it.
    global options
    ls = [s for s in Group.sprites() if s.picked==False]
    print(len(ls))
    if len(ls) > 0:
        p = random.randint(1,len(ls))
        temp = ls[p-1]
        temp.update()
        selected.add(temp)
        options.append(RESET)
        return temp
    else:
        global err
        err = True
        return
    

    
def import_csv():
    #load the saved movie list
    tmp = pd.read_csv('data/movies.csv', delimiter=";")
    tmp_list = tmp.values.tolist()
    i  = 0
    while i < len(tmp_list):
        texti = tmp_list[i][0]
        yeari = tmp_list[i][1]
        pickedi = tmp_list[i][2]
        tm = Movie(texti,yeari,pickedi)
        movies.add(tm)
        i = i+1 
    return 
    

#this is broken! 
def export_csv():
    #saves the movie list
    temp = movies.sprites()
    data = []
    i = 0 
    while i < len(temp):
        tpl = (temp[i].name, temp[i].year, temp[i].picked)
        data.append(tpl)
        i = i + 1
    data_f = pd.DataFrame(data,columns=['text','year','picked'])
    data_f.to_csv('data/movies.csv', sep=";", index = False) 
    return

    
def scrawl():
    
    global err
    global running
    
    GAME_FONT.render_to(screen, (px25, 10 + (0*px15)), ">> moviewheel.program", green)
    GAME_FONT.render_to(screen, (px25, 10 + (1*px15)), ">> print(debug.txt)", green)
    GAME_FONT.render_to(screen, (px25, 10 + (2*px15)), ">> Press ESC key to quit.", green)
    GAME_FONT.render_to(screen, (px25, 10 + (3*px15)), ">> ...", green)

    if err:
        GAME_FONT.render_to(screen, (px25, 10 + (4*px15)), ">> wheel broken...", green)
        GAME_FONT.render_to(screen, (px25, 10 + (5*px15)), ">> there are no more movies to draw...", green)        
      
    elif adding:
        GAME_FONT.render_to(screen, (px25, 10 + (4*px15)), ">> adding movies...", green)
                
    else:
        if end == False:   
            GAME_FONT.render_to(screen, (px25, 10 + (4*px15)), ">> wheel ready to spin...", green)
            GAME_FONT.render_to(screen, (px25, 10 + (5*px15)), ">> Press SPACE to draw...", green)
            
        elif end == True:       
            winner = selected.sprites()[0]
            GAME_FONT.render_to(screen, (px25, 10 + (4*px15)), ">> wheel has been spun...", green)
            GAME_FONT.render_to(screen, (px25, 10 + (5*px15)), ">> selected movie is called:", green)
            GAME_FONT.render_to(screen, (px25, 10 + (6*px15)), ">> " + winner.name, green)
            GAME_FONT.render_to(screen, (px25, 10 + (7*px15)), ">> it was released in:", green)
            GAME_FONT.render_to(screen, (px25, 10 + (8*px15)), ">> " + str(winner.year), green)
            GAME_FONT.render_to(screen, (px25, 10 + (9*px15)), ">> Press ENTER to reset...", green)
          

    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()    
    
    return



def animate():
    pygame.draw.line(screen, black, M_UP, M_DOWN, 2)
    pygame.draw.line(screen, black, M_LEFT, M_RIGHT, 2)
    return    

def animate2():
    pygame.draw.line(screen, black, M_TOPLEFT, M_BOTRIGHT, 3)
    pygame.draw.line(screen, black, M_TOPRIGHT, M_BOTLEFT, 3)
    return


###### LOADING STUFF ######

pygame.display.set_caption('Movie Wheel')

#set background screen, font stuff
screen = pygame.display.set_mode((SCRN_W, SCRN_H))
clock = pygame.time.Clock()
pygame.mouse.set_visible( True )

GAME_FONT = pygame.freetype.Font('data/cour.ttf', 14)
GAME_FONT_LARGE = pygame.freetype.Font('data/cour.ttf', 24)
MENU_FONT = pygame.freetype.Font('data/freesansbold.ttf', 40)

h1 = SCRN_H - (40+px25)
h2 = SCRN_H - (80+px25)
h3 = SCRN_H - (120+px25)

LEAVE = Option("EXIT", (25, h1))
SPIN = Option("SPIN THE WHEEL", (25, h2))
RESET = Option("RESET THE WHEEL", (25, h2))
ADD = Option("ADD MOVIE", (25, h3))
CONF = Option("CONFIRM", (25, h3))
options = [LEAVE, SPIN, ADD]

################


t1 = (SCRN_W/2 - 70)
l1 = (SCRN_H/2 - 24)

input_box = pygame.Rect(t1,l1,140,48)
color_inactive = yellow
color_active = green
color = color_inactive
active = False

text = ''

###################

#checks for stuff and things
NEW_EVENT = pygame.USEREVENT + 1
SPIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(NEW_EVENT, 500)
pygame.time.set_timer(SPIN_EVENT, 750)

#sounds
menu_sound = pygame.mixer.Sound("data/menu roll.wav")
clapping = pygame.mixer.Sound("data/Well Done.ogg")

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)

channel1.set_volume(0.5)
channel2.set_volume(0.5)


#sprite groups 
movies = pygame.sprite.Group()
selected = pygame.sprite.GroupSingle()


#data import
import_csv()



###### MAIN LOOP ######

running = True
end = False
err = False
adding = False 
spin = False 


while running:
    for event in pygame.event.get():
        #keypress?
        if event.type == KEYDOWN:
            #Press esc to quit 
            if event.key == K_ESCAPE:
                export_csv()
                running = False
                
            elif adding:
                #typing information 
                if event.key == pygame.K_RETURN:
                    #enters the name 
                    if len(text) > 0:
                        channel1.play(menu_sound, loops = 0)
                        temp_name = str(text)
                        add_movie(temp_name)
                        print('movie added!' + temp_name)
                        options.remove(CONF)
                        options.append(ADD)
                        options.append(SPIN)  
                        adding = False
                        err = False
                        text = ''
                    else:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    #backspace deletes the last character
                    text = text[:-1]
                else:
                    #typing new characters
                    text += event.unicode
                
            elif event.key == K_SPACE and (len(selected) == 0) and err == False:
                #keyboard key SPACE to spin of the wheel 
                channel2.play(clapping, loops = 0)
                options.remove(SPIN)
                draw(movies)
                
            elif event.key == K_RETURN and (len(selected) == 1) and err == False:
                #keyboard key ENTER to reset of the wheel
                channel1.play(menu_sound, loops = 0)
                options.append(SPIN)
                options.remove(RESET)
                selected.empty()
                end = False
                
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            #mouse click handler
            apos = pygame.mouse.get_pos()
            if not adding:
                for b in options:
                    if b.rect.collidepoint(event.pos):
                        if b.text == "EXIT":
                            export_csv()
                            running = False
                            
                        elif b.text == "ADD MOVIE":
                            channel1.play(menu_sound, loops = 0)
                            options.remove(ADD)
                            options.append(CONF)
                            if end and not err:
                                options.remove(RESET)
                                selected.empty()
                                end = False
                            elif not end and not err:
                                options.remove(SPIN)
                            adding = True
                            
                        elif b.text == "SPIN THE WHEEL" and not end:
                            channel2.play(clapping, loops = 0)
                            options.remove(SPIN)
                            draw(movies)
                            
                        
                        elif b.text == "RESET THE WHEEL" and end:
                            channel1.play(menu_sound, loops = 0)
                            options.append(SPIN)
                            options.remove(RESET)
                            selected.empty()
                            end = False
                            
                         
            else:
                
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                
                for b in options:
                    if b.rect.collidepoint(event.pos):
                        channel1.play(menu_sound, loops = 0)
                        if b.text == "EXIT":
                            options.remove(CONF)
                            options.append(ADD)
                            if len([s for s in movies if s.picked == False]) >= 1:
                                options.append(SPIN)
                            adding = False
                            
                            print('not added')
                            
                        elif b.text == "CONFIRM":
                            if len(text) > 0:
                                temp_name = str(text)
                                add_movie(temp_name)
                                err = False
                                print('movie added!' + temp_name)
                                text = ''
                                
                            options.remove(CONF)
                            options.append(ADD)
                            if len([s for s in movies if s.picked == False]) >= 1:
                                options.append(SPIN)
                            
                            adding = False                
     
        #user clicked X on window 
        elif event.type == QUIT:  
            export_csv()
            running = False
   

        if event.type == NEW_EVENT:
            if len(selected) == 1:
                end = True
                
        elif event.type == SPIN_EVENT:
            #spinning animation needs this 
            if end == True:
                spin = not spin


        
    # Get all the keys currently pressed nad update
    pressed_keys = pygame.key.get_pressed()
    
    #fill screen            
    screen.fill(black)
    
    #text 
    scrawl()
    
    
    #display the input text box when ADDING;
    if adding:
        txt_surface, rect = GAME_FONT_LARGE.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        GAME_FONT_LARGE.render_to(screen, (input_box.x+5, input_box.y+5), text, green)
        pygame.draw.rect(screen, color, input_box, 2)
        
    if end:
        #displays the wheel spinning after selecting the movie 
        for entity in selected:
            pygame.draw.circle(screen, red, MID, r)
            if spin:
                animate()
            else:
                animate2()
                GAME_FONT_LARGE.render_to(screen, POS2, f"{entity.name}", yellow)
        

    #flip to display everything
    pygame.display.flip()

    #program set to 60 fps
    clock.tick(60)


#######################
#END PROGRAM
pygame.mixer.quit()  
pygame.quit()

#SHUTDOWN
os._exit(00)


    


# In[ ]:




