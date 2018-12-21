"""
tvsleep.py

after the given delay, put the computer to sleep
"""

import platform
import subprocess
import time


def change_computer_into_sleep_mode():
    # thanks to https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
    if platform.system() == 'Darwin':
        # thanks to http://www.uponmyshoulder.com/blog/2010/put-os-x-to-sleep-via-command-line/
        subprocess.run(['pmset',  'sleepnow'])

def main(minutes_to_sleep, verbose=False):

    for elapsed in range(minutes_to_sleep):
        if verbose:
            print(f'Sleeping in {minutes_to_sleep - elapsed} minutes...')

        time.sleep(60) # sleep 60 seconds
    
    change_computer_into_sleep_mode()

