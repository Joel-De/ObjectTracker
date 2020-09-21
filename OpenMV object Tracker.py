import sensor, image, time, math

import pyb, ustruct
import time
from pyb import Servo


#P4 -> 21
#P5->20


s1 = Servo(1) # P7



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

def family_name(tag):
    if(tag.family() == image.TAG16H5):
        return "TAG16H5"

while(True):
    clock.tick()
    img = sensor.snapshot()
    for tag in img.find_apriltags(families=tag_families): # defaults to TAG36H11 without "families".
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))

        if(tag.cx()>90):

            s1.pulse_width(s1.pulse_width()+40)
            time.sleep(10)
        if(tag.cx()<70):
            s1.pulse_width(s1.pulse_width()-40)
            time.sleep(10)



















