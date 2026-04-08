##############################################################################
Chapter Camera Web Server
##############################################################################

In this section, we'll use ESP32's video function as an example to study.

Project 05.1 Camera Web Server
*************************************

Connect ESP32 using USB and check its IP address through serial monitor. Use web page to access IP address to obtain video and image data.

Component List
==============================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | USB cable x1                     |
|                             |                                  |
| |Chapter00_00|              | |Chapter00_01|                   |
+-----------------------------+----------------------------------+

.. |Chapter00_00| image:: ../_static/imgs/0_LED/Chapter00_00.png
.. |Chapter00_01| image:: ../_static/imgs/0_LED/Chapter00_01.png

Circuit
======================

Connect Freenove ESP32-S3 to the computer using the USB cable. 

.. image:: ../_static/imgs/31_TCP_IP/Chapter31_08.png
    :align: center

Code
=======================

Move the program folder "**Freenove ESP32-S3 WROOM Board/Python/Python_Codes**" to disk(D) in advance with the path of "**D:/Micropython_Codes**".

Since Micropython does not provide firmware including camera module, in this chapter, we will use the camera based on the firmware in lemariva's Github project, micropython-camera-driver.

Project link: https://github.com/lemariva/micropython-camera-driver

Before starting the project, we need to re-upload the firmware with the camera module via steps below.

Open Thonny, click "run" and select "Select interpreter..."

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_16.png
    :align: center

Select "Micropython (ESP32)", select "USB Single Serial @ COM28", and then click the long button under "Firmware".

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_17.png
    :align: center

Click "Select local MicroPython image \.\.\.".

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_18.png
    :align: center

Choose "esp32s3_camera_st7789_n8r8_1.20.bin"

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_19.png
    :align: center

Select "USB Single Serial @ COM28"

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_20.png
    :align: center

Click "Install", Wait for completion.

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "05.1_Camera_WebServer". Select folder "**lib**", right click your mouse to select "Upload to /", wait for "**lib**" to be uploaded to ESP32-WROVER and then double click "**picoweb_video.py**".

05.1_Camera_WebServer
--------------------------

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_21.png
    :align: center

Before running the program, please modify your router's name and password in the box shown in the illustration above to make sure that your code can compile and work successfully. 

Click "run" to run the code "picoweb_video.py", then you can see the following content in the shell area.

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_22.png
    :align: center

If your ESP32S3 has been in the process of connecting to router, but the information above has not been printed out, please re-check whether the router name and password have been entered correctly and press the reset key on ESP32S3 to wait for a successful connection prompt. 

Open a web browser, enter the IP address printed by the serial monitor in the address bar, and access it. 

Taking the Google browser as an example, here's what the browser prints out after successful access to ESP32S3's IP.

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_23.png
    :align: center

The effect is shown in the image below.

.. image:: ../_static/imgs/32_Camera_Web_Server/Chapter32_24.png
    :align: center

Please note:

If the shell area prompts an error when you click to run the code, please press the rst button on the ESP32S3, wait for the system reset to complete, and then re-run the code.

The following is the program code.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 1-118
    :dedent:

Import picoweb、utime、camera、gc modules.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 3-6
    :dedent:

Before running the code, please modify the WiFi name and password in the code to ensure that the ESP32S3 can connect to the network.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 8-9
    :dedent:

Define the WiFi connection function, set the ESP32S3 to STA mode, and let the ESP32S3 connect to the nearby WiFi. If the connection is successful, the WiFi configuration information of the ESP32S3 will be printed; if the connection fails, the connection timeout will be printed.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 12-26
    :dedent:

The deinit() is used to disable the configuration of the camera to prevent the previous configuration from interfering with the following configuration.

The init() is used to configure the camera's pin driver, image data format, resolution and other information. By default, please do not modify this function, otherwise the camera initialization fails and the image cannot be obtained.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 31-37
    :dedent:

This function can set the resolution of the camera individually, you can refer to the notes below to select the appropriate resolution size.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 39-45
    :dedent:

The following functions can modify the image information obtained by the camera.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 47-58
    :dedent:

This is the code for a simple web interface, used here as an example.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 61-72
    :dedent:

Web page response function. When a user visits the webpage "/" built by ESP32S3, ESP32S3 calls this function, allowing the user to observe a display interface in the browser.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 75-77
    :dedent:

send_frame() can send the image obtained by ESP32S3 in web page format. When someone visits the webpage "/video" built by the ESP32S3, the video(req, resp) function is used to continuously fetch images and send them to the browser.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 79-93
    :dedent:

Create two route decorators and declare their listening strings and corresponding response handlers respectively.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 96-100
    :dedent:

This is the main part of the program. First initialize the ESP32S3 camera, and then configure WiFi to connect the ESP32S3 to the network. Call the picoweb library, build a webserver, and run it.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/05.1_Camera_WebServer/picoweb_video.py
    :linenos: 
    :language: python
    :lines: 105-113
    :dedent:

Reference
--------------------

.. table::
    :class: zebra
    :align: center
    
    +-------------------+-----------+------------------+-----------+
    | Image resolution  | Sharpness | Image resolution | Sharpness |
    +===================+===========+==================+===========+
    | FRAMESIZE_96x96   | 96x96     | FRAMESIZE_HVGA   | 480x320   |
    +-------------------+-----------+------------------+-----------+
    | FRAMESIZE_QQVGA   | 160x120   | FRAMESIZE_VGA    | 640x480   |
    +-------------------+-----------+------------------+-----------+
    | FRAMESIZE_QCIF    | 176x144   | FRAMESIZE_SVGA   | 800x600   |
    +-------------------+-----------+------------------+-----------+
    | FRAMESIZE_HQVGA   | 240x176   | FRAMESIZE_XGA    | 1024x768  |
    +-------------------+-----------+------------------+-----------+
    | FRAMESIZE_240x240 | 240x240   | FRAMESIZE_HD     | 1280x720  |
    +-------------------+-----------+------------------+-----------+
    | FRAMESIZE_QVGA    | 320x240   | FRAMESIZE_SXGA   | 1280x1024 |
    +-------------------+-----------+------------------+-----------+
    | FRAMESIZE_CIF     | 400x296   | FRAMESIZE_UXGA   | 1600x1200 |
    +-------------------+-----------+------------------+-----------+

:combo:`red font-bolder:We recommend that the resolution not exceed VGA(640x480).`