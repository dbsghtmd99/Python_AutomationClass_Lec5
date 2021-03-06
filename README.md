# Python_AutomationClass_Lec5

다섯 번째 수업에서는 사용자의 직접적인 입력 없이 마우스와 키보드를 제어하는 방법에 대해서 학습했다.

코드 원본 파일은 [https://github.com/dbsghtmd99/Python_AutomationClass_Lec5](https://github.com/dbsghtmd99/Python_AutomationClass_Lec5) 에서 확인 가능하다.

## 1. 라이브러리 설명

## 2. 수업 떄 다루었던 내용

1. 현재 모니터 해상도 확인
   
```python
width, height = pgui.size()
print("{},{}".format(width, height))
```

2. 현재 마우스 위치 확인
   
```python
mx, my = pgui.position()
print("{},{}".format(mx, my))
```

3. 좌표가 모니터 안에 위치해 있는지 확인
   
```python
print(pgui.onScreen(3242, 1233))
print(pgui.onScreen(0, 0))
```

4. 마우스 컨트롤 (절대이동)
   
```python
# None = 움직이지 않음
pgui.moveTo(x=0, y=0, duration=0)
```

5. 마우스 컨트롤 (상대이동)
   
```python
pgui.move(xOffset=110, yOffset=110, duration=3)
```

6. 마우스 드래그 (절대이동)
   
```python
# button = 마우스 버튼(left ,right, middle)
pgui.dragTo(123, 123, button='left')
```

7. 마우스 드래그 (상대이동)
   
```python
pgui.drag(110, 110, button='left')
```

8. 마우스 클릭
```python
pgui.click(x=200, y=200, button='left', clicks=2, interval=1)
```

9. 마우스 버튼 누르고 떼기
    
```python
pgui.mouseDown(x=100, y=100, button='right')
pgui.mouseUp()
```

10.  마우스 스크롤하기
    
```python
pgui.scroll(50)
pgui.scroll(-50)
pgui.scroll(10, x=200, y=300)
```

11. 텍스트 입력
```python
pgui.typewrite("hello world")
pgui.typewrite(['a', 'b', 'x', 'y'])
```

## 3. 연습문제
```python
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
```

```python
# ex2
import webbrowser

def ex2():
    # time.sleep() 을 이용하여 delay를 주었다.
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

# ex2() # for test
```