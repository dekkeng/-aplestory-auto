import os, pyautogui
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
import random

#pyautogui.PAUSE=0

load_dotenv("config.txt")

class Player:
    def __init__(self):        
        self.WALK_MAX_DURATION = float(os.getenv('WALK_MAX_DURATION', 2))
        self.MIN_POTION_INTERVAL = float(os.getenv('MIN_POTION_INTERVAL', 30))
        self.MAX_POTION_INTERVAL = float(os.getenv('MAX_POTION_INTERVAL', 50))
        self.SKILL_KEY_1 = os.getenv('SKILL_KEY_1', 'a')
        self.SKILL_KEY_2 = os.getenv('SKILL_KEY_2', 's')
        self.SKILL_KEY_3 = os.getenv('SKILL_KEY_3', 'd')
        self.SKILL_KEY_4 = os.getenv('SKILL_KEY_4', 'f')
        self.POTION_KEY_1 = os.getenv('POTION_KEY_1', 'q')
        self.POTION_KEY_2 = os.getenv('POTION_KEY_2', 'w')
        self.updatePos()

    def updatePos(self):
        return False
    
    def checkClick(self, type):        
        pos = self.getPos(type)
        if pos != None:
            #self.key('1')
            self.click(pos)
            self.move([10,10])
            return True
        else:  
            return False
        
    def autoAttack(self):        
        for i in range(random.uniform(self.MIN_POTION_INTERVAL, self.MAX_POTION_INTERVAL)):
            self.wait(random.uniform(0,3))
            self.walk()
            self.atk()
        self.potion()

    def getPos(self, file, conf = 0.9):
        return pyautogui.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf, grayscale=True)

    def getAllPos(self, file, conf = 0.7):
        return pyautogui.locateAllOnScreen('./sample/'+file+'.png', confidence = conf, grayscale=True)

    def wait(self, length = 0.01):
        sleep(length)
    def move(self, pos):
        pyautogui.moveTo(pos, duration=0.01)
        
    def key(self, key):
        pyautogui.keyDown(key)
        self.wait(random.uniform(0,self.WALK_MAX_DURATION))
        pyautogui.keyUp(key)

    def key(self, key):
        pyautogui.keyDown(key)
        self.wait(random.uniform(0,self.WALK_MAX_DURATION))
        pyautogui.keyUp(key)
        
    def walk(self):
        if self.WALK_MAX_DURATION > 0:
            dir = random.choice(['left', 'right'])
            self.key(dir)
    def atk(self):
        dir = random.choice([self.SKILL_KEY_1, self.SKILL_KEY_2, self.SKILL_KEY_3, self.SKILL_KEY_4])
        self.key(dir)
    def potion(self):
        dir = random.choice([self.POTION_KEY_1, self.POTION_KEY_2])
        self.key(dir)

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
