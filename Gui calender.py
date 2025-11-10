import calendar
from tkinter import *

root = Tk()
root.title("Calendar App")
root.geometry("800x600")
root.resizable(False, False)

# function to show calendar
def show_calendar():
    try:
        year = int(year_entry.get())
        cal_text = calendar.TextCalendar().formatyear(year)
        text.delete('1.0', END)
        text.insert('insert', cal_text)
    except ValueError:
        text.delete('1.0', END)
        text.insert('insert', "Please enter a valid year!")


Label(root, text="Enter Year:", font=('Arial', 12, 'bold')).pack(pady=10)


year_entry = Entry(root, width=10, justify='center', font=('Arial', 12))
year_entry.pack()


Button(root, text="Show Calendar", command=show_calendar, bg="lightblue", font=('Arial', 12, 'bold')).pack(pady=10)

text = Text(root, width=100, height=30, font=('Courier', 10))
text.pack(pady=10)

scroll = Scrollbar(root, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)

root.mainloop()
