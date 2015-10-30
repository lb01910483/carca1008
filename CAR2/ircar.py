# This version uses new-style automatic setup/destroy/mapping
# Need to change /etc/webiopi

# Imports
#!/usr/bin/python
import RPi.GPIO as GPIO

import lirc
import time
sockid = lirc.init("myprogram")
# Retrieve GPIO lib
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #


# Left motor GPIOs
L1=10 # H-Bridge 1
L2=9 # H-Bridge 2
L3=23 # H-Bridge 1,2EN
L4=24 
# Right motor GPIOs
R1=8 # H-Bridge 3
R2=7
R3=13
R4=19# H-Bridge 4

GPIO.setup(R1,GPIO.OUT)
GPIO.setup(R2,GPIO.OUT)
GPIO.setup(R3,GPIO.OUT)
GPIO.setup(R4,GPIO.OUT)
GPIO.setup(L1,GPIO.OUT)
GPIO.setup(L2,GPIO.OUT)
GPIO.setup(L3,GPIO.OUT)
GPIO.setup(L4,GPIO.OUT)

while True:
    print("IR singal")
    code = lirc.nextcode()
    print (code)
    if code == ["KEY_POWER"]:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(R1,GPIO.OUT)
        GPIO.setup(R2,GPIO.OUT)
        GPIO.setup(R3,GPIO.OUT)
        GPIO.setup(R4,GPIO.OUT) 
        GPIO.setup(L1,GPIO.OUT)
        GPIO.setup(L2,GPIO.OUT)
        GPIO.setup(L3,GPIO.OUT)
        GPIO.setup(L4,GPIO.OUT)
        GPIO.output(L1, False)
        GPIO.output(L2, True)
        GPIO.output(R1, False)
        GPIO.output(R2, True)
        GPIO.output(L3, False)
        GPIO.output(L4, True)
        GPIO.output(R3, True)
        GPIO.output(R4, False)
        time.sleep(2)
        GPIO.output(R1,False)
        GPIO.output(R2,False)
        GPIO.output(R3,False)
        GPIO.output(R4,False)
        GPIO.output(L1,False)
        GPIO.output(L2,False)
        GPIO.output(L3,False)
        GPIO.output(L4,False)

    elif code == ["KEY_VOLUMEUP"]:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(R1,GPIO.OUT)
        GPIO.setup(R2,GPIO.OUT)
        GPIO.setup(R3,GPIO.OUT)
        GPIO.setup(R4,GPIO.OUT) 
        GPIO.setup(L1,GPIO.OUT)
        GPIO.setup(L2,GPIO.OUT)
        GPIO.setup(L3,GPIO.OUT)
        GPIO.setup(L4,GPIO.OUT)
        GPIO.output(L1, False)
        GPIO.output(L2, True)
        GPIO.output(R1, True)
        GPIO.output(R2, False)
        GPIO.output(L3, False)
        GPIO.output(L4, True)
        GPIO.output(R3, False)
        GPIO.output(R4, True)
        time.sleep(2)
        GPIO.output(R1,False)
        GPIO.output(R2,False)
        GPIO.output(R3,False)
        GPIO.output(R4,False)
        GPIO.output(L1,False)
        GPIO.output(L2,False)
        GPIO.output(L3,False)
        GPIO.output(L4,False)

    elif code == ["KEY_1"]:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(R1,GPIO.OUT)
        GPIO.setup(R2,GPIO.OUT)
        GPIO.setup(R3,GPIO.OUT)
        GPIO.setup(R4,GPIO.OUT) 
        GPIO.setup(L1,GPIO.OUT)
        GPIO.setup(L2,GPIO.OUT)
        GPIO.setup(L3,GPIO.OUT)
        GPIO.setup(L4,GPIO.OUT)
        GPIO.output(L1, False)
        GPIO.output(L2, False)
        GPIO.output(R1, False)
        GPIO.output(R2, False)
        GPIO.output(L3, False)
        GPIO.output(L4, False)
        GPIO.output(R3, False)
        GPIO.output(R4, False)
        time.sleep(2)
        GPIO.output(R1,False)
        GPIO.output(R2,False)
        GPIO.output(R3,False)
        GPIO.output(R4,False)
        GPIO.output(L1,False)
        GPIO.output(L2,False)
        GPIO.output(L3,False)
        GPIO.output(L4,False)


 
        
