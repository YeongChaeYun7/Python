import tkinter as tk

window = tk.Tk()
window.title("toolkit")
window.geometry("640x400+100+100")
window.resizable(True, True)


# frame
f1 = tk.Frame(window, bg='gray')
f1.pack(expand=True, fill="both")

fToolKit = tk.Frame(window, bg='violet')
fToolKit.pack(expand=True, fill="both")

# PanedWindow
toolkit = tk.PanedWindow(fToolKit, relief="raised", bd=2)  # 메인 틀
toolkit.pack(expand=True, fill='both')

mimage = tk.Menu(toolkit, tearoff=0, text="이미지")
mimage.add_command(label="이미지 자르기")
mimage.add_separator()
mimage.add_command(label="우측 회전")
mimage.add_separator()
mimage.add_command(label="상하 대칭")
mimage.add_separator()
mimage.add_command(label="좌우 대칭")

left = tk.Label(toolkit, text="이미지 (좌측)")
toolkit.add(mimage)


# toolkit.add_cascade(label="Image", menu=mimage)
# center = tkinter.PanedWindow(
#     toolkit, orient="vertical", relief="groove", bd=3)
# toolkit.add(center)

# right = tkinter.Label(toolkit, text="도구 (우측)")
# toolkit.add(right)

# top = tkinter.Label(center, text="내부윈도우 (가운데 - 상단)")
# center.add(top)

# bottom = tkinter.Label(center, text="내부윈도우 (가운데 - 하단)")
# center.add(bottom)

window.mainloop()
