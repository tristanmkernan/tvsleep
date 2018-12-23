import platform
import subprocess


def change_computer_into_sleep_mode():
    # thanks to https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
    if platform.system() == 'Darwin':
        # thanks to http://www.uponmyshoulder.com/blog/2010/put-os-x-to-sleep-via-command-line/
        subprocess.run(['pmset', 'sleepnow'])
