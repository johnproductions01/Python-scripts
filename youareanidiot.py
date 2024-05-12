from tkinter import *
import tkinter as tk
 
 
import threading
import time
import random
import sys
nb=0
seconds=random.randint(0,10)
def disable_event():
    for i in range(3):
        stop=time.sleep(seconds)
        nb=nb+1
        if nb==3:
            break
def move_window():
    root=Tk()
    root.title('TA7CHAAAA')
    root.attribute('-toolwindow',True)
    x=random.randint(0,999)
    y=random.randint(0,999)
    root.resiable(0,0)
    root.geometry(f'235x200+{x}+{y}')
    root.configure(background='green')
    
    label(root, text='TA7CHAAAA', fg='white', font=('terminal'))