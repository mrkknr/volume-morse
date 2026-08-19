import win32api
import win32con
import time

# functions to make writing and reading code easier
def volup():
    # volume up
    win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
    win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)
    
def voldown():
    # volume down
    win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0)
    win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0, win32con.KEYEVENTF_KEYUP)
    
def wait(n):
    # delay between commands/other stuff
    if n=="":
        return 0
    time.sleep(n)
    
def dot():
    # dot = 0; "•"
    voldown()
    wait(0.5/speed)
    volup()
    wait(0.5/speed)
        
def dash():
    # dash = 1; "—"
    voldown()
    wait(1.5/speed)
    volup()
    wait(0.5/speed)
        
def wordspace():
    # space between words = /
    wait(3.5/speed)
    
def letterspace():
    # space between letters = s
    wait(1.5/speed)

def definenum(let):
    # determine the letter number in the alphabet
    return ord(let)-96

def code(word):
    # turn word into morse code
    lt = list(word)
    res = "morse[definenum(lt[0])]"
    for x in range(1,len(lt)):
        g = lt[x]
        res+="s"+morse[definenum(g)]
    res+="/"
    return res

def read(code):
    # play the morse code
    for x in code:
        if x == '0':
            dot()
        elif x == '1':
            dash()
        elif x == 's':
            letterspace()
        elif x == '/':
            wordspace()

# main code
morse = ["01","1000","1010","100","0","0010","110","0000","00","0111","101","0100","11","10","111","0110","1101","010","000","1","001","0001","011","1001","1011","1100"]
lang = int(input("RU or EN?\n1 for RU\n2 for EN\n> "))
if lang == 1:
    # RU
    startingtext = "\nВНИМАНИЕ!\nДля корректной работы программы требуется снизить громкость устройства до минимального значения, не равного нулю.\nГромкость должна становиться равна 0/возвращаться на минимальное значение при едином нажатии на кнопку уменьшения/увеличения громкости."
    speedtext = "\nЖелаемая скорость воспроизведения кода?\nСтандартная равна 1.\nПример: '0.5' — замедлена в 2 раза, '2' — ускорена в 2 раза.\nПри введении 0 или меньшего числа будет установлена стандартная скорость.\n> "
    ogtexttext = "\nЖелаемый текст для кодирования?\nПринимается ТОЛЬКО английский.\nВ будущем будет добавлено кодирование русского.\n> "
    timertext = "\nТребуется таймер перед запуском?\nВ случае, если да, то введите в секундах желаемое время (принимаются и целочисленные и десятичные дроби).\nВ случае, если нет (запустится сразу после выбора всех настроек), то введите 0.\n> "
    starttext = "\nВсе требующиеся настройки были выбраны.\nДля начала воспроизведения кода введите любой символ.\n> "
else:
    # EN
    startingtext = "\nATTENTION!\nFor the program to work correctly, you need to reduce the device's volume to the minimum value that is not equal to zero.\nThe volume should become 0 / return to the minimum value with a single press of the volume decrease / increase button."
    speedtext = "\nWhat is the desired playback speed of the code?\nThe standard speed is 1.\nExample: '0.5' — slowed down by 2 times, '2' — sped up by 2 times.\nIf you enter 0 or a smaller number, the standard speed will be set.\n> "
    ogtexttext = "\nDesired text for encoding?\nONLY English is accepted.\n> "
    timertext = "\nIs a timer required before starting?\nIf yes, enter the desired time in seconds (both whole numbers and decimal fractions are accepted).\nIf not (it will start immediately after all settings are selected), enter 0.\n> "
    starttext = "\nAll required settings have been selected.\nTo start playing the code, enter any character."

print(startingtext)
global speed
speed = float(input(speedtext))
if speed == "" or speed == " " or speed <= 0:
    speed = 1
ogtext = input(ogtexttext).lower()
timer = float(input(timertext))
start = input(starttext)

m = ogtext.split()
c = ''
for x in m:
    c+=code(x)
read(c)
