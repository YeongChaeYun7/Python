import tkinter as tk

# 함수


def func(val):
    s = label.cget('text')  # cget():지정된 옵션의 값을 반환
    s += val  # s:12
    label.config(text=s)  # config():위젯 text 속성 값을 읽거나 변경


def calc():  # =
    s = label.cget('text')
    print(s)
    res = eval(s)  # eval(): 연산식을 문자열 매개변수로 받아서 실행
    label.config(text=str(res))


def clear():  # C
    label.config(text='')


window = tk.Tk()  # Tk 클래스 객체(기본 윈도우와 ui api를 제공) 생성
window.title('TK Calculator')
window.geometry('272x358+250+100')  # 창의 너비, 높이, 위치 설정
window.resizable(0, 0)  # 창 크기 고정

# 위젯 생성, 배치
label = tk.Label(window, height=4)
label.grid(row=0, column=0)  # grid(): 위젯의 배치 속성

b1 = tk.Button(text='1', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('1'))
b1.grid(row=1, column=0)

b2 = tk.Button(text='2', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('2'))
b2.grid(row=1, column=1)

b3 = tk.Button(text='3', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('3'))
b3.grid(row=1, column=2)

b4 = tk.Button(text='+', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('+'))
b4.grid(row=1, column=3)

b5 = tk.Button(text='4', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('4'))
b5.grid(row=2, column=0)

b6 = tk.Button(text='5', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('5'))
b6.grid(row=2, column=1)

b7 = tk.Button(text='6', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('6'))
b7.grid(row=2, column=2)

b8 = tk.Button(text='-', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('-'))
b8.grid(row=2, column=3)

b9 = tk.Button(text='7', width=8, height=4, relief='raised',
               bd=3, command=lambda: func('7'))
b9.grid(row=3, column=0)

b10 = tk.Button(text='8', width=8, height=4, relief='raised',
                bd=3, command=lambda: func('8'))
b10.grid(row=3, column=1)

b11 = tk.Button(text='9', width=8, height=4, relief='raised',
                bd=3, command=lambda: func('9'))
b11.grid(row=3, column=2)

b12 = tk.Button(text='x', width=8, height=4, relief='raised',
                bd=3, command=lambda: func('*'))
b12.grid(row=3, column=3)

b13 = tk.Button(text='0', width=8, height=4, relief='raised',
                bd=3, command=lambda: func('0'))
b13.grid(row=4, column=0)

b14 = tk.Button(text='C', width=8, height=4,
                relief='raised', bd=3, foreground='red', command=clear)
b14.grid(row=4, column=1)

b15 = tk.Button(text='=', width=8, height=4,
                relief='raised', bd=3, foreground='blue', command=calc)
b15.grid(row=4, column=2)

b16 = tk.Button(text='÷', width=8, height=4, relief='raised',
                bd=3, command=lambda: func('/'))
b16.grid(row=4, column=3)

window.mainloop()  # Tk클래스 객체의 mainloop() 메서드를 호출 -> ui실행
