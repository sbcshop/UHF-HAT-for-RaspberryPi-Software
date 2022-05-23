#!/usr/bin/python
import spidev as SPI
import lcdLib_1inch14
from PIL import Image,ImageDraw,ImageFont
import mercury

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buzzer = 17
GPIO.setup(buzzer,GPIO.OUT)



Font1 = ImageFont.truetype("font/Font00.ttf",20)
Font2 = ImageFont.truetype("font/Font00.ttf",16)
Font3 = ImageFont.truetype("font/Font02.ttf",25)
    

disp = lcdLib_1inch14.lcd()
disp.Init()
image2 = Image.new("RGB", (disp.width, disp.height), "WHITE")


image = Image.open('images/sb.jpg')	
disp.Display_image(image)


time.sleep(2)
disp.clear()
draw = ImageDraw.Draw(image2)

draw.text((50,5),"SCAN THE CARDS", font = Font2, fill = "BLUE")
disp.Display_image(image2)

count = 30

reader = mercury.Reader("tmr:///dev/ttyS0")
reader.set_region("EU3")
reader.set_read_plan([1], "GEN2")

try:
    while True:
        data=reader.read()
        if(data):
            GPIO.output(buzzer,GPIO.HIGH)
            b = data
            s = str(b)[1:-1]
            x = s.split("(")
            x = x[1].split(")")
            x = x[0]
            x = str(x)[1:-1]
            x = x.lstrip('\'')
            print(x)
            
            draw.text((10,count),x, font = Font2, fill = "RED")
            disp.Display_image(image2)

            time.sleep(0.2)
            
            count += 22
        else:
            GPIO.output(buzzer,GPIO.LOW)
finally:
    GPIO.cleanup()

        
    
 
