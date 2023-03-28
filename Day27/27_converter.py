from tkinter import *


def button_clicked():
    input_num = int(entry.get())
    result_text = str(round(1.60934 * input_num, 1))
    result_label.config(text=result_text)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

equal_to_label = Label(text="is equal to ", font=("Arial", 16, "normal"))
equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles ", font=("Arial", 14, "normal"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km ", font=("Arial", 14, "normal"))
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=("Arial", 14, "normal"))
result_label.grid(column=1, row=1)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Calculate Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
