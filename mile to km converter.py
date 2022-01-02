import tkinter


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60
    calc_label.config(text=f"{km}")


window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

equal_label = tkinter.Label(text="is equal to ", font=("Arial", 10, "bold"))
equal_label.grid(column=2, row=8)

miles_label = tkinter.Label(text="Miles ", font=("Arial", 10, "bold"))
miles_label.grid(column=20, row=7)

calc_label = tkinter.Label(text="0 ", font=("Arial", 10, "bold"))
calc_label.grid(column=15, row=8)

km_label = tkinter.Label(text="Km ", font=("Arial", 10, "bold"))
km_label.grid(column=20, row=8)

miles_input = tkinter.Entry(width=8)
miles_input.grid(column=15, row=7)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=15, row=15)

window.mainloop()
