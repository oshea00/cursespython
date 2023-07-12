import curses
import time
from curses import wrapper
from curses.textpad import Textbox, rectangle

def mov(x,offset,maxx):
    if x == 1 and offset < 0:
        return 1
    if x >= maxx and offset > 0:
        return 1
    return x + offset

def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_GREEN,-1)
    curses.init_pair(2,curses.COLOR_RED,-1)
    GREEN_BLACK = curses.color_pair(1)|curses.A_BOLD
    RED_BLACK = curses.color_pair(2)

    x, y = 1, 1
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(y,x,"X",GREEN_BLACK)
    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            x = mov(x,-1,curses.COLS-1)
        elif key == "KEY_RIGHT":
            x = mov(x,1,curses.COLS-1)
        elif key == "KEY_UP":
            y = mov(y,-1,curses.LINES-1)
        elif key == "KEY_DOWN":
            y = mov(y,1,curses.LINES-1)
        else:
            break
        stdscr.clear()
        stdscr.border()
        rectangle(stdscr,5,5,10,10)
        stdscr.addstr(y,x,"X",GREEN_BLACK)
        stdscr.refresh()


wrapper(main)

