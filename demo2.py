import curses
import time
from curses import wrapper

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK)
    GREEN_YELLOW = curses.color_pair(1)
    CYAN_BLACK = curses.color_pair(2)
    pad = curses.newpad(100,100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67+j)
            pad.addstr(char,CYAN_BLACK)

    for i in range(50):
        pad.refresh(0,i,5,5,10,25)
        time.sleep(0.2)
    stdscr.getch()


wrapper(main)

