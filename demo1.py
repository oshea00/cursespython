import curses
import time
from curses import wrapper

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_CYAN,curses.COLOR_BLACK)
    GREEN_YELLOW = curses.color_pair(1)
    CYAN_BLACK = curses.color_pair(2)
    counter_win = curses.newwin(1,20,10,10)
    stdscr.addstr("Hello World")
    stdscr.refresh()
    for i in range(100):
        counter_win.clear()
        color = CYAN_BLACK
        if i % 2 == 0:
            color = GREEN_YELLOW
        counter_win.addstr(f"Count: {i}",color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()


wrapper(main)

