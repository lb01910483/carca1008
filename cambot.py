# This version uses new-style automatic setup/destroy/mapping
# Need to change /etc/webiopi

# Imports
import webiopi
import sys
import os
# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Left motor GPIOs
L1=27 # H-Bridge 1
L2=22 # H-Bridge 2
L3=23 # H-Bridge 1,2EN
L4=24 
# Right motor GPIOs
R1=10 # H-Bridge 3
R2=9
R3=8
R4=7 # H-Bridge 4
 # H-Bridge 3,4EN

# -------------------------------------------------- #
# Convenient PWM Function                            #
# -------------------------------------------------- #

# Set the speed of two motors


# -------------------------------------------------- #
# Left Motor Functions                               #
# -------------------------------------------------- #

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def left_forward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)

def left_backward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)
# -------------------------------------------------- #
# Right Motor Functions                            
# -------------------------------------------------- #
def right_stop():
    GPIO.output(L3, GPIO.LOW)
    GPIO.output(L4, GPIO.LOW)
    GPIO.output(R3, GPIO.LOW)
    GPIO.output(R4, GPIO.LOW)
def right_forward():
    GPIO.output(R3, GPIO.LOW)
    GPIO.output(R4, GPIO.HIGH)
    GPIO.output(L3, GPIO.LOW)
    GPIO.output(L4, GPIO.HIGH)
def right_backward():
    GPIO.output(L3, GPIO.HIGH)
    GPIO.output(L4, GPIO.LOW)
    GPIO.output(R3, GPIO.HIGH)
    GPIO.output(R4, GPIO.LOW)
# -------------------------------------------------- #
# Macro definition part                              #
# -------------------------------------------------- #
@webiopi.macro
def go_forward():
    left_forward()
    right_forward()      

#os.system("sudo irsend SEND_ONCE /home/pi/lircd.conf KEY_POWER")#

@webiopi.macro
def go_backward():
    left_backward()
    right_backward()

@webiopi.macro
def turn_left():
    left_forward()
    right_backward()

@webiopi.macro
def turn_right():
    right_forward()
    left_backward()

@webiopi.macro
def stop():
    left_stop()
    right_stop()
@webiopi.marco
def attack_back():
    
    os.system("sudo irsend SEND_ONCE /home/pi/lircd.conf KEY_POWER")
@webiopi.marco
def attack_turn():    

    os.system("sudo irsend SEND_ONCE /home/pi/lircd.conf KEY_VOLUMEUP")
def attack_stop():    

    os.system("sudo irsend SEND_ONCE /home/pi/lircd.conf KEY_VOLUMEDOWN")   
# Called by WebIOPi at script loading
def setup():
    # Setup GPIOs

    GPIO.setFunction(L1, GPIO.OUT)
    GPIO.setFunction(L2, GPIO.OUT)
    GPIO.setFunction(L3, GPIO.OUT)
    GPIO.setFunction(L4, GPIO.OUT)    

    GPIO.setFunction(R1, GPIO.OUT)
    GPIO.setFunction(R2, GPIO.OUT)
    GPIO.setFunction(R3, GPIO.OUT)
    GPIO.setFunction(R4, GPIO.OUT)    
 
    stop()


# Called by WebIOPi at server shutdown
def destroy():
    # Reset GPIO functions
 
    GPIO.setFunction(L1, GPIO.IN)
    GPIO.setFunction(L2, GPIO.IN)
    GPIO.setFunction(L3, GPIO.IN)
    GPIO.setFunction(L4, GPIO.IN)    
 
    GPIO.setFunction(R1, GPIO.IN)
    GPIO.setFunction(R2, GPIO.IN)
    GPIO.setFunction(R3, GPIO.IN)
    GPIO.setFunction(R4, GPIO.IN)    
