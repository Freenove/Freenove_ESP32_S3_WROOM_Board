##############################################################################
Chapter Read and Write the SDcard
##############################################################################

An SDcard slot is integrated on the back of the ESP32-S3 WROOM. In this chapter we learn how to use ESP32-S3 to read and write SDcard.

Project SDMMC Test
***************************************

Component List
=============================

.. list-table::
   :width: 100%
   :align: center
   
   * -  ESP32-S3 WROOM x1
     -  USB cable x1
     -  SDcard reader x1 (random color)
     -  SDcard x1
       
   * -  |Chapter28_02|
     -  |Chapter28_03|
     -  |Chapter28_00| 

        :red:`(Not a USB flash drive.)`  
     -  |Chapter28_01|

.. |Chapter28_02| image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_02.png
.. |Chapter28_03| image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_03.png
.. |Chapter28_00| image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_00.png
.. |Chapter28_01| image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_01.png

Component knowledge
================================

SD card read and write method
-----------------------------------

ESP32-S3 has two ways to use SD card, one is to use the SPI interface to access the SD card, and the other is to use the SDMMC interface to access the SD card. SPI mode uses 4 IOs to access SD card. The SDMMC has one-bit bus mode and four-bit bus mode. In one-bit bus mode, SDMMC use 3 IOs to access SD card. In four-bit bus mode, SDMMC uses 6 IOs to access the SD card.

The above three methods can all be used to access the SD card, the difference is that the access speed is different.

In the four-bit bus mode of SDMMC, the reading and writing speed of accessing the SD card is the fastest. In the one-bit bus mode of SDMMC, the access speed is about 80% of the four-bit bus mode. The access speed of SPI is the slowest, which is about 50% of the four-bit bus mode of SDMMC.

Usually, we recommend using the one-bit bus mode to access the SD card, because in this mode, we only need to use the least pin IO to access the SD card with good performance and speed.

Format SD card
===================================

Before starting the tutorial, we need to create a drive letter for the blank SD card and format it. This step requires a card reader and SD card. Please prepare them in advance. Below we will guide you to do it on different computer systems. You can choose the guide that matches your computer.

Windows
-----------------------------------

Insert the SD card into the card reader, then insert the card reader into the computer.

In the Windows search box, enter "Disk Management" and select "Create and format hard disk partitions".

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_04.png
    :align: center

In the new pop-up window, find an unallocated volume close to 1G in size.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_05.png
    :align: center

Click to select the volume, right-click and select "New Simple Volume".

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_06.png
    :align: center

Click Next.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_07.png
    :align: center

You can choose the drive letter on the right, or you can choose the default. By default, just click Next.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_08.png
    :align: center

File system is FAT(or FAT32). The Allocation unit size is 16K, and the Volume label can be set to any name. After setting, click Next.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_09.png
    :align: center

Click Finish. Wait for the SD card initialization to complete.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_10.png
    :align: center

At this point, you can see the SD card in This PC.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_11.png
    :align: center

MAC
-------------------------------------

Insert the SD card into the card reader, then insert the card reader into the computer. Some computers will prompt the following information, please click to ignore it.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_12.png
    :align: center

Find "Disk Utility" in the MAC system and click to open it.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_13.png
    :align: center

Select "Generic MassStorageClass Media", note that its size is about 1G. Please do not choose wrong item. Click "Erase".

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_14.png
    :align: center

Select the configuration as shown in the figure below, and then click "Erase".

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_15.png
    :align: center

Wait for the formatting to complete. When finished, it will look like the picture below. At this point, you can see a new disk on the desktop named "SD".

Circuit
=============================

Before connecting the USB cable, insert the SD card into the SD card slot on the back of the ESP32-S3.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_16.png
    :align: center

Connect Freenove ESP32-S3 to the computer using the USB cable.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_17.png
    :align: center

Sketch
=============================

Sketch_SDMMC_Test
-----------------------------

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_18.png
    :align: center

Compile and upload the code to ESP32-S3-WROOM, open the serial monitor, and press the RST button on the board.

You can see the printout as shown below.

.. image:: ../_static/imgs/28_Read_and_Write_the_SDcard/Chapter28_19.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :dedent:

Add the SD card drive header file.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 7-8
    :dedent:

Defines the drive pins of the SD card. Please do not modify it. Because these pins are fixed.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 10-12
    :dedent:

Initialize the serial port function. Sets the drive pin for SDMMC one-bit bus mode.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 15-16
    :dedent:

Set the mount point of the SD card, set SDMMC to one-bit bus mode, and set the read and write speed to 20MHz.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 17-20
    :dedent:

Get the type of SD card and print it out through the serial port.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 21-36
    :dedent:

Call the listDir() function to read the folder and file names in the SD card, and print them out through the serial port. This function can be found in "sd_read_write.cpp".

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 41-41
    :dedent:

Call createDir() to create a folder, and call removeDir() to delete a folder.

.. code-block:: C

    createDir(SD_MMC, "/mydir");
    removeDir(SD_MMC, "/mydir");

Call writeFile() to write any content to the txt file. If there is no such file, create this file first.

Call appendFile() to append any content to txt.

Call readFile() to read the content in txt and print it via the serial port.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 49-51
    :dedent:

Call deleteFile() to delete a specified file.

Call renameFile() to copy a file and rename it.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 53-54
    :dedent:

Call the testFileIO() function to test the time it takes to read 512 bytes and the time it takes to write 2048*512 bytes of data.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 57-57
    :dedent:

Print the total size and used size of the SD card via the serial port.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_28.1_SDMMC_Test/Sketch_28.1_SDMMC_Test.ino
    :linenos: 
    :language: c
    :lines: 59-60
    :dedent: