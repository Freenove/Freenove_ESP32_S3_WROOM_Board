# The firmware for this chapter is provided by: https://github.com/cnadler86/micropython-camera-API. 
# Thanks to cnadler86 for the open source contribution.

import network
import socket
import time
from camera import Camera, FrameSize, PixelFormat

# --- Configuration Parameters ---
SSID = '********'             # WiFi SSID
PASSWORD = '********'         # WiFi Password
CURRENT_FRAME_SIZE = FrameSize.QQVGA  # Camera resolution: QQVGA (160x120), QVGA (320x240), etc.
CAM_PIXEL_FORMAT = PixelFormat.RGB565 # Pixel format: RGB565 is required for this software decoding method
XCLK_FREQ = 10000000          # Camera clock frequency (10MHz)
DISPLAY_WIDTH = 320           # Fixed display width on the webpage (CSS pixels)
DISPLAY_HEIGHT = 240          # Fixed display height on the webpage (CSS pixels)

def get_resolution_dimensions(frame_size):
    """
    Returns the actual width and height in pixels based on the FrameSize enum.
    """
    if frame_size == FrameSize.QQVGA:
        return 160, 120
    elif frame_size == FrameSize.QVGA:
        return 320, 240
    elif frame_size == FrameSize.VGA:
        return 640, 480
    else:
        # Default fallback to QQVGA
        return 160, 120

def connect_wifi(ssid, password):
    """
    Connects to the specified WiFi network and returns the local IP address.
    Blocks execution until connected.
    """
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        time.sleep(1)
    return station.ifconfig()[0]

def init_camera(frame_size, pixel_format, xclk_freq):
    """
    Initializes the camera hardware with the specified settings.
    """
    cam = Camera(frame_size=frame_size, pixel_format=pixel_format, xclk_freq=xclk_freq, init=False)
    cam.init()
    return cam

def generate_html(cam_width, cam_height):
    """
    Generates the HTML page with embedded JavaScript.
    Injects the actual camera resolution into the JS variables.
    The CSS forces the canvas to display at DISPLAY_WIDTH x DISPLAY_HEIGHT,
    while the JS handles the actual pixel data decoding.
    """
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>ESP32 Camera Stream</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }}
        .video-container {{
            text-align: center;
        }}
        canvas {{
            /* Force display size to 320x240 regardless of actual resolution */
            width: {DISPLAY_WIDTH}px;
            height: {DISPLAY_HEIGHT}px;
            border: 1px solid #ccc;
            background-color: #000;
            image-rendering: auto; /* Smooth scaling */
        }}
    </style>
</head>
<body>
    <div class="video-container">
        <h1>Stream (Actual: {cam_width}x{cam_height}, Display: {DISPLAY_WIDTH}x{DISPLAY_HEIGHT})</h1>
        <canvas id="videoCanvas"></canvas>
        <div id="status">Connecting...</div>
    </div>
    <script>
        const canvas = document.getElementById('videoCanvas');
        const ctx = canvas.getContext('2d');
        const statusDiv = document.getElementById('status');
        
        // Actual resolution injected from Python
        const ACTUAL_WIDTH = {cam_width};
        const ACTUAL_HEIGHT = {cam_height};
        const EXPECTED_DATA_LENGTH = ACTUAL_WIDTH * ACTUAL_HEIGHT * 2; // 2 bytes per pixel in RGB565

        function fetchImage() {{
            fetch('/frame')
                .then(response => response.arrayBuffer())
                .then(data => {{
                    if (!data || data.byteLength === 0) {{
                        setTimeout(fetchImage, 100);
                        return;
                    }}
                    
                    const uint8Array = new Uint8Array(data);
                    let w = ACTUAL_WIDTH;
                    let h = ACTUAL_HEIGHT;
                    
                    // Auto-detect resolution if data length doesn't match expected
                    if (uint8Array.length !== EXPECTED_DATA_LENGTH) {{
                        if (uint8Array.length === 160 * 120 * 2) {{ w = 160; h = 120; }}
                        else if (uint8Array.length === 320 * 240 * 2) {{ w = 320; h = 240; }}
                        else if (uint8Array.length === 640 * 480 * 2) {{ w = 640; h = 480; }}
                        else {{
                            setTimeout(fetchImage, 1000);
                            return;
                        }}
                    }}

                    // Swap bytes for RGB565 (Little Endian to Big Endian conversion)
                    const swappedArray = new Uint8Array(uint8Array.length);
                    for (let i = 0; i < uint8Array.length; i += 2) {{
                        swappedArray[i] = uint8Array[i+1];
                        swappedArray[i+1] = uint8Array[i];
                    }}
                    
                    // Convert RGB565 to RGBA8888 for Canvas rendering
                    const rgb565Array = new Uint16Array(swappedArray.buffer);
                    const rgbaArray = new Uint8ClampedArray(w * h * 4);
                    
                    for (let i = 0; i < rgb565Array.length; i++) {{
                        const color = rgb565Array[i];
                        // Extract 5-bit R, 6-bit G, 5-bit B and scale to 8-bit
                        const r = ((color >> 11) & 0x1F) << 3;
                        const g = ((color >> 5) & 0x3F) << 2;
                        const b = (color & 0x1F) << 3;
                        
                        const idx = i * 4;
                        rgbaArray[idx] = r;
                        rgbaArray[idx + 1] = g;
                        rgbaArray[idx + 2] = b;
                        rgbaArray[idx + 3] = 255; // Alpha channel
                    }}
                    
                    // Set internal canvas resolution to match actual image data
                    canvas.width = w;
                    canvas.height = h;
                    const imageData = new ImageData(rgbaArray, w, h);
                    ctx.putImageData(imageData, 0, 0);
                    statusDiv.textContent = `Streaming (${{w}}x${{h}})`;
                    
                    // Request next frame immediately
                    setTimeout(fetchImage, 0); 
                }})
                .catch(error => {{
                    setTimeout(fetchImage, 1000);
                }});
        }}
        fetchImage();
    </script>
</body>
</html>
"""

def handle_frame_request(client, cam):
    """
    Captures a raw RGB565 frame from the camera and sends it to the client.
    """
    frame = cam.capture()
    if frame:
        headers = b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nCache-Control: no-cache\r\n\r\n'
        client.send(headers)
        client.send(frame)
    else:
        client.send(b'HTTP/1.1 500 Internal Server Error\r\n\r\n')

def handle_html_request(client, html_content):
    """
    Sends the main HTML page to the client.
    """
    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html_content
    client.send(response.encode())

def handle_client(client, cam, html_content):
    """
    Handles an incoming HTTP request from a client.
    Routes to either frame streaming or HTML page serving.
    """
    try:
        request = client.recv(1024).decode()
        if 'GET /frame' in request:
            handle_frame_request(client, cam)
        elif 'GET /' in request or 'GET /stream' in request:
            handle_html_request(client, html_content)
        else:
            client.close()
    except OSError as e:
        print(e)
    finally:
        client.close()

def main():
    """
    Main entry point: Initializes WiFi, Camera, and starts the Web Server.
    """
    # Get dimensions for HTML injection
    cam_width, cam_height = get_resolution_dimensions(CURRENT_FRAME_SIZE)
    
    # Connect to WiFi
    ip_address = connect_wifi(SSID, PASSWORD)
    print(f'Connected! IP: {ip_address}')
    
    # Initialize Camera
    cam = init_camera(CURRENT_FRAME_SIZE, CAM_PIXEL_FORMAT, XCLK_FREQ)
    print('Camera initialized.')
    
    # Generate HTML content once
    html_content = generate_html(cam_width, cam_height)
    
    # Start TCP Server
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    print(f'Server on: {addr}')
    
    # Main loop: Accept connections and handle clients
    while True:
        try:
            client, addr = s.accept()
            handle_client(client, cam, html_content)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()