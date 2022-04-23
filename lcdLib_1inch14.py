
import time
#import lcdconfig
import sys
import time
import spidev
import numpy as np


    
class lcd_configuration:
    def __init__(self,spi=spidev.SpiDev(0,0),spi_freq=40000000,rst = 27,dc = 25,bl = 18,bl_freq=1000,i2c=None,i2c_freq=100000):
        import RPi.GPIO      
        self.np=np
        self.RST_PIN= rst
        self.DC_PIN = dc
        self.BL_PIN = bl
        self.SPEED  =spi_freq
        self.BL_freq=bl_freq
        self.GPIO = RPi.GPIO
        
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.GPIO.setup(self.RST_PIN,   self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN,    self.GPIO.OUT)
        self.GPIO.setup(self.BL_PIN,    self.GPIO.OUT)
        self.GPIO.output(self.BL_PIN,   self.GPIO.HIGH)
        
        self.SPI = spi
        if self.SPI!=None :
            self.SPI.max_speed_hz = spi_freq
            self.SPI.mode = 0b00

    def digital_write(self, pin, value):
        self.GPIO.output(pin, value)

    def digital_read(self, pin):
        return self.GPIO.input(pin)

    def spi_writebyte(self, data):
        if self.SPI!=None :
            self.SPI.writebytes(data)

    def delay_ms(self, delaytime):
        time.sleep(delaytime / 1000.0)


    def bl_DutyCycle(self, duty):
        self._pwm.ChangeDutyCycle(duty)
        
    def bl_Frequency(self,freq):
        self._pwm.ChangeFrequency(freq)
           
    def module_init(self):
        self.GPIO.setup(self.RST_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.BL_PIN, self.GPIO.OUT)
        self._pwm=self.GPIO.PWM(self.BL_PIN,self.BL_freq)
        self._pwm.start(100)
        if self.SPI!=None :
            self.SPI.max_speed_hz = self.SPEED        
            self.SPI.mode = 0b00     
        return 0

    def device_exit(self):
        if self.SPI!=None :
            self.SPI.close()
        
        self.GPIO.output(self.RST_PIN, 1)
        self.GPIO.output(self.DC_PIN, 0)        
        self._pwm.stop()
        time.sleep(0.001)
        self.GPIO.output(self.BL_PIN, 1)
        
class lcd(lcd_configuration):
    # lcd resolution
    width = 240
    height = 135
    def command(self, cmd):
        self.digital_write(self.DC_PIN, self.GPIO.LOW)
        self.spi_writebyte([cmd])	
        
    def data(self, val):
        self.digital_write(self.DC_PIN, self.GPIO.HIGH)
        self.spi_writebyte([val])	
        
    def reset(self):
        """Reset the display"""
        self.GPIO.output(self.RST_PIN,self.GPIO.HIGH)
        time.sleep(0.01)
        self.GPIO.output(self.RST_PIN,self.GPIO.LOW)
        time.sleep(0.01)
        self.GPIO.output(self.RST_PIN,self.GPIO.HIGH)
        time.sleep(0.01)
        
    def Init(self):
        """Initialize dispaly"""  
        self.module_init()
        self.reset()

        self.command(0x36)
        self.data(0x70)                
        self.command(0x3A) 
        self.data(0x05)

        self.command(0xB2)
        self.data(0x0C)
        self.data(0x0C)
        self.data(0x00)
        self.data(0x33)
        self.data(0x33)

        self.command(0xB7)
        self.data(0x35) 

        self.command(0xBB)
        self.data(0x19)

        self.command(0xC0)
        self.data(0x2C)

        self.command(0xC2)
        self.data(0x01)

        self.command(0xC3)
        self.data(0x12)   

        self.command(0xC4)
        self.data(0x20)

        self.command(0xC6)
        self.data(0x0F) 

        self.command(0xD0)
        self.data(0xA4)
        self.data(0xA1)

        self.command(0xE0)
        self.data(0xD0)
        self.data(0x04)
        self.data(0x0D)
        self.data(0x11)
        self.data(0x13)
        self.data(0x2B)
        self.data(0x3F)
        self.data(0x54)
        self.data(0x4C)
        self.data(0x18)
        self.data(0x0D)
        self.data(0x0B)
        self.data(0x1F)
        self.data(0x23)

        self.command(0xE1)
        self.data(0xD0)
        self.data(0x04)
        self.data(0x0C)
        self.data(0x11)
        self.data(0x13)
        self.data(0x2C)
        self.data(0x3F)
        self.data(0x44)
        self.data(0x51)
        self.data(0x2F)
        self.data(0x1F)
        self.data(0x1F)
        self.data(0x20)
        self.data(0x23)
        
        self.command(0x21)

        self.command(0x11)

        self.command(0x29)
  
    def SetWindows(self, Xstart, Ystart, Xend, Yend):
        #set the X coordinates
        self.command(0x2A)
        self.data((Xstart+40)>>8& 0xff)             
        self.data((Xstart+40)   & 0xff)      
        self.data((Xend-1+40)>>8& 0xff)       
        self.data((Xend-1+40)   & 0xff) 
        
        #set the Y coordinates
        self.command(0x2B)
        self.data((Ystart+53)>>8& 0xff)
        self.data((Ystart+53)   & 0xff)
        self.data((Yend-1+53)>>8& 0xff)
        self.data((Yend-1+53)   & 0xff)

        self.command(0x2C) 
        
    def Display_image(self,Image):
        """Set buffer to value of Python Imaging Library image."""
        """Write display buffer to physical display"""
                
        imwidth, imheight = Image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))
        img = self.np.asarray(Image)
        pix = self.np.zeros((self.height,self.width,2), dtype = self.np.uint8)
        
        pix[...,[0]] = self.np.add(self.np.bitwise_and(img[...,[0]],0xF8),self.np.right_shift(img[...,[1]],5))
        pix[...,[1]] = self.np.add(self.np.bitwise_and(self.np.left_shift(img[...,[1]],3),0xE0),self.np.right_shift(img[...,[2]],3))
        
        pix = pix.flatten().tolist()
        self.SetWindows ( 0, 0, self.width, self.height)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range(0,len(pix),4096):
            self.spi_writebyte(pix[i:i+4096])		
            
    def clear(self):
        """Clear contents of image buffer"""
        _buffer = [0xff]*(self.width * self.height * 2)
        self.SetWindows ( 0, 0, self.width, self.height)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range(0,len(_buffer),4096):
            self.spi_writebyte(_buffer[i:i+4096])	        
        

