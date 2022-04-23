#!/usr/bin/python
import time
import spidev as SPI
import lcdLib_1inch14
from PIL import Image,ImageDraw,ImageFont
import mercury


Font1 = ImageFont.truetype("font/Font00.ttf",20)
Font2 = ImageFont.truetype("font/Font00.ttf",16)
Font3 = ImageFont.truetype("font/Arial, Bold.ttf",22)
    

disp = lcdLib_1inch14.lcd()
disp.Init()
image2 = Image.new("RGB", (disp.width, disp.height), "WHITE")


image = Image.open('images/sb.jpg')	
disp.Display_image(image)


time.sleep(2)
disp.clear()
draw = ImageDraw.Draw(image2)

draw.text((20,5),"SMART SHOPPING", font = Font3, fill = "BLUE")
disp.Display_image(image2)

count = 30

# write your tag
lst = {"b'E200001B63130047123014B3'":"USB Fingerprint","b'121212121212121212121212'":"Micro:bit Servo Driver","b'E200001B63130047121014B7'":"Breadboard for micro:bit","b'E200001B63130047133014E7'":"Motor Driver HAT for RPi"}
lst1=[]

reader = mercury.Reader("tmr:///dev/ttyS0")
reader.set_region("EU3")
reader.set_read_plan([1], "GEN2")


while True:
        data=reader.read()
        for i in range(len(data)):
            lst1.append(lst[str(data[i])])
            lst1=list(set(lst1))
            print(lst1)
            draw.text((20,count),lst[str(data[i])], font = Font2, fill = "RED")
            disp.Display_image(image2)
            print(len(lst1))
            time.sleep(0.1)
            count +=22
        lst1.clear()
        
            




