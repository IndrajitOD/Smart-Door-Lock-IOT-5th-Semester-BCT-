import network
import socket
from time import sleep
from machine import Pin,PWM
from picozero import Servo

servo = Servo(5)
// Your WiFi credentials. 
// Set password to "" for open networks.
ssid = 'POCO M6 Pro 5G'
password = 'Anamika@1998

pir= Pin(6,Pin.IN)

def connect():
#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
print('Waiting for connection .')
sleep(1) 
ip = wlan.ifconfig()[0]
print(f'Connected on {ip}')
return ip

def open_socket(ip):
# Open a socket
address = (ip, 80)
connection = socket.socket()
connection.bind(address)

connection.listen(1)
return connection
def webpage(state):
#Template HTML
html = f"""
<!DOCTYPE html>
<html>
<form action="./DoorOpen">
<input type="submit" value="Door Open" />
</form>
<form action="./DoorClose">
<input type="submit" value="Door Close" />
</form>
</body>
</html>
"""
return str(html)
def serve(connection):
#Start a web server
state = 'Close'
servo.min()
while True:
pir==1
client = connection.accept()[0]
request = client.recv(1024)
request = str(request)
try:
request = request.split()[1]
except IndexError:
pass
if request == '/DoorOpen?':
servo.max()
state = 'Open'
elif request =='/DoorClose?':
servo.min()
state = 'Close'
#temperature = pico_temp_sensor.temp
html = webpage(state)
client.send(html)
client.close()
try:
ip = connect()
connection = open_socket(ip)
serve(connection)
except KeyboardInterrupt:
machine.reset()














