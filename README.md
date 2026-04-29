# 🔐 Smart Door Lock System using Raspberry Pi Pico (IoT)

## 📌 Project Overview

The Smart Door Lock System is an Internet of Things (IoT)-based embedded solution designed to provide secure and remote-controlled access to a door locking mechanism. The system leverages a Raspberry Pi Pico microcontroller, along with sensors and actuators, to enable real-time monitoring and control via a web interface.

This project demonstrates the integration of embedded systems, networking, and automation to build a functional smart security system suitable for home and small-scale applications.

---

## 🎯 Objectives

- To design and implement a smart door locking mechanism  
- To enable remote access control using a web-based interface  
- To integrate motion detection for enhanced security  
- To develop a lightweight IoT system using MicroPython  
- To demonstrate real-time interaction between hardware and software  

---

## 🚀 Key Features

-  🌐 Remote door lock/unlock using browser-based interface  
-  🔁 Real-time system response with minimal latency  
-  👁️ Motion detection using PIR sensor  
-  🖥️ Embedded web server running on Raspberry Pi Pico  
-  ⚡ Lightweight and cost-effective implementation  
-  🧠 Modular system design for scalability  

---

## 🧠 System Description

The system operates by hosting a local web server on the Raspberry Pi Pico. When a user accesses the device’s IP address through a browser, a control interface is displayed. The user can send commands to open or close the door.

The microcontroller processes these commands and controls a servo motor that physically locks or unlocks the door. Additionally, a PIR sensor continuously monitors motion near the door, enabling basic security awareness.

---

## 🧩 System Components

### Hardware Components

- Raspberry Pi Pico (RP2040 microcontroller)  
- Micro Servo Motor (for locking mechanism)  
- PIR Sensor (motion detection)  
- Jumper Wires (connections)  
- USB Cable (power and programming)  
- Cardboard structure (for physical prototype)  

---

### Software Components

- MicroPython  
- Thonny IDE  
- Socket Programming (for web server)  
- HTML (for user interface)  

---

## ▶️ Entry Point

- The main program file is located at : <span style="color: green;"> code/main.py </span>

---

## ⚙️ System Architecture (High-Level)

The system follows a layered architecture:

1. **Input Layer**
   - PIR sensor detects motion  

2. **Processing Layer**
   - Raspberry Pi Pico processes inputs and requests  

3. **Communication Layer**
   - WiFi + socket server handles HTTP requests  

4. **Output Layer**
   - Servo motor performs locking/unlocking  

5. **Presentation Layer**
   - Web interface displayed in browser  

---

## 🔄 Working Principle

1. The Raspberry Pi Pico initializes and connects to WiFi  
2. A socket-based web server is started  
3. The user accesses the system via IP address  
4. The web interface provides control options  
5. User actions generate HTTP requests:
   - `/DoorOpen` → Unlock door  
   - `/DoorClose` → Lock door  
6. The Pico processes the request  
7. The servo motor rotates accordingly  
8. PIR sensor continuously monitors motion  
9. System updates and responds in real time  

---

## 🔌 Hardware Connections (Summary)

### Servo Motor
- Signal → GP5  
- VCC → 5V / 3.3V  
- GND → GND  

### PIR Sensor
- VCC → 3.3V  
- GND → GND  
- OUT → GP6  

### Power Supply
- Powered via USB cable  

---

## 📁 Project Structure 
Smart-Door-Lock-IOT-5th-Semester-BCT-/ <br>
│ <br>
├── certificates/ <br>
│      └── iot-training-certificate.pdf <br>
├── code/ # MicroPython source code <br>
│      ├── index.html # Optional UI separation <br>
│      └── main.py # Main program <br>
│ <br>
├── docs/ # Documentation files <br>
│      ├── architecture.md <br>
│      ├── project-report.pdf <br>
│      ├── working.md <br>
│      └── setup-guide.md <br>
│ <br>
├── hardware/ # Hardware documentation <br>
│      ├── components.md <br>
│      └── connections.md <br>
│ <br>
├── README.md <br>
└── screenhshots.md <br>

---

## ⚙️ Setup Instructions

Detailed setup instructions are available in:

👉 `docs/setup-guide.md`

---

## 📚 Documentation

- Architecture → `docs/architecture.md`  
- Working Principle → `docs/working.md`  
- Setup Guide → `docs/setup-guide.md`  

---

## 🔐 Security Considerations

- The current system operates on a local network  
- No authentication mechanism is implemented  
- Data transmission is not encrypted  

Future improvements can include:
- Password-based access  
- OTP authentication  
- Secure communication protocols  

---

## ⚠️ Limitations

- Limited to local network access  
- No user authentication system  
- Single-threaded request handling  
- Dependent on WiFi availability  

---

## 🔮 Future Scope

- Integration with cloud platforms  
- Mobile application control  
- Biometric authentication (fingerprint/face recognition)  
- AI-based intrusion detection  
- Multi-user access management  
- Real-time notification system  

---

## 📜 Certification

- This project was developed as part of a 30-hour IoT training program conducted by Ardent Computech Pvt. Ltd.
- The training focused on embedded systems, sensor integration, and real-time IoT applications.

🔗 View Certificate: [IoT Training Certificate](certificates/iot-training-certificate.pdf)

---

## 🧪 Testing & Validation

The system was tested for:
- Web interface accessibility  
- Servo motor response accuracy  
- PIR sensor motion detection  
- Real-time command execution  

---

## 📌 Conclusion

The Smart Door Lock System demonstrates the effective integration of IoT, embedded systems, and automation. It provides a practical and scalable solution for smart access control and highlights the potential for future enhancements in security and user experience.

---

## 👨‍💻 Author

**Indrajit Bhowmick**  
B.Tech (Electronics and Communication Engineering)

---

## ⭐ Repository Support

If you find this project useful, consider giving it a ⭐ on GitHub.
