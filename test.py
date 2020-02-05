import pyautogui as pgui
import time

# 현재 모니터 크기 확인
width, height = pgui.size()
print("{},{}".format(width, height))

# 현재 마우스 위치 확인
mx, my = pgui.position()
print("{},{}".format(mx, my))

# 좌표가 모니터 안에 위치해 있는지 확인
print(pgui.onScreen(3242, 1233))
print(pgui.onScreen(0, 0))

# 마우스 컨트롤 (절대이동)
# None = 움직이지 않음
pgui.moveTo(x=0, y=0, duration=0)

# 마우스 컨트롤 (상대이동)
pgui.move(xOffset=110, yOffset=110, duration=3)

# 마우스 드래그 (절대이동)
# button = 마우스 버튼(left ,right, middle)
pgui.dragTo(123, 123, button='left')

# 마우스 드래그 (상대이동)
pgui.drag(110, 110, button='left')

# 마우스 클릭
pgui.click(x=200, y=200, button='left', clicks=2, interval=1)

# 마우스 버튼 누르고 떼기
pgui.mouseDown(x=100, y=100, button='right')
pgui.mouseUp()

# 마우스 스크롤하기
pgui.scroll(50)
pgui.scroll(-50)
pgui.scroll(10, x=200, y=300)

# 텍스트 입력
pgui.typewrite("hello world")
pgui.typewrite(['a', 'b', 'x', 'y'])

# ex1
def ex1():
    time.sleep(1)
    pgui.click()
    distance = 200
    while distance > 0:
        pgui.dragRel(distance, 0, duration=0.2)
        distance = distance - 10
        pgui.dragRel(0, distance, duration=0.2)
        pgui.dragRel(distance, 0, duration=0.2)
        distance = distance - 10
        pgui.dragRel(0, distance, duration=0.2)

# ex1() # for test


# 키 누르기
# left는 왼쪽 화살표


# ex2
import webbrowser


def ex2():
    webbrowser.open('http://autbor.com/form')
    time.sleep(5)
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.typewrite("이름")
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.typewrite("Name")
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.typewrite("Greatest Fear")
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.hotkey('down')
    time.sleep(1)
    pgui.hotkey('enter')
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.hotkey('space')
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.typewrite("sdjakdjakshkjsdh")
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.hotkey('enter')

ex2()
