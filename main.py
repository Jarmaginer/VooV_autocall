from time import sleep
import pyautogui
import pyperclip
import pyautogui
import pyscreeze
import cv2


absentlist=[]
namelist = ["学生1","学生2","学生3"]
target= cv2.imread(r"target.png",cv2.IMREAD_GRAYSCALE)
target2= cv2.imread(r"target2.png",cv2.IMREAD_GRAYSCALE)




def checkname(name):
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.5)
    result = checkonline()

    if result == "OK":
        result = checkoffline()

    pyautogui.hotkey('ctrl', 'a')
    return result

def checkonline():
    screenScale=1

    #事先读取按钮截图
#    target= cv2.imread(r"zhengnengliang.png",cv2.IMREAD_GRAYSCALE)
    # 先截图
    screenshot=pyscreeze.screenshot('screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'screenshot.png',cv2.IMREAD_GRAYSCALE)

    tempheight, tempwidth = temp.shape[:2]
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp=cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if(max_val>=0.9):
#        print("yes")
        return "未到"
 
    else:
#        print("未找到")

        return "OK"

def checkoffline():
    screenScale=1
    temp = cv2.imread(r'screenshot.png',cv2.IMREAD_GRAYSCALE)

    tempheight, tempwidth = temp.shape[:2]
    scaleTemp=cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    res = cv2.matchTemplate(scaleTemp, target2, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if(max_val>=0.9):
        return "到了"
 
    else:

        return "识别失败"



sleep(2)

for name in namelist:
    a = checkname(name)
    if a == "到了":
        print(name,"到了")
    elif a == "未到":
        print(name,"未到")
        absentlist.append(name)
    else:
        print(name,a)
        namelist.append(name)

print(absentlist)

