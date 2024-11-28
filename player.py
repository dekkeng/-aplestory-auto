import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
import random
import subprocess 
import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
E = 0x12
S = 0x1F
D = 0x20
Z = 0x2C
UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD
ENTER = 0x1C 

PUL = ctypes.POINTER(ctypes.c_ulong)

#pyautogui.PAUSE=0

load_dotenv("config.txt")

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class Player:
    def __init__(self):       
        #subprocess.Popen("osk", stdout= subprocess.PIPE, shell=True) 
        self.WALK_MAX_DURATION = float(os.getenv('WALK_MAX_DURATION', 2))
        self.MIN_POTION_INTERVAL = int(os.getenv('MIN_POTION_INTERVAL', 30))
        self.MAX_POTION_INTERVAL = int(os.getenv('MAX_POTION_INTERVAL', 50))
   
    def autoAttack(self):
        #count = 1
        #amount = random.uniform(self.MIN_POTION_INTERVAL,self.MAX_POTION_INTERVAL)
        while(True):
            #count = count+1
            self.walk()
            self.wait(random.uniform(0,1))
            self.atk()
            #if count > amount:
                #self.potion()
                #count = 1
                #amount = random.uniform(self.MIN_POTION_INTERVAL,self.MAX_POTION_INTERVAL)

    def getPos(self, file, conf = 0.9):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf, grayscale=True)

    def getAllPos(self, file, conf = 0.7):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf, grayscale=True)

    def wait(self, length = 0.01):
        sleep(length)
    def move(self, pos):
        pyautogui.moveTo(pos, duration=0.01)
        
    def key(self, key):        
        self.pressKey(key)
        self.wait(random.uniform(0,self.WALK_MAX_DURATION))
        self.releaseKey(key)
        #pyautogui.keyDown(key)
        #self.wait(random.uniform(0,self.WALK_MAX_DURATION))
        #pyautogui.keyUp(key)
        
    def walk(self):
        if self.WALK_MAX_DURATION > 0:
            self.log('walk')
            key = random.choice([LEFT, RIGHT])
            self.key(key)
    def atk(self):        
        self.log('Attack')
        key = random.choice([A])
        self.key(key)
    def potion(self):
        self.click(self.POTION_KEY_1)


    def drag(self, pos1, pos2):
        pyautogui.mouseDown(pos1, duration=0.01)
        pyautogui.dragTo(pos2, duration=0.2)
        pyautogui.mouseUp(pos2, duration=0.01)
        
    def click(self, pos):
        self.move(pos)
        pyautogui.click([pos[0], pos[1]])
        
    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')

    def pressKey(self, hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def releaseKey(self, hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, 
    ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

