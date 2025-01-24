##############################################################################
Chapter LED (Important)
##############################################################################

This chapter is the Start Point in the journey to build and explore ESP32-S3 WROOM electronic projects. We will start with simple "Blink" project.

Project Blink
*********************************

In this project, we will use ESP32-S3 WROOM to control blinking a common LED.

Component List
=================================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | USB cable x1                     |
|                             |                                  |
| |Chapter00_00|              | |Chapter00_01|                   |
+-----------------------------+----------------------------------+

.. |Chapter00_00| image:: ../_static/imgs/0_LED/Chapter00_00.png
.. |Chapter00_01| image:: ../_static/imgs/0_LED/Chapter00_01.png

Power
-------------------------------

ESP32-S3 WROOM needs 5v power supply. In this tutorial, we need connect ESP32-S3 WROOM to computer via USB cable to power it and program it. We can also use other 5v power source to power it.

.. image:: ../_static/imgs/1_LED/Chapter01_18.png
    :align: center

In the following projects, we only use USB cable to power ESP32-S3 WROOM by default.

In the whole tutorial, we don't use T extension to power ESP32-S3 WROOM. So 5V and 3.3V (includeing EXT 3.3V) on the extension board are provided by ESP32-S3 WROOM. 

We can also use DC jack of extension board to power ESP32-S3 WROOM. In this way, 5v and EXT 3.3v on extension board are provided by external power resource.

Code
===============================

Codes used in this tutorial are saved in "Freenove_Ultimate_Starter_Kit_for_ESP32_S3/Python/

Python_Codes". You can move the codes to any location. For example, we save the codes in Disk(D) with the path of "D:/Micropython_Codes".

Blink
---------------------------------

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes".

.. image:: ../_static/imgs/1_LED/Chapter01_19.png
    :align: center

Expand folder "01.1_Blink" and double click "Blink.py" to open it. As shown in the illustration below.

.. image:: ../_static/imgs/1_LED/Chapter01_20.png
    :align: center

Make sure ESP32-S3 has been connected with the computer with ESP32-S3 correctly. Click "Stop/Restart backend" or press the reset button, and then wait to see what interface will show up.

.. image:: ../_static/imgs/1_LED/Chapter01_21.png
    :align: center

Click "Run current script" shown in the box above, the code starts to be executed and the LED in the circuit starts to blink. 

.. image:: ../_static/imgs/1_LED/Chapter01_22.png
    :align: center

.. note::

    This is the code :ref:`running online<running_online>`. If you disconnect USB cable and repower ESP32-S3 or press its reset key, LED stops blinking and the following messages will be displayed in Thonny.

.. image:: ../_static/imgs/1_LED/Chapter01_23.png
    :align: center

Uploading code to ESP32S3
----------------------------------

As shown in the following illustration, right-click the file Blink.py and select "Upload to /" to upload code to ESP32S3.

.. image:: ../_static/imgs/1_LED/Chapter01_24.png
    :align: center

Upload boot.py in the same way.

.. image:: ../_static/imgs/1_LED/Chapter01_25.png
    :align: center

Press the reset key of ESP32-S3 and you can see LED is ON for one second and then OFF for one second, which repeats in an endless loop. 

.. image:: ../_static/imgs/1_LED/Chapter01_26.png
    :align: center

If you want to exit the offline operation mode, you can press Ctrl+C at the same time in the shell to let the ESP32-S3 exit the offline operation mode.

.. image:: ../_static/imgs/1_LED/Chapter01_27.png
    :align: center

If there is no response after pressing, it is recommended to press again until exiting.

If you have any concerns, please contact us via: support@freenove.com

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/01.1_Blink/Blink.py
    :linenos: 
    :language: python
    :lines: 1-12
    :dedent:

Each time a new file is opened, the program will be executed from top to bottom. When encountering a loop construction, it will execute the loop statement according to the loop condition.

.. image:: ../_static/imgs/1_LED/Chapter01_28.png
    :align: center

Print() function is used to print data to Terminal. It can be executed in Terminal directly or be written in a Python file and executed by running the file.

.. code-block:: python

    print("Hello world!")

Each time when using the functions of ESP32S3, you need to import modules corresponding to those functions: Import sleep_ms module of time module and Pin module of machine module.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/01.1_Blink/Blink.py
    :linenos: 
    :language: python
    :lines: 1-2
    :dedent:

Configure GPIO2 of ESP32-S3 to output mode and assign it to an object named "led". 

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/01.1_Blink/Blink.py
    :linenos: 
    :language: python
    :lines: 4-4
    :dedent:

It means that from now on, LED represents GPIO2 that is in output mode.

Set the value of LED to 1 and GPIO2 will output high level.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/01.1_Blink/Blink.py
    :linenos: 
    :language: python
    :lines: 7-7
    :dedent:

Set the value of LED to 0 and GPIO2 will output low level.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/01.1_Blink/Blink.py
    :linenos: 
    :language: python
    :lines: 9-9
    :dedent:

Execute codes in a while loop.

.. code-block:: python

    while True:
        ......

Put statements that may cause an error in "try" block and the executing statements when an error occurs in "except" block. In general, when the program executes statements, it will execute those in "try" block. However, when an error occurs to ESP32-S3 due to some interference or other reasons, it will execute statements in "except" block.

"Pass" is an empty statement. When it is executed, nothing happens. It is useful as a placeholder to make the structure of a program look better. 

.. code-block:: python

    try:
        ...
    except:
        pass

The single-line comment of Micropython starts with a "#" and continues to the end of the line. Comments help us to understand code. When programs are running, Thonny will ignore comments.

.. code-block:: python

    #Set led turn on

MicroPython uses indentations to distinguish different blocks of code instead of braces. The number of indentations is changeable, but it must be consistent throughout one block. If the indentation of the same code block is inconsistent, it will cause errors when the program runs.

.. code-block:: python

    while True:
        led.value(1) #Set led turn on
        sleep_ms(1000)
        led.value(0) #Set led turn off
        sleep_ms(1000)

How to import python files
----------------------------------

Whether to import the built-in python module or to import that written by users, the command "import" is needed.

If you import the module directly you should indicate the module to which the function or attribute belongs when using the function or attribute (constant, variable) in the module. The format should be: <module name>.<function or attribute>, otherwise an error will occur. 

.. image:: ../_static/imgs/1_LED/Chapter01_29.png
    :align: center

If you only want to import a certain function or attribute in the module, use the from...import statement. The format is as follows

.. image:: ../_static/imgs/1_LED/Chapter01_30.png
    :align: center

When using "from...import" statement to import function, to avoid conflicts and for easy understanding, you can use "as" statement to rename the imported function, as follows

.. image:: ../_static/imgs/1_LED/Chapter01_31.png
    :align: center

Reference
--------------------------------

.. py:function:: Class machine	
    
    Before each use of the machine module, please add the statement "import machine" to the top of python file.
    
    **machine.freq(freq_val):** When freq_val is not specified, it is to return to the current CPU frequency; Otherwise, it is to set the current CPU frequency.
    
    **freq_val:** 80000000(80MHz)、160000000(160MHz)、240000000(240MHz)
    
    **machine.reset():** A reset function. When it is called, the program will be reset.
    
    **machine.unique_id():** Obtains MAC address of the device. 
    
    **machine.idle():** Turns off any temporarily unused functions on the chip and its clock, which is useful to reduce power consumption at any time during short or long periods.
    
    **machine.disable_irq():** Disables interrupt requests and return the previous IRQ state. The disable_irq () function and enable_irq () function need to be used together; Otherwise the machine will crash and restart.
    
    **machine.enable_irq(state):** To re-enable interrupt requests. The parameter state should be the value that was returned from the most recent call to the disable_irq() function
    
    **machine.time_pulse_us(pin, pulse_level, timeout_us=1000000):**
    
    Tests the duration of the external pulse level on the given pin and returns the duration of the external pulse level in microseconds. When pulse level = 1, it tests the high level duration; When pulse level = 0, it tests the low level duration.
    
    If the setting level is not consistent with the current pulse level, it will wait until they are consistent, and then start timing. If the set level is consistent with the current pulse level, it will start timing immediately.
    
    When the pin level is opposite to the set level, it will wait for timeout and return "-2". When the pin level and the set level is the same, it will also wait timeout but return "-1". timeout_us is the duration of timeout. 

.. py:function:: Class Pin(id[, mode, pull, value])
    
    Before each use of the Pin module, please add the statement "from machine import Pin" to the top of python file.
    
    **id:** Arbitrary pin number
    
    **mode:** Mode of pins
    
        **Pin.IN:** Input Mode
    
        **Pin.OUT:** Output Mode
    
        **Pin.OPEN_DRAIN:** Open-drain Mode
    
    **Pull:** Whether to enable the internal pull up and down mode
    
        **None:** No pull up or pull down resistors
    
        **Pin.PULL_UP:** Pull-up Mode, outputting high level by default
    
        **Pin.PULL_DOWN:** Pull-down Mode, outputting low level by default
    
    **Value:** State of the pin level, 0/1
    
    **Pin.init(mode, pull):** Initialize pins 
    
    **Pin.value([value]):** Obtain or set state of the pin level, return 0 or 1 according to the logic level of pins. Without parameter, it reads input level. With parameter given, it is to set output level. 
    
    **value:** It can be either True/False or 1/0.
    
    Pin.irq(trigger, handler):** Configures an interrupt handler to be called when the pin level meets a condition.     
    
    **trigger:**  
    
            **Pin.IRQ_FALLING:** interrupt on falling edge

            **Pin.IRQ_RISING:** interrupt on rising edge

            **3:** interrupt on both edges
    
        **Handler:** callback function

.. py:function:: Class time
    
    Before each use of the **time** module, please add the statement "import time" to the top of python file
    
    **time.sleep(sec):** Sleeps for the given number of seconds
    
        **sec:** This argument should be either an int or a float.
    
    **time.sleep_ms(ms):** Sleeps for the given number of milliseconds, ms should be an int.
    
    **time.sleep_us(us):** Sleeps for the given number of microseconds, us should be an int.
    
    **time.time():** Obtains the timestamp of CPU, with second as its unit.
    
    **time.ticks_ms():** Returns the incrementing millisecond counter value, which recounts after some values.
    
    **time.ticks_us():** Returns microsecond
    
    **time.ticks_cpu():** Similar to ticks_ms() and ticks_us(), but it is more accurate(return clock of CPU).
    
    **time.ticks_add(ticks, delta):** Gets the timestamp after the offset.
    
        **ticks:** ticks_ms()、ticks_us()、ticks_cpu()
    
        **delta:** Delta can be an arbitrary integer number or numeric expression
    
    **time.ticks_diff(old_t, new_t):** Calculates the interval between two timestamps, such as ticks_ms(), ticks_us() or ticks_cpu().
    
        **old_t:** Starting time
    
        **new_t:** Ending time

Project Blink
*********************************

In this project, we will use ESP32-S3 WROOM to control blinking a common LED.

Component List
============================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | GPIO Extension Board x1          |
|                             |                                  |
| |Chapter01_00|              | |Chapter01_01|                   |
+-----------------------------+----------------------------------+
| Breadboard x1                                                  |
|                                                                |
| |Chapter01_02|                                                 |
+-------------------+------------------+-------------------------+
| LED x1            | Resistor 220Ω x1 | Jumper M/M x2           |
|                   |                  |                         |
| |Chapter01_03|    | |Chapter01_04|   | |Chapter01_05|          |
+-------------------+------------------+-------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_03| image:: ../_static/imgs/1_LED/Chapter01_03.png
    :width: 50%
.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png

Component knowledge
========================

LED
------------------------

A LED is a type of diode. All diodes only work if current is flowing in the correct direction and have two poles. A LED will only work (light up) if the longer pin (+) of LED is connected to the positive output from a power source and the shorter pin is connected to the negative (-).  Negative output is also referred to as Ground (GND). This type of component is known as "diodes" (think One-Way Street).

All common 2 lead diodes are the same in this respect. Diodes work only if the voltage of its positive electrode is higher than its negative electrode and there is a narrow range of operating voltage for most all common diodes of 1.9 and 3.4V. If you use much more than 3.3V the LED will be damaged and burn out.

.. image:: ../_static/imgs/1_LED/Chapter01_06.png
    :align: center

.. note::
    
    LEDs cannot be directly connected to a power supply, which usually ends in a damaged component. A resistor with a specified resistance value must be connected in series to the LED you plan to use.

Resistor
--------------------------

Resistors use Ohms (Ω) as the unit of measurement of their resistance (R). 1MΩ=1000kΩ, 1kΩ=1000Ω. 

A resistor is a passive electrical component that limits or regulates the flow of current in an electronic circuit. 

On the left, we see a physical representation of a resistor, and the right is the symbol used to represent the presence of a resistor in a circuit diagram or schematic.

.. image:: ../_static/imgs/1_LED/Chapter01_07.png
    :align: center

The bands of color on a resistor is a shorthand code used to identify its resistance value. For more details of resistor color codes, please refer to the appendix of this tutorial.

With a fixed voltage, there will be less current output with greater resistance added to the circuit. The relationship between Current, Voltage and Resistance can be expressed by this formula: I=V/R known as Ohm's Law where I = Current, V = Voltage and R = Resistance. Knowing the values of any two of these allows you to solve the value of the third.

In the following diagram, the current through R1 is: I=U/R=5V/10kΩ=0.0005A=0.5mA. 

.. image:: ../_static/imgs/1_LED/Chapter01_08.png
    :align: center

WARNING: Never connect the two poles of a power supply with anything of low resistance value (i.e. a metal object or bare wire) this is a Short and results in high current that may damage the power supply and electronic components.

.. note::
    
    Unlike LEDs and diodes, resistors have no poles and re non-polar (it does not matter which direction you insert them into a circuit, it will work the same)

Breadboard
------------------------------

Here we have a small breadboard as an example of how the rows of holes (sockets) are electrically attached. 

The left picture shows the way to connect pins. The right picture shows the practical internal structure.

.. image:: ../_static/imgs/1_LED/Chapter01_10.png
    :align: center

Power
------------------------------

ESP32-S3 WROOM needs 5v power supply. In this tutorial, we need connect ESP32-S3 WROOM to computer via USB cable to power it and program it. We can also use other 5v power source to power it.

.. image:: ../_static/imgs/1_LED/Chapter01_09.png
    :align: center

In the following projects, we only use USB cable to power ESP32-S3 WROOM by default.

In the whole tutorial, we don't use T extension to power ESP32-S3 WROOM. So 5V and 3.3V (includeing EXT 3.3V) on the extension board are provided by ESP32-S3 WROOM. 

We can also use DC jack of extension board to power ESP32-S3 WROOM.In this way, 5v and EXT 3.3v on extension board are provided by external power resource.

Circuit
===============================

First, disconnect all power from the ESP32-S3 WROOM. Then build the circuit according to the circuit and hardware diagrams. After the circuit is built and verified correct, connect the PC to ESP32-S3 WROOM. 

CAUTION: Avoid any possible short circuits (especially connecting 5V or GND, 3.3V and GND)! WARNING: A short circuit can cause high current in your circuit, generate excessive component heat and cause permanent damage to your hardware!

.. list-table::
   :width: 100%
   :header-rows: 1 
   :align: center
   
   * -  Schematic diagram
   * -  |Chapter01_11|
   * -  Hardware connection. 
       
        :red:`If you need any support, please contact us via:` support@freenove.com
   * -  |Chapter01_12|

        :red:`Don't rotate ESP32-S3 WROOM 180° for connection.`
    
.. |Chapter01_11| image:: ../_static/imgs/1_LED/Chapter01_11.png
.. |Chapter01_12| image:: ../_static/imgs/1_LED/Chapter01_12.png

Code
=========================

Codes used in this tutorial are saved in "Freenove_Ultimate_Starter_Kit_for_ESP32_S3/Python/

Python_Codes". You can move the codes to any location. For example, we save the codes in Disk(D) with the path of "D:/Micropython_Codes".

Blink
----------------------------

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes".

.. image:: ../_static/imgs/1_LED/Chapter01_32.png
    :align: center

Expand folder "01.1_Blink" and double click "Blink.py" to open it. As shown in the illustration below.

.. image:: ../_static/imgs/1_LED/Chapter01_33.png
    :align: center

Make sure ESP32-S3 has been connected with the computer with ESP32-S3 correctly. Click "Stop/Restart backend" or press the reset button, and then wait to see what interface will show up.

.. image:: ../_static/imgs/1_LED/Chapter01_34.png
    :align: center

Click "Run current script" shown in the box above, the code starts to be executed and the LED in the circuit starts to blink. 

.. image:: ../_static/imgs/1_LED/Chapter01_35.png
    :align: center

.. note::

    This is the code running online. If you disconnect USB cable and repower ESP32-S3 or press its reset key, LED stops blinking and the following messages will be displayed in Thonny.

.. image:: ../_static/imgs/1_LED/Chapter01_36.png
    :align: center

Uploading code to ESP32S3
--------------------------------

As shown in the following illustration, right-click the file Blink.py and select "Upload to /" to upload code to ESP32S3.

.. image:: ../_static/imgs/1_LED/Chapter01_37.png
    :align: center

Upload boot.py in the same way.

.. image:: ../_static/imgs/1_LED/Chapter01_38.png
    :align: center

Press the reset key of ESP32-S3 and you can see LED is ON for one second and then OFF for one second, which repeats in an endless loop. 

Press the reset key of ESP32-S3 and you can see LED is ON for one second and then OFF for one second, which repeats in an endless loop. 

.. image:: ../_static/imgs/1_LED/Chapter01_39.png
    :align: center

If you want to exit the offline operation mode, you can press Ctrl+C at the same time in the shell to let the ESP32-S3 exit the offline operation mode.

.. image:: ../_static/imgs/1_LED/Chapter01_40.png
    :align: center

If there is no response after pressing, it is recommended to press again until exiting.

:red:`If you have any concerns, please contact us via:` support@freenove.com