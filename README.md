# RGB Led Control GUI
This is a Kivy GUI for the control of a RGB LED via serial port. This GUI was designed as a helper tool for the students involved in the "Electronic Technologies and Biosensors Laboratory" course at Politecnico di Milano, to better understand Kivy functionality and the serial communication between Python and a micro-controller. 

## Functionality
The GUI shows three sliders, that allow to control the three channels of the RGB LED.

![alt text](https://github.com/dado93/RGB_LED_Control_GUI/blob/main/images/screen.jpg?raw=true)

When clicking on the "Update Color" button, the following packet is sent to the MCU:

Byte (HEX)   | Description |
:-----------:|-------------|
0xA0         | Packet header (decimal value: 160)
R            | Red light (0x00-0xFF in Hex, 0-255 in decimal)
G            | Green light (0x00-0xFF in Hex, 0-255 in decimal)
B            | Blue light (0x00-0xFF in Hex, 0-255 in decimal)
0xC0         | Packet tail (decimal value: 192)

## Requirements
- [Kivy](https://kivy.org/#home)
- [PySerial](https://pypi.org/project/pyserial/)

## Author
[Davide Marzorati](mailto:davide.marzorati@polimi.it)