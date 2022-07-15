import tkinter as tk
from tokenize import Double

print("hello")


def calculate(work_hours, entries, label : tk.StringVar):
    if not isinstance(work_hours, dict):
        return
    if not isinstance(entries, dict):
        return
    income = 0
    print("test")
    for entry in entries:
        if not entries[entry].get():
           continue 
        print( entries[entry].get())
        income += work_hours[entry]*float(entries[entry].get())

    skatt = 0.67
    label.set(str(int(income * skatt)))

window = tk.Tk()


work_hours = {
    "month": 23400,
    "night": 65,
    "evening": 43.63,
    "overtime": 42.97, 
    "day_weekend": 93.63, 
    "night_weekend": 110.14 
}

greeting = tk.Label(text="heloo, work")

money = tk.StringVar() 
i = 0
entries = {}
for shift in work_hours:
    label = tk.Label(window, text = shift).grid(row = i)
    entry = tk.Entry(window)
    entry.grid(row = i, column = 1)
    entries[shift] = entry
    i += 1
    if shift == "night_weekend":
        total_income_label = tk.Label(window, textvariable = money).grid(row = i)
        tk.Button(window, text = "quit", command=window.quit).grid(row=i,column=1)
        tk.Button(window, text = "calculate", command= lambda: calculate(work_hours, entries, money)).grid(row=i,column=2)

window.mainloop()