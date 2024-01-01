# Building Motion Detection Alarm System with Raspberry Pi
For Alarm system two library is needed, which are:
. LCD1602 (Library for 12C connection of the LCD1602 to the raspberry pi). the file is safe as LCD1602.py.
. KPLIB (Library for reading a 16 button keypad on the raspberry pi). the fie is safe as KPLIB.py.


# Components
# Keypads
    Keypad Setup
    . The keypad has eight leads which represents row and colums.
      The first four leads are: Row 0,1,2,3 and the remaining four leads are: Column 0,1,2,3.
    
    # How to hook up keypad pins(lead) to Raspberry pi:
    . Starting from row 0 i.e the leftmost pin from the keypad pin to pin 11, 13, 15, 29, 31, 33, 35, 37.

# LCD
    LCD Setup
    . Turning LCD upside down, the let pin is the ground(GND). Ground goes to   ground on rspberry pi, pin 14 can be used on the raspberry pi.
    . The next pin on the LCD is VCC which is 5 volts , pin 4 or pin 2 can be used on the raspberry pi.

# PIR sensor
    PIR Setup
    . Turning the sensor upside down the leftmost is the VCC which needs to go to 5 volts pin on the raspberry pi. Pin 2 or 4 can be used.
    . The centre pin is the signal pin, that will be pinned to the first convenient GPIO pin. pin 12 on the raspberry pi can be used.
    . The right most is the ground(GND), goes to ground(GND) on rapberry pi. 
# Motion_Detection_Alarm_system
Motion detection alarm system using raspberry pi and PIR sensor.
