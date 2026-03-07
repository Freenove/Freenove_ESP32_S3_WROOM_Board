/*
  KeyboardAndMouseControl

  Hardware:
  - five pushbuttons attached to D12, D13, D14, D15, D0

  The mouse movement is always relative. This sketch reads four pushbuttons, and
  uses them to set the movement of the mouse.

  WARNING: When you use the Mouse.move() command, the Arduino takes over your
  mouse! Make sure you have control before you use the mouse commands.

  created 15 Mar 2012
  modified 27 Mar 2012
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/KeyboardAndMouseControl
*/
#define ARDUINO_USB_MODE 0
#ifndef ARDUINO_USB_MODE
#error This ESP32 SoC has no Native USB interface
#elif ARDUINO_USB_MODE == 1
#warning This sketch should be used when USB is in OTG mode
void setup() {}
void loop() {}
#else

#include "USB.h"
#include "USBHIDKeyboard.h"
USBHIDKeyboard Keyboard;

// set pin numbers for the five buttons:
const int upButton = 14;
const int leftButton = 13;
const int downButton = 12;
const int rightButton = 11;
const int mouseButton = 0;

void setup() {  // initialize the buttons' inputs:
  pinMode(upButton, INPUT_PULLUP);
  pinMode(downButton, INPUT_PULLUP);
  pinMode(leftButton, INPUT_PULLUP);
  pinMode(rightButton, INPUT_PULLUP);
  pinMode(mouseButton, INPUT_PULLUP);

  Keyboard.begin();
  USB.begin();
}

void loop() {
  // use the pushbuttons to control the keyboard:
  if (digitalRead(upButton) == LOW) {
    Keyboard.write(KEY_UP_ARROW);
  }
  if (digitalRead(downButton) == LOW) {
    Keyboard.write(KEY_DOWN_ARROW);
  }
  if (digitalRead(leftButton) == LOW) {
    Keyboard.write(KEY_LEFT_ARROW);
  }
  if (digitalRead(rightButton) == LOW) {
    Keyboard.write(KEY_RIGHT_ARROW);
  }
  if (digitalRead(mouseButton) == LOW) {
    Keyboard.write(KEY_SPACE);
  }
  delay(5);
}
#endif /* ARDUINO_USB_MODE */
