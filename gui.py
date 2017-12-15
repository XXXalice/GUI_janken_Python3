from tkinter import *
import janken as jk
root = Tk()
root.title("janken")

label = Label(text="choose your hand")
label.pack()

r_button = Button(
    text="rock",
    width=10,
    command=lambda:jk.janken(0)
)
p_button = Button(
    text="paper",
    width=10,
    command=lambda:jk.janken(1)
)
s_button = Button(
    text="scissors",
    width=10,
    command=lambda:jk.janken(2)
)
r_button.pack()
p_button.pack()
s_button.pack()

root.mainloop()