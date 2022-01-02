import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

# ways to change the text in my_label.
my_label["text"] = "New text"
# or
my_label.config(text="New text")


# new_label = tkinter.Label(text="Ouch!", font=("Arial", 25, "bold"))
# new_label.pack()


# create a Button

def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=2, column=2)
button2 = tkinter.Button(text="Click Me 2", command=button_clicked)
button2.grid(row=0, column=3)

# Entry component , like an input ...
input = tkinter.Entry(width=10)
input.grid(row=5, column=5)

# def scale_used(value):
#     print(value)
#
#
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Button 1", value=1, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2 = tkinter.Radiobutton(text="Button 2", value=2, variable=radio_state, command=radio_used)
# radiobutton2.pack()

window.mainloop()
