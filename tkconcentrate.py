#!/Users/markbolding/anaconda3/bin/python
# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time



class App():
    def __init__(self):
        self.start_time = time.time()
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.elapsed_time = time.time() - self.start_time
        now = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()
