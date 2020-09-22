import sensor, image, time, math

import pyb, ustruct
import time
from pyb import Servo


#P4 -> 21
#P5->20


s1 = Servo(1) # P7
s2 = Servo(2) # P8


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_brightness(0)
sensor.set_contrast(0)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

tag_families = 0
tag_families |= image.TAG16H5

s1.pulse_width(1450)


s2.pulse_width(1200)

def family_name(tag):
    if(tag.family() == image.TAG16H5):
        return "TAG16H5"

def moveservo(servo , deg):
    if servo == 1:

        s1.pulse_width(deg)


    else:

        s2.pulse_width(deg)

while(True):
    clock.tick()
    img = sensor.snapshot()
    for tag in img.find_apriltags(families=tag_families): # defaults to TAG36H11 without "families".
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))

        print(tag.cx())
        print(tag.cy())

        if tag.cx() <60:
            s1.pulse_width(s1.pulse_width()-30)
            print("run")

        elif (tag.cx()>120):

            s1.pulse_width(s1.pulse_width()+30)

        if tag.cy() <50:
            s2.pulse_width(s2.pulse_width()+30)
            print("run")

        elif (tag.cy()>80):

            s2.pulse_width(s2.pulse_width()-30)
























