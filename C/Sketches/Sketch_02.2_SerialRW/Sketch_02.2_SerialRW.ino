/**********************************************************************
  Filename    : SerialRW
  Description : Use UART read and write data between ESP32 and PC.
  Auther      : www.freenove.com
  Modification: 2026/01/12
**********************************************************************/
String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(115200);
  Serial.println("\nESP32S3 initialization completed!");
  Serial.println("Please input some characters,");
  Serial.println("select \"Newline\" below and Ctrl + Enter to send message to ESP32S3.");
  Serial.println("Ready to receive data...\n");
}

void loop() {
  if (Serial.available()) {
    inputString = Serial.readStringUntil('\n');

    // trim() removes leading and trailing whitespace characters, including \r, \n, tabs, etc.
    inputString.trim();
    
    if (inputString.length() > 0) {
      stringComplete = true;
    }
  }

  if (stringComplete) {
    Serial.printf("inputString: %s\r\n", inputString.c_str());
    inputString = "";
    stringComplete = false;
  }
}