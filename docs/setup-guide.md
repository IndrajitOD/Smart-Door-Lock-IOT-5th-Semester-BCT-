# ⚙️ Setup Guide — Smart Door Lock System

## 📌 Overview

This guide explains how to set up and run the Smart Door Lock System using Raspberry Pi Pico, MicroPython, and connected hardware components.

Follow the steps carefully to ensure proper functionality.

---

## 🧰 Hardware Requirements

- Raspberry Pi Pico  
- Micro Servo Motor  
- PIR Sensor  
- Jumper Wires (Male-Female / Female-Female)  
- USB Cable (for power and programming)  

---

## 💻 Software Requirements

- Thonny IDE (recommended for MicroPython)  
- MicroPython firmware for Raspberry Pi Pico  
- Web browser (Chrome / Edge / Firefox)  

---

## 🔌 Hardware Connections

### 🔹 Servo Motor
- Signal (Orange/Yellow) → GPIO Pin (e.g., GP5)  
- VCC (Red) → 5V or 3.3V  
- GND (Brown/Black) → GND  

---

### 🔹 PIR Sensor
- VCC → 3.3V  
- GND → GND  
- OUT → GPIO Pin (e.g., GP6)  

---

## 🧠 Software Setup

### Step 1: Install Thonny
- Download from: https://thonny.org  
- Install and open Thonny  

---

### Step 2: Configure Interpreter
- Go to **Tools → Options → Interpreter**
- Select:  
  **MicroPython (Raspberry Pi Pico)**  

---

### Step 3: Connect Raspberry Pi Pico
- Use USB cable to connect Pico to your system  
- Ensure it is detected in Thonny  

---

### Step 4: Upload Code
- Open `main.py` in Thonny  
- Update WiFi credentials:

```python
SSID = "your_wifi_name"
PASSWORD = "your_wifi_password"
```
Click Run or save as main.py on Pico

---

##🌐 Running the System

### Step 5: Connect to WiFi
- After running the code, Pico will attempt WiFi connection
- Wait until IP address is printed in the console

---

### Step 6: Access Web Interface
- Open browser
- Enter the IP address shown in Thonny
Example:  http://192.168.x.x

---

Step 7: Control the Door
- Click Open Door → Unlock
- Click Close Door → Lock
- Observe servo motor movement

---

## 📁 Optional: Using Separate HTML File

### If using index.html instead of inline HTML:

- Place index.html in the same directory as main.py
- Modify Python code to load HTML file
Refer to comments inside index.html for exact instructions.

---

## 🧪 Testing & Validation
- Ensure servo rotates correctly
- Verify PIR sensor detects motion
- Confirm web interface loads without error
- Check response time of commands

---

## ⚠️ Troubleshooting

### ❌ WiFi Not Connecting
- Check SSID and password
- Ensure 2.4GHz network (Pico limitation)

---

## ❌ No IP Address Displayed
- Restart Pico
- Re-run code

---

## ❌ Servo Not Moving
- Check wiring
- Ensure correct GPIO pin

---

## ❌ Webpage Not Loading
- Verify IP address
- Ensure same network (device & Pico)

---

## 🔐 Safety Notes
- Do not overload GPIO pins
- Use proper power supply for servo
- Avoid short circuits

---

## 📌 Conclusion
After completing these steps, the Smart Door Lock System should be fully functional and controllable via a web interface within the local network.
