# UHF-HAT-for-RaspberryPi

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img0.png" />

UHF HAT for Raspberry Pi is an advanced and compact "Ultra High Frequency" RFID reader that consists of powerful RFID technology designing for a broad range of applications in the defense, healthcare system, banks, offices etc. UHF HAT for Raspberry Pi has an onboard  ThingMagic® M6E Nano UHF RFID Reader that is JADAK’s smallest embeddable module with ultra-low power consumption and tiny form factor.  This RFID reader is ideal for battery operated, low-cost, small form factor portable devices.

<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img5.png" />

## Further information about M6E-NANO, we attach datasheet of M6E-NANO

### Enable Serial Port for this type ```sudo raspi-config``` in command promt, then go to Interface Options -> Serial Port - > Would you like a login shell to be accessible over ? type "**No**" then Would you like the serial port hardware to be enabled? type "**Yes**"
         
## How to enable the external UFL port in the UHF HAT
<img src = "https://github.com/sbcshop/UHF-HAT-for-RaspberryPi/blob/main/images/img10.png" />

## Run Using Python (Raspberry Pi) Run below command one by one

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

## Example codes (raspberry pi) 
Open Exmples directory for testing all other functionalities of UHF HAT. If the library error shows in any code file during compilation, please copy that file outside the example folder and then try to run. The names of code files and thier functions are mentioned below:

To scan cards, run below file

**```scan_cards.py```**  

To know the temperature of module (UHF HAT), Run below file 

**```read_temp.py```**

To write uhf tag or change tag id, run below file

**```tag_write.py```**

To read read basic Perameters like anteena, power etc, run below file 

**```read_basic_Perameters.py```**

Control onboard GPIO pins of UHF HAT

**```control_gpio_pins.py```**

### Make sure before run applications which is inside application folder, copy all the application files outside the folder then run the file
#### Inside application folder, there are three files 
 * attendance.py  - run this file to apply attendance 
 * library_management.py - run this file to do library management
 * smart_shopping.py - run this file to do smart shopping

## Youtube
https://www.youtube.com/watch?v=vQsGz0Gdf00&t=9s

## Getting started video or How to setup UHF HAT 

https://www.youtube.com/watch?v=saSQZn1sG-Y&ab_channel=SBComponentsLtd


## Documentation

* [UHF HAT For RaspberryPi Hardware](https://github.com/sbcshop/UHF-HAT-for-RaspberryPi-Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [RFID HAT for RaspberryPi](https://shop.sb-components.co.uk/products/rfid-hat-for-raspberry-pi?_pos=3&_sid=59f725ea2&_ss=r)

 ![RFID HAT for RaspberryPi](https://cdn.shopify.com/s/files/1/1217/2104/products/RFIDforPi.jpg?v=1614587676&width=600)

* [RaspberryPi Pico RFID Expansion](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion?_pos=3&_sid=075681430&_ss=r)

 ![RaspberryPi Pico RFID Expansion](https://cdn.shopify.com/s/files/1/1217/2104/products/2_85a5dfb2-96cb-4e0b-ba28-a70af127a4f1.png?v=1613732653&width=600)
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>
