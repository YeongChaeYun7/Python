# 미니 프토샵 프로그램 만들기
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
# 이미지 처리 기능을 제공하는 Pillow 라이브러리를 import 함
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# 전역변수 선언 및 초기화
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0


def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 화면 크기 설정
    window.geometry(str(width)+'x'+str(height))
    # print(str(width)+", "+str(height))
    # 기존에 canvas 에 출력한 그림이 있다면
    if canvas != None:
        canvas.destroy()    # canvas를 깨끗하게 만든다.

    # canvas 생성
    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    # 이미지의 폭을 절반의 값과 높이의 절반의 값의 위치에 이미지를 생성한다.
    canvas.create_image((width/2, height/2), image=paper)

    rgbString = ''
    rgbImage = img.convert("RGB")
    cnt = 0
    # 높이와 너비만큼 더블루프 돌면서 rgb 값을 getpixel() 로 추출하여 16진수 형태로 rgbString 에 누적시키고 있다.
    for i in range(0, height):
        tmpString = ""
        for j in range(0, width):
            # 복사된 이미지 객체에 getpixel() 를 이용하여 rgb값을 얻어낼 수 있다.
            r, g, b = rgbImage.getpixel((j, i))
            # x 값 뒤에 한 칸을 공백으로 두어야한다.
            tmpString += "#%02x%02x%02x " % (r, g, b)
            cnt += 1
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백(중요)
    # print(rgbString, "cnt: ",cnt)
    # rgb 문자열 값을 paper 에 대입시키면서 papar 에 이미지를 출력시키고 있다.
    paper.put(rgbString)
    canvas.pack()

# 파일 열기


def func_open():
    # photo 는 원본 이미지 저장할 변수, photo2 는 이미지 처리후 나타나는 결과 이미지를 저장할 변수,
    # oriX, oriY 원본 이미지의 폭과 높이를 저장할 변수
    global window, canvas, paper, photo, photo2, oriX, oriY
    # 파일다이얼로그(열기)를 통하여 원하는 이미지를 사용자가 선택할 수 있도록 한다.
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;"
                                                        "*.tif;*.gif"), ("모든 파일", "*.*")))

    # 파이썬에서 제공하는 PhotoImage() 가 아닌 Pillow 라이브러리에서 제공하는 Image.open() 함수를 사용하도록 한다.
    # 파이썬에서 제공하는 PhotoImage()0 클래스는 이미지 파일의 확장자가 .gif, .png 만 지원하므로 한계가 있다.
    # 사용자가 선택한 이미지를 읽고 RGB 모드로 변환시키고 있다.
    photo = Image.open(readFp).convert("RGB")
    # 원본 이미지의 너비와 높이를 저장하고 있다.
    oriX = photo.width
    oriY = photo.height
    # 원본 이미지를 photo2 변수에 복사하여 대입한다.
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    print(newX, ", ", newY)  # 복사된 이미지의 높이와 너비값을 출력해봄
    # 복사한 내용을 가지고 displayImage() 함수를 호출하고 있다.
    displayImage(photo2, newX, newY)

# 파일 저장


def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY
    # photo2 가 None 이라는 것은 복사된 이미지 객체가 없다...라면
    if photo is None:
        return  # return 을 이용하여 함수를 종료시킨다.
    # 파일 다이얼로그(저장)을 띄어서 사용자로부터 파일명을 입력받고 저장하는 방식 여기서는 이미지 파이리을 저장할 때
    # 기본값으로 .jpg 파일로 저장하게끔 하였다.
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.jpg',
                           filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든파일", "*.*")))
    # 사용자가 입력한 파일명으로 저장
    photo2.save(saveFp.name)


# 프로그램 종료
def func_exit():
    exit()

# 이미지 확대하기


def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대 배수", '확대할 배수를 입력해주세요.', minvalue=2, maxvalue=10)
    photo2 = photo.copy()
    # Pillow  라이브러리에서 제공하는 resize()  함수는 간단하게 이미지를 확대 및 축소를 할 수가 있다.
    # 하지만, 확대할 배수가 너무 크다면 메모리나 속도적인 측면에서 시간이 오래 걸릴 수 있다는 것이 문제점이다.
    # photo2에 이미지 사이즈를 변경하여 변경된 이미지 객체를 photo2에 대입하고 있다.
    photo2 = photo2.resize((int(oriX * scale), int(oriY * scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 이미지 축소 하기
def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소 배수", '축소할 배수를 입력해주세요.', minvalue=2, maxvalue=10)
    photo2 = photo.copy()
    # Pillow  라이브러리에서 제공하는 resize()  함수는 간단하게 이미지를 확대 및 축소를 할 수가 있다.
    # 하지만, 확대할 배수가 너무 크다면 메모리나 속도적인 측면에서 시간이 오래 걸릴 수 있다는 것이 문제점이다.
    # photo2에 이미지 사이즈를 변경하여 변경된 이미지 객체를 photo2에 대입하고 있다.
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 상하반전


def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    # 이미지를 상하로 반전할 때는 transpose(Image.FLIP_TOP_BOTTOM)를 사용하면 쉽다.
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 좌우반전


def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    # 이미지를 좌우로 반전할 때는 transpose(Image.FLIP_LEFT_RIGHT)를 사용하면 쉽다.
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 회전


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전 기능", "회전할 각도를 입력하세요.", minvalue=0, maxvalue=360)
    photo2 = photo.copy()
    # 이미지를 회전할 때는 rotate()를 사용하낟. 매개변수값으로 각도와 expand 값으로 설정하는데 여기서
    # expand 값을 True로 설정하면 회전결과 이미지를 확대하고, False를 설정하면 원본 크기를 그대로 유지한다
    photo2 = photo2.rotate(degree, expand=True)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지를 밝게 하는 기능


def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("밝게", "값을 입력하세요(1.0~16.0)", minvalue=1.0, maxvalue=16.0)
    photo2 = photo.copy()
    # 이미지를 밝게, 어둡게 처리 하고자 한다면 ImageEnhance.Brightness(이미지).enhance(밝기값)함수를 사용하면된다.
    # 밝기값은 1.0이면 원본 이미지의 밝기값이다. 1.0이 초과되면 이미지를 밝게 처리하고, 1.0미만이면 이미지를 어둡게 처리한.
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 이미지를 어둡게 하는 기능
def func_dark():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("어둡게", "값을 입력하세요(0.0~1.0)", minvalue=0.0, maxvalue=1.0)
    photo2 = photo.copy()
    # 이미지를 밝게, 어둡게 처리 하고자 한다면 ImageEnhance.Brightness(이미지).enhance(밝기값)함수를 사용하면된다.
    # 밝기값은 1.0이면 원본 이미지의 밝기값이다. 1.0이 초과되면 이미지를 밝게 처리하고, 1.0미만이면 이미지를 어둡게 처리한.
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 이미지를 블러링 하는 기능
def func_blur():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    # 이미지에 특수효과를 주려면 fitler(ImageFilter.필터)함수를 사용하면 된다.
    # 블러링은 BLUR 필터를 사용하고 엠보싱은 EMBOSS 필터를 사용하면 된다. 이외에도 CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE
    # FIND_EDGES, SHARPEN, SMOOTH 등의 특수효과들이 존재한다.
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지를 엠보싱 하는 기능


def func_embo():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    # 이미지에 특수효과를 주려면 fitler(ImageFilter.필터)함수를 사용하면 된다.
    # 블러링은 BLUR 필터를 사용하고 엠보싱은 EMBOSS 필터를 사용하면 된다. 이외에도 CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE
    # FIND_EDGES, SHARPEN, SMOOTH 등의 특수효과들이 존재한다.
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 이미지를 흑백으로 하는 기능
def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    # 컬러이미지를 흑백이미지로 변경하려면 ImageOps.grayscale(이미지) 함수를 사용하면 된다.

    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

    # 미니포토샵 프로그램에서 사용한 Pillow 라이브러리 모듈은 이 외에도 상당히 많은 고급 뮤들과 기능을 제공한다.
    # 이것을 잘 이용하면 상용포토삽과 아주 유사하게 이미지 처리하는 기술을 파이썬에서 구현할 수 있다


# 메인코드 부분
if __name__ == '__main__':
    window = Tk()  # 윈도우 생성
    window.geometry("250x250")  # 윈도우 크기 설정
    window.title("미니포토샵")

    mainMenu = Menu(window)  # 메뉴바를 생성
    window.config(menu=mainMenu)  # 윈도우의 메뉴를 mainMenu 로 설정

    # tearoff 속성은 메뉴의 점선을 없애준다.
    fileMenu = Menu(mainMenu, tearoff=False)
    # add_cascade() 함수는 상위메뉴와 하위메뉴를 연결해준다.(상위 메뉴=mainMenu)
    # 다른 메뉴가 확장이 되어야 되기 때문에 add_cascade() 를 사용하여 메뉴의 이름을
    # 파일로 설정하였고, menu속성값을 fileMenu 로 지정한 것이다.
    mainMenu.add_cascade(label='파일', menu=fileMenu)
    # add_command() 는 메뉴 항목을 생성해준다.
    # 파일 열기 메뉴아이템을 클릭했을 때 func_open() 가 호출이 된다.
    fileMenu.add_command(label='파일 열기', command=func_open)
    fileMenu.add_command(label='파일 저장', command=func_save)
    # 구분선 추가하기
    fileMenu.add_separator()
    fileMenu.add_command(label='종료', command=func_exit)

    image1Menu = Menu(mainMenu, tearoff=False)
    mainMenu.add_cascade(label='이미지 처리(1)', menu=image1Menu)
    image1Menu.add_command(label='확대', command=func_zoomin)
    image1Menu.add_command(label='축소', command=func_zoomout)
    image1Menu.add_separator()
    image1Menu.add_command(label='상하 반전', command=func_mirror1)
    image1Menu.add_command(label='좌우 반전', command=func_mirror2)
    image1Menu.add_command(label='회전', command=func_rotate)

    image2Menu = Menu(mainMenu, tearoff=False)
    mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
    image2Menu.add_command(label='밝게', command=func_bright)
    image2Menu.add_command(label='어둡게', command=func_dark)
    image2Menu.add_separator()
    image2Menu.add_command(label='블러링', command=func_blur)
    image2Menu.add_command(label='엠보싱', command=func_embo)
    image2Menu.add_separator()
    image2Menu.add_command(label='흑백', command=func_bw)

    window.mainloop()
