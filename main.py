import tkinter as tk
from salary import Salary

print("hello")

salary = Salary()

def calculate(work_hours, entries, label : tk.StringVar):
    if not isinstance(work_hours, dict):
        return
    if not isinstance(entries, dict):
        return
    total_income = 0
    print("test")
    for entry in entries:
        if not entries[entry].get():
           continue 
        print( entries[entry].get())
        #total_income += work_hours[entry]*int(entries[entry].get())

    label = str(total_income)

print (salary.base_income)

window = tk.Tk()

work_hours = {
    "night": 60,
    "evening": 40,
    "overtime": 40, 
    "day_weekend": 80, 
    "night_weekend": 100 
}

greeting = tk.Label(text="heloo, work")

money = 0
i = 0
entries = {}
for shift in work_hours:
    cost = "0"
    label = tk.Label(window, text = shift).grid(row = i)
    entry = tk.Entry(window, textvariable=cost)
    entry.grid(row = i, column = 1)
    entries[shift] = entry
    i += 1
    if shift == "night_weekend":
        total_income_label = tk.Label(window, textvariable = money).grid(row = i)
        tk.Button(window, text = "quit", command=window.quit).grid(row=i,column=1)
        tk.Button(window, text = "calculate", command=calculate(work_hours, entries, money)).grid(row=i,column=1)

#greeting.pack()
window.mainloop()