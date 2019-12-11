import pygame as py
import sys
import pygame.gfxdraw as draw
import random
import pygame.font as f
import msvcrt as mv
import time

def draw_man(i):
    if i==1:
        draw.vline(scr,500,350,450,(255,255,255))
    elif i==2:
        draw.aacircle(scr,500,320,20,(255,255,255))
    elif i==3:
        draw.hline(scr,490,450,380,(255,255,255))
    elif i==4:
        draw.hline(scr,510,550,380,(255,255,255))
    elif i==5:
        draw.line(scr,490,450,460,500,(255,255,255))
    elif i==6:
        draw.line(scr,510,450,540,500,(255,255,255))
    py.display.update()
    return

def main():
    char=0
    mancount=0
    count=0
    font=f.SysFont("Cooper Black",30)
    text=font.render("Hangman", True,(0,0,255))
    t=font.render(fact,True,(255,0,0))
    p=font.render('enter your guess',True,(255,255,0))
    gameover=font.render('Sorry game over! :( ',True,(255,255,0))
    gamewon=font.render('Correct guess, Hurray! :) ',True,(255,255,0))
    for i in list_word:
        if i is not ' ':
            blanks.append("_")
            char += 1
    update_choice()
    while not False:
        for event in py.event.get():
            if event.type == py.QUIT:
                return
            elif event.type == py.KEYDOWN:
                mancount,count = get_char(event,mancount,count)
        if mancount == 6:
            scr.blit(gameover,(150,450))
            py.display.flip()
            return
        if count == len(word):
            scr.blit(gamewon,(150,450))
            py.display.flip()
            return
        scr.blit(text,(220,20))
        scr.blit(t,(80,150))
        scr.blit(p,(80,250))
        py.display.flip()

def get_char(event,mancount,count):
    
    if event.key == py.K_a:
        user_character='a'
    elif event.key == py.K_b:
        user_character='b'
    elif event.key == py.K_c:
        user_character='c'
    elif event.key == py.K_d:
        user_character='d'
    elif event.key == py.K_e:
        user_character='e'
    elif event.key == py.K_f:
        user_character='f'
    elif event.key == py.K_g:
        user_character='g'
    elif event.key == py.K_h:
        user_character='h'
    elif event.key == py.K_i:
        user_character='i'
    elif event.key == py.K_j:
        user_character='j'
    elif event.key == py.K_k:
        user_character='k'
    elif event.key == py.K_l:
        user_character='l'
    elif event.key == py.K_m:
        user_character='m'
    elif event.key == py.K_n:
        user_character='n'
    elif event.key == py.K_o:
        user_character='o'
    elif event.key == py.K_p:
        user_character='p'
    elif event.key == py.K_q:
        user_character='q'
    elif event.key == py.K_r:
        user_character='r'
    elif event.key == py.K_s:
        user_character='s'
    elif event.key == py.K_t:
        user_character='t'
    elif event.key == py.K_u:
        user_character='u'
    elif event.key == py.K_v:
        user_character='v'
    elif event.key == py.K_w:
        user_character='w'
    elif event.key == py.K_x:
        user_character='x'
    elif event.key == py.K_y:
        user_character='y'
    elif event.key == py.K_z:
        user_character='z'
    else:
        return mancount
    if user_character not in blanks and user_character in list_word:
        count = find_duplicate(list_word,user_character,blanks,count)
    else:
        mancount=mancount+1
        draw_man(mancount)
    update_choice()
    return mancount,count

def update_choice():
    x=80
    font=f.SysFont("Cooper Black",20)
    for i in blanks:
        text=font.render(i,True,(0,0,255))
        scr.blit(text,(x,200))
        x=x+10
        text=font.render('   ',True,(0,0,255))
        scr.blit(text,(x,200))
        x=x+10
    return
 
def find_duplicate(list_word,user_character,blanks,count):
    dup_list=[]
    for x,char in enumerate(list_word):
        if char is user_character:
            if x not in dup_list:
                dup_list.append(x)
                blanks[x]=user_character
                count=count+1
    return count


blanks=[]
word_list=["india","china","antartica","australia"]
clue_fact=["has the highest cricket ground in the world","has the largest population","is the largest desert in the world","kangroo is the national animal"]
index=random.randint(0,3)
word=word_list[index]
fact=clue_fact[index]
list_word=list(word)
py.init()
scr=py.display.set_mode((900,600))
main()
time.sleep(1)
py.quit()


