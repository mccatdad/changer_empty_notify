import network
import socket
import time
from machine import Pin

def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

NTFY_TOPIC = ''
LOCATIONS = [("Orange_Cat_HQ", "ssid", "password"),("location", "ssid", "password")]

changer_out_at = 'undefined!'
led = Pin(10, Pin.OUT)

i=0
while i < 3:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    i = i + 1

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

networks = wlan.scan()
print(wlan.isconnected())
wlan.disconnect()
print(wlan.isconnected())
for ssid in networks:
    for location in LOCATIONS:
        if ssid[0].decode('ASCII') == location[1]:
            print(ssid[0].decode('ASCII'))
            wlan.connect(location[1], location[2])
            time.sleep(10)
            changer_out_at = location[0]
        if wlan.isconnected():
            print("wlan is connected")
            break
    if wlan.isconnected():
        break
    
http_get('http://ntfy.sh/%s/publish?message=Change+Machine+out+at+%s' % (NTFY_TOPIC , changer_out_at))

