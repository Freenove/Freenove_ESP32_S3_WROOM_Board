#define ARDUINO_USB_MODE 0
#ifndef ARDUINO_USB_MODE
#error This ESP32 SoC has no Native USB interface
#elif ARDUINO_USB_MODE == 1
#warning This sketch should be used when USB is in OTG mode
void setup() {}
void loop() {}
#else

#include "USB.h"
#include "USBHIDConsumerControl.h"
USBHIDConsumerControl ConsumerControl;

// set pin numbers for the five buttons:
const int upButton = 14;
const int leftButton = 13;
const int downButton = 12;
const int rightButton = 11;

void setup() {
  pinMode(upButton, INPUT_PULLUP);
  pinMode(downButton, INPUT_PULLUP);
  pinMode(leftButton, INPUT_PULLUP);
  pinMode(rightButton, INPUT_PULLUP);

  ConsumerControl.begin();
  USB.begin();
}

void loop() {
  // use the pushbuttons to control the keyboard:
  if (digitalRead(upButton) == LOW) {
    ConsumerControl.press(CONSUMER_CONTROL_VOLUME_INCREMENT);
    ConsumerControl.release();
  }
  if (digitalRead(downButton) == LOW) {
    ConsumerControl.press(CONSUMER_CONTROL_VOLUME_DECREMENT);
    ConsumerControl.release();
  }
  if (digitalRead(leftButton) == LOW) {
    ConsumerControl.press(CONSUMER_CONTROL_BRIGHTNESS_INCREMENT);
    ConsumerControl.release();
  }
  if (digitalRead(rightButton) == LOW) {
    ConsumerControl.press(CONSUMER_CONTROL_BRIGHTNESS_DECREMENT);
    ConsumerControl.release();
  }
  delay(100);
}
#endif /* ARDUINO_USB_MODE */
