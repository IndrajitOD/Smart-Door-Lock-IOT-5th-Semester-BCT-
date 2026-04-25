**# 🧠 System Architecture — Smart Door Lock (IoT)**

## 📌 Overview

The Smart Door Lock System is an IoT-based embedded solution designed to provide remote access control and enhanced security using a Raspberry Pi Pico. It integrates sensing, actuation, and networking to enable real-time interaction through a web interface.

The system follows a **modular architecture**, separating hardware interaction, processing logic, and user interface layers.

---

## 🧩 Core Components

### 🔹 1. Microcontroller (Raspberry Pi Pico)
- Acts as the **central processing unit**
- Executes MicroPython code
- Handles sensor input, user requests, and actuator control

---

### 🔹 2. PIR Sensor (Input Layer)
- Detects motion using infrared radiation
- Sends HIGH/LOW signal to Pico
- Enables security monitoring

---

### 🔹 3. Servo Motor (Actuation Layer)
- Controls physical locking/unlocking
- Operates based on PWM signals
- Rotates between defined angles:
  - 0° → Locked
  - 90° → Unlocked

---

### 🔹 4. Network Interface (WiFi)
- Connects Pico to local network
- Enables communication via IP address
- Uses socket programming for HTTP requests

---

### 🔹 5. Web Interface (User Layer)
- Accessible via browser
- Provides control buttons:
  - Open Door
  - Close Door
- Displays real-time door status

---

## 🔄 System Workflow

1. System boots and connects to WiFi  
2. Pico starts a local web server  
3. User opens browser and enters device IP  
4. HTML interface is loaded  
5. User clicks action button:
   - `/DoorOpen` → unlock
   - `/DoorClose` → lock  
6. Pico processes request  
7. Servo motor executes action  
8. Status is updated and sent back to user  

---

## 🧭 Architecture Layers

### 🟢 1. Input Layer
- PIR Sensor  
- Detects environmental motion  

---

### 🔵 2. Processing Layer
- Raspberry Pi Pico  
- Decision-making logic  
- Handles HTTP requests  

---

### 🔴 3. Output Layer
- Servo Motor  
- Executes locking mechanism  

---

### 🟡 4. Communication Layer
- WiFi + Socket Server  
- Enables browser interaction  

---

### 🟣 5. Presentation Layer
- HTML Interface  
- Displays system state  

---

## 🔗 Data Flow

User (Browser)
↓
HTTP Request (/DoorOpen / DoorClose)
↓
Raspberry Pi Pico (Processing)
↓
Servo Motor (Action)
↓
Status Update
↓
HTML Response → User

---

## ⚙️ Design Principles Used

- **Modularity** → Separate UI and logic  
- **Real-time Processing** → Immediate response to user input  
- **Low Power Embedded Design** → Efficient microcontroller usage  
- **Scalability Ready** → Can integrate cloud, AI, biometrics  

---

## 🔐 Security Considerations

- Local network-based control (basic security)  
- Can be enhanced with:
  - Authentication system  
  - Encrypted communication  
  - OTP / biometric verification  

---

## 🚀 Future Enhancements (Architecture Level)

- Cloud integration for remote access  
- Mobile application interface  
- AI-based anomaly detection  
- Multi-user access control system  
- Camera-based verification  

---

**## 📌 Summary**

The system demonstrates a **complete IoT pipeline**, combining sensing, processing, communication, and actuation into a single embedded solution. It serves as a strong foundation for building advanced smart home security systems.
