##############################################################################
Chapter Pong Game
##############################################################################

We have experienced single-player game snake before. Now, let's use ESP32S3 board to play classic two-player pong game. You will experience both 2D and 3D version.

Project Pong Game
*******************************

First, let's experience the 2D version game.

Component List
==========================

+-----------------------------+----------------------------------+
| ESP32-S3 WROOM x1           | GPIO Extension Board x1          |
|                             |                                  |
| |Chapter01_00|              | |Chapter01_01|                   |
+-----------------------------+----------------------------------+
| Breadboard x1                                                  |
|                                                                |
| |Chapter01_02|                                                 |
+-----------------------------+----------------------------------+
| Rotary potentiometer x1     | Jumper M/M x3                    |
|                             |                                  |
| |Chapter09_00|              |  |Chapter01_05|                  |
+-----------------------------+----------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter09_00| image:: ../_static/imgs/9_AD_Converter/Chapter09_00.png

Circuit
==========================

Use A0, A3 ports on ESP32S3 board to detect the voltage of rotary potentiometers.

.. list-table::
   :width: 100%
   :header-rows: 1 
   :align: center
   
   * -  Schematic diagram
   * -  |Chapter05_00|
   * -  Hardware connection. 
   * -  |Chapter05_01|

.. |Chapter05_00| image:: ../_static/imgs/5_Pong_Game/Chapter05_00.png
.. |Chapter05_01| image:: ../_static/imgs/5_Pong_Game/Chapter05_01.png

Sketch
========================

Sketch Pong_Game
--------------------------

Use Processing to open Pong_Game and click Run. If the connection succeeds, the follow will be shown:

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_02.png
    :align: center

Now you can try to turn the potentiometer to control the movement of paddle without ball. Press space bar to start the game: 

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_03.png
    :align: center

Use potentiometer to control the movement of paddle to block the ball back. The game rules are the same as classic pong game:

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_04.png
    :align: center

The game will be over when one side reachs three points. Pressing the space bar can restart the game:

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_05.png
    :align: center

Additionally, you can restart the game by pressing the space bar at any time.

Project Pong Game 3D
**********************************

Now, let's experience the 3D version game.

Component list
============================

The same as last section.

Circuit
============================

The same as last section.

Sketch
==============================

Sketch Pong_Game_3D
--------------------------------

Use Processing to open Pong_Game_3D.pde and click Run. If the connection succeeds, the follow will be shown:

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_06.png
    :align: center

Now you can try to turn the potentiometer to control the movement of paddle without ball. Press space bar to start the game: 

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_07.png
    :align: center

Use potentiometer to control the movement of paddle to block the ball back. The game rules are the same as classic pong game:

.. image:: ../_static/imgs/5_Pong_Game/Chapter05_08.png
    :align: center

The rest operation is the same as the 2D version.