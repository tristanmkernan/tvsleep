import tkinter as tk

from .util import change_computer_into_sleep_mode


class Timer(object):
    def __init__(self, minutes_to_sleep):
        self.length = minutes_to_sleep * 60
        self.remaining = self.length
        self.terminated = False

    def tick(self, delta):
        self.remaining -= delta

    @property
    def done(self):
        return self.remaining <= 0


class Application(tk.Frame):
    def __init__(self, minutes_to_sleep, master=None):
        # initialize parent class
        super().__init__(master)

        # basic frame initialization
        self.master = master
        self.pack()

        # initialize timer to null
        self.timer = None

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

        self.status = tk.Label(self, text='Idle', bg='grey', width=24)
        self.status.pack(side='left', fill=tk.X, expand=True)

        self.status_frame.pack(fill=tk.X)

        # start the initial timer
        self.start_loop()

        # start the interval which manages the timer
        self.after(1000, self.update_timer)

    def update_timer(self):
        if self.timer:
            self.timer.tick(1)

            if self.timer.done:
                if not self.timer.terminated:
                    self.status['text'] = 'Putting computer to sleep...'

                    change_computer_into_sleep_mode()

                    # prevent an infinite loop
                    self.timer.terminated = True
            else:
                if self.timer.remaining > 60:
                    self.status['text'] = f'Sleeping in {self.timer.remaining // 60} mins...'
                else:
                    self.status['text'] = f'Sleeping in {self.timer.remaining} seconds...'

        self.after(1000, self.update_timer)

    def start_stop_callback(self):
        if self.timer:
            self.stop_loop()
        else:
            self.start_loop()

    def start_loop(self):
        self.start_stop['text'] = 'Reset'
        self.sleep_after['state'] = 'disabled'

        minutes_to_sleep = self.sleep_after_var.get()
        self.status['text'] = f'Sleeping in {minutes_to_sleep} mins...'

        self.timer = Timer(minutes_to_sleep)

    def stop_loop(self):
        self.start_stop['text'] = 'Start'
        self.sleep_after['state'] = 'normal'
        self.status['text'] = 'Idle'

        self.timer = None


def main_gui_loop(minutes_to_sleep):
    root = tk.Tk()
    root.geometry('300x80')
    app = Application(minutes_to_sleep, master=root)
    app.master.title('TV Sleep')
    app.mainloop()
