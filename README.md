# MCU_Controller_With_Hand
Thanks to this project, there is a data flow to the microcontroller over the serial port according to the location of your hand. In this way, you can transmit various messages to your microcontroller using your camera.In this context, a servo application is shared with an example arduino code.

# Example Using
* Pair Arduino with your computer. Then upload the file in the example folder into the arduino with the arduino compiler. 
* Then run the file mcu_manipulator_hand.py via Python. Make your serial port settings properly before running the code. 
* For example, the code is set for COM4 port. If you are using COMx set it to COMx. For Linux or Mac systems, point the corresponding usb driver under the dev folder as the path.
* When you run the code and the arduino is connected to the computer, your servo will rotate 0 or 180 degrees depending on whether your hand is on the right or left. 
* For your servo connections, connect the orange cable of the servo motor to digital pin 3 of the arduino. Make the supply over 5V. 
