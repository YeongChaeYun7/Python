from tkinter import *
from tkinter.filedialog import *


def newFile():  # 새파일. 텍스트창을 지우는 기능
    text_area.delete(1.0, END)


def saveFile():  # 저장
    f = asksaveasfile(mode='w', defaultextention=".txt",
                      filetypes=[('Text files', '.txt')])  # .txt 파일명으로 저장 설정
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()


window = Tk()
window.title('NotePad')
window.geometry("400x400+800+300")
window.resizable(0, 0)

menu = Menu(window)
menu01 = Menu(menu, tearoff=0)
menu01.add_command(label="새파일", command=newFile)
menu01.add_command(label="저장", command=saveFile)
menu01.add_separator()  # 메뉴 안에 분리선 삽입
menu01.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu01)

# 텍스트를 입력받을 수 있는 창 추가
text_area = Text(window)
window.grid_rowconfigure(0, weight=1)  # 좌, 우 공백 설정
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N+E+S+W)  # 텍스트 입력 창 배치

window.config(menu=menu)

window.mainloop()
