import network
import socket
from time import sleep
from machine import Pin
from picozero import Servo
import machine

# -------------------- CONFIG --------------------
SSID = 'YOUR_WIFI_NAME'
PASSWORD = 'YOUR_WIFI_PASSWORD'

SERVO_PIN = 5
PIR_PIN = 6

# -------------------- HARDWARE SETUP --------------------
servo = Servo(SERVO_PIN)
pir = Pin(PIR_PIN, Pin.IN)

# -------------------- WIFI CONNECTION --------------------
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to WiFi...", end="")

    while not wlan.isconnected():
        print(".", end="")
        sleep(1)

    ip = wlan.ifconfig()[0]
    print("\nConnected! IP Address:", ip)
    return ip


# -------------------- WEB SERVER --------------------
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print("Server listening on", address)
    return connection


# -------------------- HTML PAGE --------------------
def webpage(state):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Door Lock</title>
    </head>
    <body>
        <h2>Door Status: {state}</h2>

        <form action="/DoorOpen">
            <input type="submit" value="Door Open" />
        </form>

        <form action="/DoorClose">
            <input type="submit" value="Door Close" />
        </form>
    </body>
    </html>
    """
    return html


# -------------------- MAIN SERVER LOOP --------------------
def serve(connection):
    state = "Closed"
    servo.min()  # Ensure door is locked initially

    while True:
        client, addr = connection.accept()
        print("Client connected from", addr)

        request = client.recv(1024)
        request = str(request)
        print("Request:", request)

        # Extract URL path
        try:
            request_path = request.split(' ')[1]
        except:
            request_path = "/"

        # Handle actions
        if request_path == '/DoorOpen':
            servo.max()
            state = "Open"
            print("Door Opened")

        elif request_path == '/DoorClose':
            servo.min()
            state = "Closed"
            print("Door Closed")

        # PIR detection (optional logic)
        if pir.value() == 1:
            print("Motion Detected!")

        # Send response
        response = webpage(state)
        client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        client.send(response)
        client.close()


# -------------------- MAIN EXECUTION --------------------
try:
    ip = connect_wifi()
    connection = open_socket(ip)
    serve(connection)

except KeyboardInterrupt:
    print("System stopped. Restarting...")
    machine.reset()
