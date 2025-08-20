# This section uses firmware from Lemariva's Micropython-camera-driver.  
# for details, please refer to: https://github.com/lemariva/micropython-camera-driver  
import picoweb
import utime
import camera
import gc

SSID = "FYI_2.4G"         # Enter your WiFi name
PASSWORD = "freenove208"     # Enter your WiFi password

# Let ESP32 connect to wifi.
def wifi_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASSWORD) 
    start = utime.time()
    while not wlan.isconnected():
        utime.sleep(1)
        if utime.time()-start > 5:
            print("connect timeout!")
            break
    if wlan.isconnected():
        print('network config:', wlan.ifconfig())

# Initializing the Camera
def camera_init():
    # Disable camera initialization
    camera.deinit()
    # Enable camera initialization
    camera.init(0, d0=11, d1=9, d2=8, d3=10, d4=12, d5=18, d6=17, d7=16,
                format=camera.JPEG, framesize=camera.FRAME_VGA, 
                xclk_freq=camera.XCLK_10MHz,
                href=7, vsync=6, reset=-1, pwdn=-1,
                sioc=5, siod=4, xclk=15, pclk=13, fb_location=camera.PSRAM)

    camera.framesize(camera.FRAME_VGA) # Set the camera resolution
    # The options are the following:
    # FRAME_96X96 FRAME_QQVGA FRAME_QCIF FRAME_HQVGA FRAME_240X240
    # FRAME_QVGA FRAME_CIF FRAME_HVGA FRAME_VGA FRAME_SVGA
    # FRAME_XGA FRAME_HD FRAME_SXGA FRAME_UXGA
    # Note: The higher the resolution, the more memory is used.
    # Note: And too much memory may cause the program to fail.
    
    camera.flip(0)                       # Flip up and down window: 0-1
    camera.mirror(0)                     # Flip window left and right: 0-1
    camera.saturation(0)                 # saturation: -2,2 (default 0). -2 grayscale 
    camera.brightness(0)                 # brightness: -2,2 (default 0). 2 brightness
    camera.contrast(0)                   # contrast: -2,2 (default 0). 2 highcontrast
    camera.quality(10)                   # quality: # 10-63 lower number means higher quality
    # Note: The smaller the number, the sharper the image. The larger the number, the more blurry the image
    
    camera.speffect(camera.EFFECT_NONE)  # special effects:
    # EFFECT_NONE (default) EFFECT_NEG EFFECT_BW EFFECT_RED EFFECT_GREEN EFFECT_BLUE EFFECT_RETRO
    camera.whitebalance(camera.WB_NONE)  # white balance
    # WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME

# HTTP Response Content  
index_web="""
HTTP/1.0 200 OK\r\n
<html>
  <head>
    <title>Video Streaming</title>
  </head>
  <body>
    <h1>Video Streaming Demonstration</h1>
    <img src="/video" margin-top:100px; style="transform:rotate(180deg)"; />
  </body>
</html>
"""

# HTTP Response
def index(req, resp):
    # You can construct an HTTP response completely yourself, having
    yield from resp.awrite(index_web)

# Send camera pictures
def send_frame():
    buf = camera.capture()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n'
           + buf + b'\r\n')
    del buf
    gc.collect()
        
# Video transmission
def video(req, resp):
    yield from picoweb.start_response(resp, content_type="multipart/x-mixed-replace; boundary=frame")
    while True:
        yield from resp.awrite(next(send_frame()))
        gc.collect()


ROUTES = [
    # You can specify exact URI string matches...
    ("/", index),
    ("/video", video),
]


if __name__ == '__main__':
    
    import ulogging as logging
    logging.basicConfig(level=logging.INFO)
    camera_init()
    wifi_connect()

    #Create an app object that contains two decorators
    app = picoweb.WebApp(__name__, ROUTES)
    
    app.run(debug=1, port=80, host="0.0.0.0")
    # debug values:
    # -1 disable all logging
    # 0 (False) normal logging: requests and errors
    # 1 (True) debug logging
    # 2 extra debug logging

