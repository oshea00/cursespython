import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK)
    GREEN_YELLOW = curses.color_pair(1)
    CYAN_BLACK = curses.color_pair(2)
    for i in range(100):
        stdscr.clear()
        color = CYAN_BLACK
        if i % 2 == 0:
            color = GREEN_YELLOW
        stdscr.addstr(f"Count: {i}",color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)

