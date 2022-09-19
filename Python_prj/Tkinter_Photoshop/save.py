from numpy import newaxis
from email.mime import image

import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk

window = tk.Tk()
window.geometry("800x600")
window.title("Photoshop")

# 함수


def displayImage():
    pass


def Open():  # 불러오기
    pass


def Save():  # 저장
    pass


def SaveAs():  # 다른이름으로 저장
    pass
# 종료는 함수 안빼고 코드 중간에


def ZoomInOut():  # 이미지 확대 축소
    global window, canvas, paper, photo, newPhoto, orgX, orgY
    scale = askfloat('확대/축소', '배율 입력(0.1~4.0)', minvalue=0.1, maxvalue=4.0)
    newPhoto = photo.copy()
    newPhoto.resize(int(orgX*scale), int(orgY*scale))
    newX = newPhoto.width
    newY = newPhoto.height
    displayImage(newPhoto, newX, newY)


def Flip():  # 상하반전
    global window, canvas, paper, photo, newPhoto, orgX, orgY
    newPhoto = photo.copy()
    newPhoto.flip()
    newX = newPhoto.width
    newY = newPhoto.height
    displayImage(newPhoto, newX, newY)


def Flop():  # 좌우반전
    global window, canvas, paper, photo, newPhoto, orgX, orgY
    newPhoto = photo.copy()
    newPhoto.flop()
    newX = newPhoto.width
    newY = newPhoto.height
    displayImage(newPhoto, newX, newY)


def rotate():  # 90도 회전
    global window, canvas, paper, photo, newPhoto, orgX, orgY
    newPhoto = photo.copy()
    newPhoto.rotate(90)
    newX = newPhoto.width
    newY = newPhoto.height
    displayImage(newPhoto, newX, newY)


def brightness():  # 밝기
    pass


def clearly():  # 선명하게
    pass


def gray():  # 흑백

    pass


def pen():  # 펜
    pass


def eraser():  # 지우개
    pass


window, canvas, peper = None, None, None  # 공통으로 접근할 전역변수
photo, newPhoto = None, None  # 원본, 이미지 처리 결과
orgX, orgY = 0, 0  # 원본 폭과 높이

# 구조
mainMenu = tk.Frame(window)
mainMenu.pack(expand=True, fill="both")
window.config(menu=mainMenu)

photo = PhotoImage()  # ??????????????????????
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)
# ToolKit = tk.Frame(window, bg='violet')
# ToolKit.pack(expand=True, fill="both")

# fTable = tk.Frame(window, bd=5, bg='skyblue', relief='sunken')
# fTable.pack(expand=True, fill="both")

# fFooter = tk.Frame(window, bg='yellowgreen')
# fFooter.pack(expand=True, fill="both")

fMenu = tk.Menu(mainMenu)

mainMenu.add_cascade(label='파일', menu=fMenu)  # 중복?
mfile = tk.Menu(fMenu, tearoff=0)
mfile.add_separator()
mfile.add_command(label="불러오기", command=Open)
mfile.add_command(label="저장하기", command=Save)
mfile.add_separator()
mfile.add_command(label="다른이름으로 저장하기", command=SaveAs)
mfile.add_command(label="종료", command=window.quit)
fMenu.add_cascade(label="file", menu=mfile)

iMenu = tk.Menu(mainMenu)

mainMenu.add_cascade(label='이미지', menu=iMenu)
mimage = tk.Menu(iMenu, tearoff=0)
mimage.add_command(label="확대/축소", command=ZoomInOut)
mimage.add_command(label="90도 회전", command=rotate)
mimage.add_command(label="상하 반전", command=Flip)
mimage.add_command(label="좌우 반전", command=Flop)
mimage.add_command(label="밝기", command=brightness)
mimage.add_command(label="흑백", command=gray)
mimage.add_command(label="선명하게", command=clearly)
iMenu.add_cascade(label="file", menu=mimage)

nMenu = tk.Menu(mainMenu)

mainMenu.add_cascade(label='삽입?', menu=nMenu)
mnote.add_command(label="펜", command=pen)
mnote.add_command(label="지우개", command=eraser)
nMenu.add_cascade(label="file", menu=mnote)

# msave = tk.Menu(mainMenu, tearoff=0)
# mainMenu.add_cascade(label="save")

# mback = tk.Menu(mainMenu, tearoff=0)
# mainMenu.add_cascade(label="실행취소")

# mfront = tk.Menu(mainMenu, tearoff=0)
# mainMenu.add_cascade(label="다시실행")

window.config(menu=mainMenu)  # 윈도우창에 메뉴 등록

window.mainloop()
