# -*- coding:utf-8 -*-
from tkinter import *


def donoting():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=donoting)

filemenu.add_command(label="Open", command=donoting)

filemenu.add_command(label="Save", command=donoting)

filemenu.add_command(label="Save as...", command=donoting)

filemenu.add_command(label="Close", command=donoting)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Undo", command=donoting)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donoting)

editmenu.add_command(label="Copy", command=donoting)

editmenu.add_command(label="Paste", command=donoting)

editmenu.add_command(label="Delete", command=donoting)

editmenu.add_command(label="Select All", command=donoting)

menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Help Index", command=donoting)

helpmenu.add_command(label="About...", command=donoting)

menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
