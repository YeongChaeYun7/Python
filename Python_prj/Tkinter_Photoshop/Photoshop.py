import tkinter as tk
from tkinter import *


def donoting():
    filewin = Toplevel(window)
    button = Button(filewin, text="Do nothing button")
    button.pack()


window = tk.Tk()
window.geometry("800x600")
window.title("Photoshop")

# frame
fMenu = tk.Frame(window, bg='gray')
fMenu.pack(expand=True, fill="both")

fToolKit = tk.Frame(window, bg='violet')
fToolKit.pack(expand=True, fill="both")

fTable = tk.Frame(window, bd=5, bg='skyblue', relief='sunken')
fTable.pack(expand=True, fill="both")

fFooter = tk.Frame(window, bg='yellowgreen')
fFooter.pack(expand=True, fill="both")

# fMenu inner widget

menubar = tk.Menu(fMenu)

mfile = tk.Menu(menubar, tearoff=0)
mfile.add_command(label="Open", command=donoting)
mfile.add_separator()
mfile.add_command(label="Save", command=donoting)
mfile.add_separator()
mfile.add_command(label="Save as. . .", command=donoting)
mfile.add_separator()
mfile.add_command(label="Close", command=window.quit)
menubar.add_cascade(label="file", menu=mfile)

msave = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="save")

mback = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="실행취소")

mfront = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="다시실행")

window.config(menu=menubar)  # 윈도우창에 메뉴 등록

# # fToolKit inner widget
toolkit = tk.PanedWindow(fToolKit, relief="raised", bd=2)  # 메인 틀
toolkit.pack(expand=True, fill='both')  # sticky='n'

left = tk.Label(toolkit, text="이미지 (좌측)")
toolkit.add(left)

center = tk.PanedWindow(
    toolkit, orient="vertical", relief="groove", bd=3)
toolkit.add(center)

right = tk.Label(toolkit, text="도구 (우측)")
toolkit.add(right)

top = tk.Label(center, text="내부윈도우 (가운데 - 상단)")
center.add(top)

bottom = tk.Label(center, text="내부윈도우 (가운데 - 하단)")
center.add(bottom)

# toolkit = tk.Menu(fToolKit)
toolkit = tk.PanedWindow(fToolKit, relief="raised", bd=2)  # 메인 틀
toolkit.pack(expand=True, fill='both')  # sticky='n'

left = tk.Label(toolkit, text="필터")
toolkit.add(left)

left = tk.Label(toolkit, text="이미지")
toolkit.add(left)

center = tk.PanedWindow(
    toolkit, orient="vertical", relief="groove", bd=3)
toolkit.add(center)

right = tk.Label(toolkit, text="도구 (우측)")
toolkit.add(right)

top = tk.Label(center, text="내부윈도우 (가운데 - 상단)")
center.add(top)

bottom = tk.Label(center, text="내부윈도우 (가운데 - 하단)")
center.add(bottom)
# mimage = tk.Menu(toolkit, tearoff=0)
# mimage.add_command(label="이미지 자르기")
# mimage.add_separator()
# mimage.add_command(label="우측 회전")
# mimage.add_separator()
# mimage.add_command(label="상하 대칭")
# mimage.add_separator()
# mimage.add_command(label="좌우 대칭")

# toolkit.add_cascade(label="Image", menu=mimage)

# mfilter = tk.Menu(toolkit, tearoff=0)
# mfilter.add_command(label="RGB->흑백화")
# mfilter.add_separator()
# mfilter.add_command(label="명도")
# mfilter.add_separator()
# mfilter.add_command(label="대비")
# mfilter.add_separator()
# toolkit.add_cascade(label="Filter", menu=mfilter)

# mtool = tk.Menu(toolkit, tearoff=0)
# mtool.add_command(label="그리기")
# mtool.add_separator()
# mtool.add_command(label="지우개")
# mtool.add_separator()
# mtool.add_command(label="글상자")
# mtool.add_separator()
# mtool.add_command(label="크기")
# mtool.add_separator()
# toolkit.add_cascade(label="Tool", menu=mtool)

# mcolor = tk.Menu(toolkit, tearoff=0)
# mcolor.add_command(label="tor")
# mcolor.add_separator()
# toolkit.add_cascade(label="Color", menu=mcolor)

# window.config(menu=toolkit)

# fTable inner widget
label = tk.Label(fTable, text='Table')
label.pack()

button1 = tk.Button(fTable, text='Button1')
button1.pack(padx=10, pady=10)
# fFooter inner widget

window.mainloop()
