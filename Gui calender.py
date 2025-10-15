import calendar
from tkinter import *

# create main window
root = Tk()
root.title("Calendar App")
root.geometry("500x500")
root.resizable(False, False)

# function to show calendar
def show_calendar():
    year = int(year_entry.get())
    cal_text = calendar.TextCalendar().formatyear(year)
    text.delete('1.0', END)
    text.insert('insert', cal_text)

# label
Label(root, text="Enter Year:", font=('Arial', 12, 'bold')).pack(pady=10)

# entry box
year_entry = Entry(root, width=10, justify='center')
year_entry.pack()

# button
Button(root, text="Show Calendar", command=show_calendar, bg="lightblue").pack(pady=10)

# text box to display calendar
text = Text(root, width=150, height=100)
text.pack()

root.mainloop()
