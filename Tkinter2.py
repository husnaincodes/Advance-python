import tkinter as tk

win = tk.Tk()
win.geometry("300x300")
tk.Label(win, text="One",font=("bold",20)).pack(pady=15)

tk.Label(win, text="Two").pack()
tk.Label(win, text="Three").pack()

win.mainloop()
