from tkinter import *
from tkinter.filedialog import *

import numpy as np
import cv2


def newFile():  # 새파일
    text_area.delete(1.0, END)


def saveFile():  # 저장
    f = asksaveasfile(mode='w', defaultextention=".jpg",
                      filetypes=[('fromfiles', '.jpg')])  # .txt 파일명으로 저장 설정
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def cartoon(img):
    
    
window = Tk()
window.title('TK Photoshop')
# window.geometry("700x400+800+300")
window.resizable(0, 0)

menu = Menu(window)
menu01 = Menu(menu, tearoff=0)
menu01.add_command(label="새파일", command=newFile)
menu01.add_command(label="저장", command=saveFile)
menu01.add_separator()  # 메뉴 안에 분리선 삽입
menu01.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu01)

# ㅅㅏㅈㅣㄴ
f = np.fromfile(r"C:\workspace\Python\Python_prj\Tkinter_Photoshop\img",np.unit8)
img = cv2.imdecode(f,cv2.IMREAD_UNCHANGED)# ㅇㅜㅓㄴㅂㅗㄴㅇㅡㄹㅗ ㅎㅗㅊㅜㄹ





window.mainloop()
