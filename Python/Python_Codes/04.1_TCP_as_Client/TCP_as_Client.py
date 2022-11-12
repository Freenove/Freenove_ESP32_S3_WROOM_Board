import network
import socket
import time

ssidRouter     =  "********"       #Enter the router name
passwordRouter =  "********"       #Enter the router password
host           =  "192.168.1.139"  #input the remote server
port           =   8888            #input the remote port

wlan=None
s=None

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True
try:
  connectWifi(ssidRouter,passwordRouter)
  s = socket.socket()
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.connect((host,port))
  print("TCP Connected to:", host, ":", port)
  s.send('Hello')
  s.send('This is my IP.')
  while True:
    data = s.recv(1024)
    if(len(data) == 0):
      print("Close socket")
      s.close()
      break
    print(data)
    ret=s.send(data)
except:
  print("TCP close, please reset!")
  if (s):
    s.close()
  wlan.disconnect()
  wlan.active(False)