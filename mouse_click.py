#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#先下载pyautogui库，pip install pyautogui
import os,time
import pyautogui as pag

pag.FAILSAFE=False
pag.FailSafeException=False

try:
    #print ("Press Ctrl-C to end")
    pag.click()
    x,y = pag.position() #返回鼠标的坐标
    posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
    print (posStr) #打印坐标
    pag.tripleClick()
    pag.hotkey('f8')
    #print ("click")
    #os.system('cls')#清楚屏幕
except  KeyboardInterrupt:
    pass
    #print ('end....')
