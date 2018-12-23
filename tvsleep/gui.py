import threading
import tkinter as tk

from .util import change_computer_into_sleep_mode

config = {}


class Application(tk.Frame):
    def __init__(self, minutes_to_sleep, master=None):
        # initialize parent class
        super().__init__(master)

        # basic frame initialization
        self.master = master
        self.pack()

        # initialize thread to null
        self.thread = None
        self.stop_thread_event = None

        # define, create and initialize the layout/ui

        # title
        self.title = tk.Label(self, text='TV Sleep')
        self.title.pack(side='top')

        # 'go to sleep after...' label, input, bound variable and button
        self.sleep_after_frame = tk.Frame(self)

        self.sleep_after_label = tk.Label(self.sleep_after_frame, text='Sleep After:')
        self.sleep_after_label.pack(side='left')

        self.sleep_after_var = tk.IntVar(value=minutes_to_sleep)
        self.sleep_after = tk.Entry(self.sleep_after_frame,
                                    textvariable=self.sleep_after_var,
                                    width=5)
        self.sleep_after.pack(side='left')

        self.start_stop = tk.Button(self.sleep_after_frame,
                                    text='Start',
                                    command=self.start_stop_callback)
        self.start_stop.pack(side='left')

        self.sleep_after_frame.pack()

        # status labels
        self.status_frame = tk.Frame(self)

        self.status_label = tk.Label(self, text='Status:')
        self.status_label.pack(side='left')

        self.status = tk.Label(self, text='Idle', bg='grey')
        self.status.pack(side='left', fill=tk.X, expand=True)

        self.status_frame.pack(fill=tk.X)

        # start the initial timer
        self.start_loop()

    def start_stop_callback(self):
        if self.thread:
            self.stop_loop()
        else:
            self.start_loop()

    def thread_logic(self):
        minutes_to_sleep = self.sleep_after_var.get()

        elapsed = 0
        stop_event = self.stop_thread_event

        self.status['text'] = f'Sleeping in {minutes_to_sleep} mins...'

        while not stop_event.wait(1):
            elapsed += 1

            if elapsed > minutes_to_sleep * 60:
                self.status['text'] = 'Putting computer to sleep...'
                change_computer_into_sleep_mode()
                return

            remaining = (minutes_to_sleep * 60 - elapsed)

            if remaining > 60:
                self.status['text'] = f'Sleeping in {remaining // 60} mins...'
            else:
                self.status['text'] = f'Sleeping in {remaining} seconds...'

    def start_loop(self):
        self.start_stop['text'] = 'Reset'
        self.sleep_after['state'] = 'disabled'

        self.stop_thread_event = threading.Event()
        self.thread = threading.Thread(target=self.thread_logic)
        self.thread.start()

    def stop_loop(self):
        self.start_stop['text'] = 'Start'
        self.sleep_after['state'] = 'normal'
        self.status['text'] = 'Idle'

        self.stop_thread_event.set()
        self.stop_thread_event = None
        self.thread = None


def main_gui_loop(minutes_to_sleep, verbose=False):
    config['verbose'] = verbose

    root = tk.Tk()
    root.geometry('300x80')
    app = Application(minutes_to_sleep, master=root)
    app.master.title('TV Sleep')
    app.mainloop()


if __name__ == '__main__':
    main_gui_loop(42)
