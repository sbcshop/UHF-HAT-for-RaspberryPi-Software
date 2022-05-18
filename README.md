# UHF-HAT-for-RaspberryPi

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img0.png" />

### UHF HAT for Raspberry Pi is an advanced and compact "Ultra High Frequency" RFID reader that consists of powerful RFID technology designing for a broad range of applications in the defense, healthcare system, banks, offices etc. 
### UHF HAT for Raspberry Pi has an onboard  ThingMagic® M6E Nano UHF RFID Reader that is JADAK’s smallest embeddable module with ultra-low power consumption and tiny form factor.  This RFID reader is ideal for battery operated, low-cost, small form factor portable devices.

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img5.png" />

## Further information about M6E-NANO, we attach datasheet of M6E-NANO

## Run Using Python (Raspberry Pi)
First, make sure you have the required packages

 ```pip install Pillow ```

```sudo apt-get install unzip patch xsltproc gcc libreadline-dev python-dev python-setuptools```

Install Mercury API, for this you need to download below repository

https://github.com/gotthardp/python-mercuryapi

 or 
 
```git clone https://github.com/gotthardp/python-mercuryapi.git```

```cd python-mercuryapi```

Give permission to all files

```sudo chmod 777 *```

```make```

The make command will automatically determine which Python version is installed. If both 2.x and 3.x are installed, the 3.x takes precedence. To build and install 2.x you need to explicitly specify the Python interpreter to use:

```sudo make PYTHON=python```

Then, install the module by running

```sudo make install```

which is a shortcut to running

```sudo python setup.py build install```

#### make sure jumper wire is sort between RX-TX0 and TX-RX1
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img10.jpg" />

## Run Using Universal Assistant(Through Micro USB)
**Download Universal Assistant Software From Below Link, And Install The Software**

https://www.jadaktech.com/resources/all-document-libraries/#Universal_Reader_Assistant

**Step 1 - Open the software, Connect UHF HAT To computer via micro usb cable ( make sure jumper wire is sort between U_RX-TX0 and U_TX-RX1 ) as shown in picture, then click on refresh button to refresh the serial port**

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img9.jpg" />

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img.JPG" />

**Step 2 - Then click next or skip button**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img1.JPG" />

**Step 3 - Then select the baudrate**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img2.JPG" />
        
**Step 4 - Connect**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img3.JPG" />
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img4.JPG" />
         
**Step 5 - Select your region and anteena and go to read**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img6.JPG" />
         
**Step 6 - Now it start read the cards**
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img7.JPG" />
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img8.JPG" />

## Buzzer is connected to GPIO 17 Pin of raspberry pi

## Code (raspberry pi)
### Make sure before run applications which is inside application folder, copy all the application files outside the folder then run the file
#### Inside application folder, there are three files 
 * attendance.py  - run this file to apply attendance 
 * library_management.py - run this file to do library management
 * smart_shopping.py - run this file to do smart shopping

## Youtube
https://www.youtube.com/watch?v=vQsGz0Gdf00&t=9s
