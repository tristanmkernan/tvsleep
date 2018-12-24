"""
tvsleep.py

after the given delay, put the computer to sleep
"""

import time

from .util import change_computer_into_sleep_mode


def main(minutes_to_sleep, verbose=False, gui=False):
    if gui:
        from .gui import main_gui_loop

        main_gui_loop(minutes_to_sleep)
    else:
        for elapsed in range(minutes_to_sleep):
            if verbose:
                print(f'Sleeping in {minutes_to_sleep - elapsed} minutes...')

            time.sleep(60)  # sleep 60 seconds

        change_computer_into_sleep_mode()
