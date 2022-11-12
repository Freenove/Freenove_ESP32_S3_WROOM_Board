from machine import Pin
import time

lastChangeTime=0
keyState=0
State=0

class KeyPad(object):
    def __init__(self, row1: int=14, row2: int=13, row3: int=12, row4: int=11, col1: int=10, col2: int=9, col3: int=8, col4: int=18):
        self._row1=Pin(row1,Pin.OUT)
        self._row2=Pin(row2,Pin.OUT)
        self._row3=Pin(row3,Pin.OUT)
        self._row4=Pin(row4,Pin.OUT)
        self._col1=Pin(col1,Pin.IN,Pin.PULL_DOWN)
        self._col2=Pin(col2,Pin.IN,Pin.PULL_DOWN)
        self._col3=Pin(col3,Pin.IN,Pin.PULL_DOWN)
        self._col4=Pin(col4,Pin.IN,Pin.PULL_DOWN)
        
    
    def scan(self):
        global lastChangeTime
        nowTime=time.ticks_ms()
        if(nowTime-lastChangeTime>10):
            lastChangeTime=nowTime
            if(self._readCol()!=0):
                State=self._readCol()
                return State
            
    def _readRow1(self):
        self._setRow(1)
        if(self._col1.value()==1):
            keyState='1'
        elif(self._col2.value()==1):
            keyState='2'
        elif(self._col3.value()==1):
            keyState='3'
        elif(self._col4.value()==1):
            keyState='A'
        else:
            keyState=0
        return keyState

    def _readRow2(self):
        self._setRow(2)
        if(self._col1.value()==1):
            keyState='4'
        elif(self._col2.value()==1):
            keyState='5'
        elif(self._col3.value()==1):
            keyState='6'
        elif(self._col4.value()==1):
            keyState='B'
        else:
            keyState=0 
        return keyState

    def _readRow3(self):
        self._setRow(3)
        if(self._col1.value()==1):
            keyState='7'
        elif(self._col2.value()==1):
            keyState='8'
        elif(self._col3.value()==1):
            keyState='9'
        elif(self._col4.value()==1):
            keyState='C'
        else:
            keyState=0 
        return keyState
    
    def _readRow4(self):
        self._setRow(4)
        if(self._col1.value()==1):
            keyState='*'
        elif(self._col2.value()==1):
            keyState='0'
        elif(self._col3.value()==1):
            keyState='#'
        elif(self._col4.value()==1):
            keyState='D'
        else:
            keyState=0
        return keyState
    
    def _readCol(self):
        data_buffer1=self._readRow1()
        data_buffer2=self._readRow2()
        data_buffer3=self._readRow3()
        data_buffer4=self._readRow4()
        if (data_buffer1!=0):
            return data_buffer1
        elif (data_buffer2!=0):
            return data_buffer2
        elif (data_buffer3!=0):
            return data_buffer3
        elif (data_buffer4!=0):
            return data_buffer4

    def _setRow(self,num):
        if num==1:
            self._row1.on()
            self._row2.off()
            self._row3.off()
            self._row4.off()
        if num==2:
            self._row1.off()
            self._row2.on()
            self._row3.off()
            self._row4.off()
        if num==3:
            self._row1.off()
            self._row2.off()
            self._row3.on()
            self._row4.off()
        if num==4:
            self._row1.off()
            self._row2.off()
            self._row3.off()
            self._row4.on()
            
        
        
        

