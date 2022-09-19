from email.mime import image
import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk

window = tk.Tk()
window.geometry("800x600")
window.title("Photoshop")

#함수
def displayImage():
    pass
def Open():#불러오기
    pass
def Save():#저장
    pass
def SaveAs():#다른이름으로 저장
    pass
#종료는 함수 안빼고 코드 중간에
def ZoomIn():#이미지 확대
    pass
def zoomOut():#이미지 축소
    pass
def Flip():#상하반전
    pass
def Flop():#좌우반전
    pass
def rotate():#90도 회전
    pass
def brightness():#밝기
    pass
def clearly(): #선명하게
    pass
def gray():#흑백
    pass
def pen():#펜
    pass
def eraser():#지우개
    pass
window, canvas, peper = None, None, None#공통으로 접근할 전역변수
photo, newPhoto = None, None#원본, 이미지 처리 결과
orgX, orgY = 0, 0#원본 폭과 높이

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
mfile.add_command(label="불러오기")
mfile.add_command(label="저장하기")
mfile.add_command(label="다른이름으로 저장하기")
mfile.add_separator()
mfile.add_command(label="나가기", command=window.quit)
menubar.add_cascade(label="file", menu=mfile)

msave = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="save")

mback = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="실행취소")

mfront = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="다시실행")

window.config(menu=menubar)  # 윈도우창에 메뉴 등록

# # fToolKit inner widget
# toolkit = tk.Menu(fToolKit)

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