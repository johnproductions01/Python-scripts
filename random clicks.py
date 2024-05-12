import random, pyautogui as fun
for i in range(20):
    h = random.randint(0, 1080)
    w = random.randint(0,1920)
    fun.click(h,w,duration = 0.3)
    fun.hotkey('winleft', 'm')