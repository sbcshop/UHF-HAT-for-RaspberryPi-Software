#!/usr/bin/python
import time
import spidev as SPI
import lcdLib_1inch14
from PIL import Image,ImageDraw,ImageFont
import mercury

Font1 = ImageFont.truetype("font/Font00.ttf",20)
Font2 = ImageFont.truetype("font/Font00.ttf",16)
Font3 = ImageFont.truetype("font/Font02.ttf",25)
    

disp = lcdLib_1inch14.lcd()
disp.Init()
image2 = Image.new("RGB", (disp.width, disp.height), "WHITE")


image = Image.open('pic/sb.jpg')	
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

while True:
    data=reader.read()
    if(data):
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

        
    
 
