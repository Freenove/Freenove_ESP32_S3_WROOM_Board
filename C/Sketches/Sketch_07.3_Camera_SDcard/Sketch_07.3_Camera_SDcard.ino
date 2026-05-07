/**********************************************************************
  Filename    : Camera and SDcard
  Description : Use the onboard buttons to take photo and save them to an SD card.
  Auther      : www.freenove.com
  Modification: 2022/11/02
**********************************************************************/
#include "esp_camera.h"
#define CAMERA_MODEL_ESP32S3_EYE
#include "camera_pins.h"
#include "ws2812.h"
#include "sd_read_write.h"

#define BUTTON_PIN  0

void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(false);
  Serial.println();
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  ws2812Init();
  sdmmcInit();
  //removeDir(SD_MMC, "/camera");
  createDir(SD_MMC, "/camera");
  listDir(SD_MMC, "/camera", 0);
  if(cameraSetup()==1){
    ws2812SetColor(2);
  }
  else{
    ws2812SetColor(1);
    return;
  }
}

void loop() {
  if(digitalRead(BUTTON_PIN)==LOW){
    delay(20);
    if(digitalRead(BUTTON_PIN)==LOW){
	  	ws2812SetColor(3);
      while(digitalRead(BUTTON_PIN)==LOW);
      camera_fb_t * fb = esp_camera_fb_get();
      if (fb != NULL) {
        int photo_index = readFileNum(SD_MMC, "/camera");
        if(photo_index != -1) {
          String path = "/camera/" + String(photo_index) + ".jpg";

          if (fb->format == PIXFORMAT_JPEG) {
            writejpg(SD_MMC, path.c_str(), fb->buf, fb->len);
            Serial.println("Direct JPEG save.");
          } 
          else {
            uint8_t *jpg_buf = NULL;
            size_t jpg_len = 0;
            
            if (frame2jpg(fb, 80, &jpg_buf, &jpg_len)) {
              writejpg(SD_MMC, path.c_str(), jpg_buf, jpg_len);
              free(jpg_buf);
            } else {
              Serial.println("JPEG compression failed!");
            }
          }
        }
        esp_camera_fb_return(fb);
      }
      else {
        Serial.println("Camera capture failed.");
      }
      ws2812SetColor(2);
    }
  }
}

int cameraSetup(void) {
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 10000000;
  config.frame_size = FRAMESIZE_QVGA;
  config.pixel_format = PIXFORMAT_RGB565; // for streaming
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 1;
  
  // if PSRAM IC present, init with UXGA resolution and higher JPEG quality
  // for larger pre-allocated frame buffer.
  if(psramFound()){
    config.jpeg_quality = 10;
    config.fb_count = 2;
    config.grab_mode = CAMERA_GRAB_LATEST;
  } else {
    // Limit the frame size when PSRAM is not available
    config.frame_size = FRAMESIZE_SVGA;
    config.fb_location = CAMERA_FB_IN_DRAM;
  }

  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return 0;
  }

  sensor_t * s = esp_camera_sensor_get();
  uint8_t pid = s->id.PID;

  if(pid == 0x45)
  {
    s->set_hmirror(s, 1);
    vTaskDelay(500);
    s->set_vflip(s, 1);       // Flip the image vertically
  }else if(pid == 0x26)
  {
    s->set_hmirror(s, 0);
    s->set_vflip(s, 0);       // Flip the image vertically
  }else if(pid == 0x9B)
  {
    s->set_hmirror(s, 0);
    vTaskDelay(500);
    s->set_vflip(s, 0);       // Flip the image vertically
  }
  else{
    s->set_hmirror(s, 0);
    s->set_vflip(s, 1);       // Flip the image vertically
  }
  s->set_brightness(s, 1);  // Slightly increase brightness
  s->set_saturation(s, 0);  // Reduce saturation
  s->set_ae_level(s, -3);   // Set exposure compensation level
  Serial.println("Camera configuration complete!");
  return 1;
}
