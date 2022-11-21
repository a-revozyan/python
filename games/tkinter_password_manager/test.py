from tkinter import *

ws = Tk()
ws.title("Python Guides")

ws.geometry("500x300")


def closewin(tp):
    tp.destroy()


def insert_val(e):
    e.insert(0, "Hello Guides!")


def popup_win():
    tp = Toplevel(ws)
    tp.geometry("500x200")

    entry1 = Entry(tp, width=20)
    entry1.pack()

    Button(tp, text="Place text", command=lambda: insert_val(entry1)).pack(pady=5, side=TOP)

    button1 = Button(tp, text="ok", command=lambda: closewin(tp))
    button1.pack(pady=5, side=TOP)


label1 = Label(ws, text="Press the Button to Open the popup dialogue", font=('Helvetica 15 bold'))
label1.pack(pady=20)

button1 = Button(ws, text="Press!", command=popup_win, font=('Helvetica 16 bold'))
button1.pack(pady=20)
ws.mainloop()