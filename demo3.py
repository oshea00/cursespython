import curses
import time
from curses import wrapper

def mov(x,offset,maxx):
    if x == 0 and offset < 0:
        return 0
    if x >= maxx and offset > 0:
        return 0
    return x + offset

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    GREEN_YELLOW = curses.color_pair(1)
    CYAN_BLACK = curses.color_pair(2)
    WHITE_BLACK = curses.color_pair(3)

    x, y = 0, 0
    stdscr.clear()
    stdscr.addstr(y,x,"X",CYAN_BLACK)
    stdscr.addstr(15,30,"User Arrow Keys To Move 'X'",WHITE_BLACK)
    stdscr.addstr(16,30,"'Q' to Quit",WHITE_BLACK)
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
        elif key.upper() == "Q":
            break
        stdscr.clear()
        stdscr.addstr(y,x,"X",CYAN_BLACK)
        stdscr.refresh()


wrapper(main)

