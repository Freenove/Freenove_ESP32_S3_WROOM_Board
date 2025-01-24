##############################################################################
Chapter Bluetooth
##############################################################################

This chapter mainly introduces how to make simple data transmission through Bluetooth of ESP32-S3 WROOM and mobile phones.

Project Bluetooth Low Energy Data Passthrough
*************************************************************

Component List
=============================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | USB cable x1                     |
|                             |                                  |
| |Chapter00_00|              | |Chapter00_01|                   |
+-----------------------------+----------------------------------+

.. |Chapter00_00| image:: ../_static/imgs/0_LED/Chapter00_00.png
.. |Chapter00_01| image:: ../_static/imgs/0_LED/Chapter00_01.png

Component knowledge
==============================

ESP32-S3's integrated Bluetooth function Bluetooth is a short-distance communication system, which can be divided into two types, namely Bluetooth Low Energy(BLE) and Classic Bluetooth. There are two modes for simple data transmission: master mode and slave mode.

Master mode
-------------------------------

In this mode, works are done in the master device and it can connect with a slave device. And we can search and select slave devices nearby to connect with. When a device initiates connection request in master mode, it requires information of the other Bluetooth devices including their address and pairing passkey. After finishing pairing, it can connect with them directly.

Slave mode
---------------------------------

The Bluetooth module in slave mode can only accept connection request from a host computer, but cannot initiate a connection request. After connecting with a host device, it can send data to or receive from the host device.

Bluetooth devices can make data interaction with each other, as one is in master mode and the other in slave mode. When they are making data interaction, the Bluetooth device in master mode searches and selects devices nearby to connect to. When establishing connection, they can exchange data. When mobile phones exchange data with ESP32-S3, they are usually in master mode and ESP32-S3 in slave mode.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_00.png
    :align: center

Circuit
==========================

Connect Freenove ESP32-S3 to the computer using the USB cable.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_01.png
    :align: center

Code
=========================

Lightblue
---------------------------

If you can't install Serial Bluetooth on your phone, try LightBlue.If you do not have this software installed on your phone, you can refer to this link：https://apps.apple.com/us/app/lightblue/id557428110#?platform=iphone.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_02.png
    :align: center

Move the program folder “Freenove_Ultimate_Starter_Kit_for_ESP32_S3/Python/Python_Codes” to disk(D) in advance with the path of “D:/Micropython_Codes”.

Open “Thonny”, click “This computer” -> “D:” -> “Micropython_Codes” -> “BLE”. Select “ble_advertising.py”, right click your mouse to select “Upload to /”, wait for “ble_advertising.py” to be uploaded to ESP32-S3 and then double click “BLE.py”. 

BLE
---------------------------

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_18.png
    :align: center

Click run for BLE.py.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_19.png
    :align: center

Turn ON Bluetooth on your phone, and open the Lightblue APP. 

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_20.png
    :align: center

In the Scan page, swipe down to refresh the name of Bluetooth that the phone searches for. Click ESP32S3.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_21.png
    :align: center

After Bluetooth is connect successfully, Shell will printer the information.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_22.png
    :align: center

Click “Receive”. Select the appropriate Data format in the box to the right of Data Format. For example, HEX for hexadecimal, utf-string for character, Binary for Binary, etc. Then click SUBSCRIBE.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_23.png
    :align: center

You can type “Hello” in Shell and press “Enter” to send.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_24.png
    :align: center

And then you can see the mobile Bluetooth has received the message.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_25.png
    :align: center

Similarly, you can select “Send” on your phone. Set Data format, and then enter anything in the sending box and click Write to send.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_26.png
    :align: center

You can check the message from Bluetooth in “Shell”.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_27.png
    :align: center

And now data can be transferred between your mobile phone and computer via ESP32S3.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.1_BLE/BLE.py
    :linenos: 
    :language: python
    :dedent:

Define the specified UUID number for BLE vendor.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 20-28
    :dedent:

Write an _irq function to manage BLE interrupt events.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 46-63
    :dedent:

Initialize the BLE function and name it.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 36-36
    :dedent:

When the mobile phone send data to ESP32-S3 via BLE Bluetooth, it will print them out with serial port; When the serial port of ESP32-S3 receive data, it will send them to mobile via BLE Bluetooth.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 80-96
    :dedent:

Project Bluetooth Control LED
*****************************************

In this section, we will control the LED with Bluetooth.

Component List
================================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | GPIO Extension Board x1          |
|                             |                                  |
| |Chapter01_00|              | |Chapter01_01|                   |
+-----------------------------+----------------------------------+
| Breadboard x1                                                  |
|                                                                |
| |Chapter01_02|                                                 |
+-----------------------------+----------------------------------+
| Resistor 220Ω x1            | Jumper M/M x2                    |
|                             |                                  |
| |Chapter01_04|              |  |Chapter19_02|                  |
+-----------------------------+----------------------------------+
| LED x1                      | Micro USB Wire x1                |
|                             |                                  |
| |Chapter01_04|              |  |Chapter08_00|                  |
+-----------------------------+----------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter19_02| image:: ../_static/imgs/19_Stepper_Motor/Chapter19_02.png
.. |Chapter08_00| image:: ../_static/imgs/8_Serial_Communication/Chapter08_00.png

Circuit
=================================

Connect Freenove ESP32-S3 to the computer using a USB cable.

.. list-table::
   :width: 100%
   :align: center
   
   * -  Schematic diagram
   * -  |Chapter27_12|
   * -  Hardware connection. 
       
        :red:`If you need any support, please contact us via:` support@freenove.com
   * -  |Chapter27_13|

.. |Chapter27_12| image:: ../_static/imgs/27_Bluetooth/Chapter27_12.png
.. |Chapter27_13| image:: ../_static/imgs/27_Bluetooth/Chapter27_13.png

Code
=================================

Move the program folder “Freenove_Ultimate_Starter_Kit_for_ESP32_S3/Python/Python_Codes” to disk(D) in advance with the path of “D:/Micropython_Codes”.

Open “Thonny”, click “This computer” -> “D:” -> “Micropython_Codes” -> “BLE_LED”. Select “ble_advertising.py”, right click your mouse to select “Upload to /”, wait for “ble_advertising.py” to be uploaded to ESP32-S3 and then double click “BLE_LED.py”.

BLE_LED
--------------------------------

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_28.png
    :align: center

Compile and upload code to ESP32S3. The operation of the APP is the same as 27.1, you only need to change the sending content to "led_on" and "led_off" to operate LEDs on the ESP32S3.

Data sent from mobile APP:

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_29.png
    :align: center

You can check the message sent by Bluetooth in “Shell”.

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_30.png
    :align: center

The phenomenon of LED

.. image:: ../_static/imgs/27_Bluetooth/Chapter27_31.png
    :align: center

.. attention:: 
    
    If the sending content isn't "led_on' or "led_off", then the state of LED will not change. If the LED is on, when receiving irrelevant content, it keeps on; Correspondingly, if the LED is off, when receiving irrelevant content, it keeps off.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.2_BLE_LED/BLE_LED.py
    :linenos: 
    :language: python
    :dedent:

Compare received message with "led_on" and "led_off" and take action accordingly.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/27.2_BLE_LED/BLE_LED.py
    :linenos: 
    :language: python
    :lines: 88-91
    :dedent: