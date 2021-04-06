# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 02:00:24 2021
@author: jacobo
@description: This is a simple snake game to test and learn python.
"""

# pip install windows-curses to install the package if not available
import random
import curses
import ctypes  # An included library with Python install.
import time


# Part of the funtions.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# We initializate the screen

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0) # We put the window in the center
w.keypad(1)
w.timeout(100)

# We initialise the location of the snake. We also put the food in one place.

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT
eaten=0

# And now we put here where the magic begins


try:
    start = time.time()
    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key
    
        if (snake[0][0] in [0, sh]) or (snake[0][1]  in [0, sw]) or (snake[0] in snake[1:]):
            curses.endwin()
            break
    
        new_head = [snake[0][0], snake[0][1]]
    
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
    
        snake.insert(0, new_head)
    
        if snake[0] == food:
            eaten +=1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-1),
                    random.randint(1, sw-1)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(int(tail[0]), int(tail[1]), ' ')
    
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    
    end = time.time()
    end_message='Snake has finished.\nYou ate '+str(eaten)+" pieces of food.\nYou played for "+str(round(end-start,2))+" seconds."
    Mbox('This is the end', end_message, 1)

except:
    end = time.time()
    end_message='Snake has finished.\nYou ate '+str(eaten)+" pieces of food.\nYou played for "+str(round(end-start,2))+" seconds."
    Mbox('This is the end', end_message, 1)

quit()