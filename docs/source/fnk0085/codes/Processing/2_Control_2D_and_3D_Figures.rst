##############################################################################
Chapter Control 2D and 3D Figures
##############################################################################

In this chapter, we will use ESP32S3 board to make Processing program control figure changes. And we will control 2D and 3D figures, respectively.

Project Ellipse
**********************************

First, control a 2D figure.

Component list
=================================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | GPIO Extension Board x1          |
|                             |                                  |
| |Chapter01_00|              | |Chapter01_01|                   |
+-----------------------------+----------------------------------+
| Breadboard x1                                                  |
|                                                                |
| |Chapter01_02|                                                 |
+-----------------------------+----------------------------------+
| Jumper M/M x5               | Joystick x1                      |
|                             |                                  |
|  |Chapter01_05|             |  |Chapter14_00|                  |
+-----------------------------+----------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter14_00| image:: ../_static/imgs/14_Joystick/Chapter14_00.png

Circuit
===============================

Use GPIO1 and GPIO2 (A0 and A1) ports to detect the voltage value of two rotary potentiometers inside joystick.

.. list-table::
   :width: 100%
   :header-rows: 1 
   :align: center
   
   * -  Schematic diagram
   * -  |Chapter02_00|
   * -  Hardware connection. 
   * -  |Chapter02_01|

.. |Chapter02_00| image:: ../_static/imgs/2_Control_2D_and_3D_Figures/Chapter02_00.png
.. |Chapter02_01| image:: ../_static/imgs/2_Control_2D_and_3D_Figures/Chapter02_01.png

Sketch
========================

Sketch Ellipse
--------------------------

Use Processing to open Freenove_Ultimate_Starter_Kit_for_ESP32_S3\\C\\Processing\\Processing\\Ellipse\\Ellipse.pde, then click Run. If the connection succeeds, the following will be shown:

.. image:: ../_static/imgs/2_Control_2D_and_3D_Figures/Chapter02_02.png
    :align: center

Then you can change the ellipse shape by shifting the joystick:

.. image:: ../_static/imgs/2_Control_2D_and_3D_Figures/Chapter02_03.png
    :align: center

Project Box 3D
*********************************

Now control a 3D figure.

Component list
===============================

The same as last section.

Circuit
===============================

The same as last section.

Sketch
================================

Sketch Box_3D
-------------------------------

Use Processing to open Freenove_Ultimate_Starter_Kit_for_ESP32_S3\\C\\Processing\\Processing\\Box_3D\\Box_3D.pde, and click Run. If the connection succeeds, the following will be shown. The left is a 3D box presented by line and the right is a 3D box entity.

.. image:: ../_static/imgs/2_Control_2D_and_3D_Figures/Chapter02_04.png
    :align: center

Then you can change the space angle of two 3D box by shifting the joystick:

.. image:: ../_static/imgs/2_Control_2D_and_3D_Figures/Chapter02_05.png
    :align: center