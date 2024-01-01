import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
PIRpin=12
GPIO.setup(PIRpin,GPIO.IN)
import LCD1602
import KPLIB
from time import sleep
import threading
myPad=KPLIB.keypad(retChar='D')
LCD1602.init(0x27,1)
myString=''
pwd='1234'

from pygame import mixer
mixer.init()
mixer.music.load('al1.mp3')

def readKP():
    global myString
    while myString != '*':
        myString=myPad.readKeypad()
        sleep(.5)
readThread=threading.Thread(target=readKP,)
readThread.daemon=True
readThread.start()
while myString != '*':
    CMD=myString
    if CMD=='A'+pwd:
        LCD1602.write(0,0,'Armed          ')
        moveVal=GPIO.input(PIRpin)
        if moveVal==1:
            LCD1602.write(0,1,'Intruder Alert')
            mixer.music.play()
            sleep(10)
        if moveVal==0:
            LCD1602.write(0,1,'All Clear      ')
    if CMD=='B'+pwd:
        LCD1602.write(0,0,'UnArmed        ')
        LCD1602.write(0,1,'               ')
    if CMD=='C'+pwd:
        LCD1602.write(0,0,'Password?      ')
        LCD1602.write(0,1,'               ')
        while myString=='C'+pwd:
            pass
        pwd=myString
        LCD1602.write(0,0,pwd+'         ')
        sleep(2)
        LCD1602.write(0,0,'               ')
        LCD1602.clear()
    if CMD=='CA1'+pwd:
        myString='A'+pwd
        mixer.music.load('al1.mp3')
    if CMD=='CA2'+pwd:
        myString='A'+pwd
        mixer.music.load('al2.mp3')
    if CMD=='CA3'+pwd:
        myString='A'+pwd
        mixer.music.load('al3.wav')
    if CMD=='CA4'+pwd:
        myString='A'+pwd
        mixer.music.load('al4.wav')
    if CMD=='CA5'+pwd:
        myString='A'+pwd
        mixer.music.load('al5.mp3')
sleep(1)
GPIO.cleanup()
LCD1602.clear()
print('GPIO Good to Go')